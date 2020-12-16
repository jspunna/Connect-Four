
#Test code for Class Board of the Connect4 project


from connect4_board import Board
import unittest
import os

class TestBoard(unittest.TestCase):

    # Testing the constructor
    def test_init(self):
        board = Board([1,2,3], [6,7,8], 'score_file1.txt', 'score_file2.txt')
        self.assertEqual(board.x, [1,2,3])
        self.assertEqual(board.y, [6,7,8])
        self.assertEqual(board.red_scorefile, 'score_file1.txt')
        self.assertEqual(board.yellow_scorefile, 'score_file2.txt')


    # Test for 'first_turn' method in the Board class
    def test_first_turn(self):
        board = Board([1,2,3], [6,7,8], 'file1.txt', 'file2.txt')
        var = board.first_turn()
        var = (var == 'Red' or var == 'Yellow')
        self.assertTrue(var)


    # Testing for 'make_tracker_board' method in the Board class
    def test_tracker_board(self):

        # Test 1 - Using two lists of same lengths
        board = Board([1,2,3,4], [6,7,8,9], 'file1.txt', 'file2.txt')
        self.assertEqual(board.make_tracker_board(),
                         [[(1, 6), (2, 6), (3, 6), (4, 6), (1, 7), (2, 7),
                           (3, 7)], [(4, 7), (1, 8), (2, 8), (3, 8), (4, 8),
                                     (1, 9), (2, 9)], [(3, 9), (4, 9)]])

        # Test 2- Using two lists of different lengths and neg/pos numbers
        board = Board([-4,-2,1,3], [-6,7], 'file1.txt', 'file2.txt')
        self.assertEqual(board.make_tracker_board(),
                         [[(-4, -6), (-2, -6), (1, -6), (3, -6), (-4, 7),
                           (-2, 7), (1, 7)], [(3, 7)]])

        # Test 3- Using two empty lists
        board = Board([], [], 'file1.txt', 'file2.txt')
        self.assertEqual(board.make_tracker_board(), [])        


    # Test for both initialize methods from a non-existent file
    def test_initalizing_scores_no_file(self):
        board = Board([1,2,3], [6,7,8], 'red_score.txt', 'yellow_score.txt')

        # Test 1- Method for red. Should return 0 
        if os.path.exists('r_score.txt'):
            os.remove('r_score.txt')
        self.assertEqual(board.initialize_red_score(), 0)      

        # Test 2- Method for yellow. Should return 0 
        if os.path.exists('y_score.txt'):
            os.remove('y_score.txt')
        self.assertEqual(board.initialize_yellow_score(), 0)


    # Testing initialize methods from score files for red & yellow
    def test_initalizing_scores_file(self):
        board = Board([1,2,3], [6,7,8], 'r_scoretest.txt', 'y_scoretest.txt')
        
        # Test 1- initialize from red file w/ score 3. 
        with open('r_scoretest.txt', 'w') as outfile:
            outfile.write('3')
        self.assertEqual(board.initialize_red_score(), 3)
        os.remove('r_scoretest.txt')      

        # Test 2- initialize from yellow file w/ a score 5. 
        with open('y_scoretest.txt', 'w') as outfile:
            outfile.write('5')
        self.assertEqual(board.initialize_yellow_score(), 5)
        os.remove('y_scoretest.txt')

    
def main():

    unittest.main()

main()
