import unittest
import sys

sys.path.append("/home/codio/workspace/") #have to tell the unittest the PATH to find boggle_solver.py and the Boggle Class

from boggle_solver import Boggle

class TestSuite_Alg_Scalability_Cases(unittest.TestCase):

  # ADD 4x4, 5x5, 6x6, 7x7...13x13, and LARGER Dictionaries
  def test_Normal_case_3x3(self): #failed fix it pls
    grid = [["A", "B", "C"],["D", "E", "F"],["G", "H", "I"]]
    dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["abc", "abdhi", "cfi", "dea"];
    expected = [x.upper() for x in expected]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)
  def test_Normal_case_4x4(self): #failed fix it pls
    grid = [
        ["T", "E", "S", "T"],
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["I", "J", "K", "L"]
    ]
    dictionary = ["test", "abcf", "efgh", "ijkl", "tbe", "abcd"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["TEST", "ABCF", "EFGH", "ABCD"]
    solution.sort()
    expected.sort()
    self.assertEqual(expected, solution)
  def test_Normal_case_5x5(self): #failed fix it pls
    grid = [
        ["A", "B", "C", "D", "E"],
        ["F", "G", "H", "I", "J"],
        ["K", "L", "M", "N", "O"],
        ["P", "Q", "R", "S", "T"],
        ["U", "V", "W", "X", "Y"]
    ]
    dictionary = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "afkpv"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["ABCDE", "FGHIJ", "KLMNO", "PQRST", "UVWXY", "AFKPV"]
    solution.sort()
    expected.sort()
    self.assertEqual(expected, solution)

class TestSuite_Simple_Edge_Cases(unittest.TestCase):
  #ADD MANY SIMPLE TEST CASES
  def test_SquareGrid_case_1x1(self):
    grid = [["A"]];
    dictionary = ["a", "b", "c"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)
    #ADD HERE
  def test_EmptyGrid_case_0x0(self):
      grid = [[]]
      dictionary = ["hello", "there", "general", "kenobi"]
      mygame = Boggle(grid, dictionary)
      solution = mygame.getSolution()
      solution = [x.upper() for x in solution]
      expected = []
      solution.sort()
      expected.sort()
      self.assertEqual(expected, solution)


  

class TestSuite_Complete_Coverage(unittest.TestCase):
  #ADD MANY COMPLEXED TEST CASES
  def test_case_1(self):  
    self.assertEqual(True, True)
  #ADD HERE
  def test_EveryLetter(self): #test if everytile makes up a word, would it still run
      grid = [
          ["C", "A", "T", "S"],
          ["D", "O", "G", "S"],
          ["B", "I", "R", "D"],
          ["F", "I", "S", "H"]
      ]
      dictionary = ["catsgodbirdhsif","cats", "dogs", "bird", "fish", "catdog", "birdfish"]
      mygame = Boggle(grid, dictionary)
      solution = mygame.getSolution()
      solution = [x.upper() for x in solution]
      expected = ["CATS", "DOGS", "BIRD", "FISH"]
      solution.sort()
      expected.sort()
      self.assertEqual(expected, solution)

  def test_NoWordsFound(self):
    grid = [["X", "Y"], ["Z", "Q"]]
    dictionary = ["hello", "world"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    solution.sort()
    expected.sort()
    self.assertEqual(expected, solution)

class TestSuite_Qu_and_St(unittest.TestCase):
  #ADD QU AND ST TEST CASES
  def test_case_1(self): 
    self.assertEqual(True, True)
  #ADD HERE
  def test_QU_handling(self): # wrong because lone 'Q' isnt allowed-> only 'qu' allowed 
      grid = [["Q", "U", "I", "C"], ["K", "B", "O", "X"], ["L", "A", "M", "P"], ["S", "T", "A", "R"]]
      dictionary = ["quick", "qubit", "star", "lamp", "box"]
      mygame = Boggle(grid, dictionary)
      solution = mygame.getSolution()
      solution = [x.upper() for x in solution]
      expected = ["QUICK", "STAR", "LAMP", "BOX"]
      solution.sort()
      expected.sort()
      self.assertEqual(expected, solution)

  def test_ST_handling(self): #wrong because lone 's' not allowed-> only 'st' allowed
    grid = [["S", "T", "O"], ["P", "A", "T"], ["E", "R", "S"]]
    dictionary = ["stop", "star", "stops", "pat"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["STOP", "STAR", "PAT"]
    solution.sort()
    expected.sort()
    self.assertEqual(expected, solution)

if __name__ == '__main__':
	unittest.main()

