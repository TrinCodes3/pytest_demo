class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = self.convert_grid_to_lowercase(grid)  # 2D list representing the board
        self.dictionary = self.convert_dictionary_to_lowercase(dictionary)  # list of words to search for
        self.solutions = []  # found words
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid and len(grid) > 0 and len(grid[0]) > 0 else 0
        self.fast_dict = {}
        self.solution_set = set()
        self.visited = None

    def convert_grid_to_lowercase(self, grid):
        """Convert all cells in grid to lowercase"""
        if not grid or not grid[0]:
            return grid
        
        new_grid = []
        for row in grid:
            new_row = []
            for cell in row:
                # Handle special tiles like "Qu" - convert to lowercase
                new_row.append(cell.lower())
            new_grid.append(new_row)
        return new_grid
    
    def convert_dictionary_to_lowercase(self, dictionary):
        """Convert all words in dictionary to lowercase"""
        return [word.lower() for word in dictionary]
    
    def getgrid(self):
        """Return the grid"""
        return self.grid
    
    def getdictionary(self):
        """Return the dictionary"""
        return self.dictionary
    
    def exists(self, word):
        """Check if a word exists in the dictionary"""
        return word.lower() in self.dictionary
    
    def has_prefix(self, prefix):
        """Check if any word in dictionary starts with the given prefix"""
        for word in self.dictionary:
            if word.startswith(prefix):
                return True
        return False
    
    def dfs(self, row, col, current_word):
        """Depth-first search to find words starting from position (row, col)"""
        # Check boundaries
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return
        
        # Check if cell already visited
        if self.visited[row][col]:
            return
        
        # Mark current cell as visited
        self.visited[row][col] = True
        
        # Get current cell value
        cell_value = self.grid[row][col]
        
        # Build new word
        new_word = current_word + cell_value
        
        # Check if this word exists in dictionary (minimum length 3)
        # IMPORTANT: Words cannot end with 'q' - only 'qu' is allowed
        if len(new_word) >= 3 and new_word in self.dictionary:
            # Make sure the word doesn't end with 'q' (should be 'qu' instead)
            if not new_word.endswith('q'):
                self.solution_set.add(new_word.upper())
        
        # REMOVED: The special handling that created words ending with 'q'
        # We don't add alternative words with 'q' anymore
        
        # Check if this prefix could lead to any word (pruning)
        if self.has_prefix(new_word):
            # Explore all 8 adjacent cells
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    self.dfs(row + dr, col + dc, new_word)
        
        # Backtrack: unmark current cell
        self.visited[row][col] = False
    
    def getSolution(self):
        """Main method to find all words in the boggle grid"""
        # Clear previous solutions
        self.solutions = []
        self.solution_set = set()
        
        # Handle edge cases
        if self.rows == 0 or self.cols == 0:
            return []
        
        # Initialize visited matrix
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        
        # Start DFS from each cell
        for i in range(self.rows):
            for j in range(self.cols):
                self.dfs(i, j, "")
        
        # Convert solution set to list
        self.solutions = list(self.solution_set)
        return self.solutions

def main():
    grid = [
        ["T", "W", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "Qu", "R"],
        ["O", "N", "T", "A"]
    ]

    dictionary = [
        "ego", "Quart", "Ten", "aab"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()