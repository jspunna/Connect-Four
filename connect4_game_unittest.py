
#Test code for Class Game of the Connect4 project

from connect4_game import Game
import unittest
import os

class TestGame(unittest.TestCase):

    # Testing the constructor
    def test_init(self):
        game = Game([-3, -2, -1, 0, 1, 2, 3], 'Red', [[1,2,3,4,5], [6,7,8,9,0]],
                    3 , 4, 'score_file1.txt', 'score_file2.txt')
        self.assertEqual(game.y_coords, [-3, -2, -1, 0, 1, 2, 3])
        self.assertEqual(game.turn, 'Red')
        self.assertEqual(game.board, [[1,2,3,4,5], [6,7,8,9,0]])
        self.assertEqual(game.r_score, 3)
        self.assertEqual(game.y_score, 4)
        self.assertEqual(game.red_scorefile, 'score_file1.txt')
        self.assertEqual(game.yellow_scorefile, 'score_file2.txt')
        self.assertEqual(game.circles_taken, [])
        self.assertEqual(game.move, 0)
        self.assertEqual(game.xclick, 0)
        self.assertEqual(game.yclick, 0)
        temp = (game.turn_display == object)
        self.assertFalse(temp)


    # Testing the 'get_clicked_column', which returns the x-cor of column
    def test_clicked_column(self):
        game = Game([1, 2, 3], 'Red', [[1,2,3], [6,7,8]],
                    3 , 4, 'score_file1.txt', 'score_file2.txt')

        # Test 1- Clicks are within range of arrows.
        game.xclick = -151
        game.yclick = 167
        self.assertEqual(game.get_clicked_column(), -150)
        game.xclick = -57
        game.yclick = 178
        self.assertEqual(game.get_clicked_column(), -50)
        game.xclick = 99
        game.yclick = 160
        self.assertEqual(game.get_clicked_column(), 100)

        # Test 2- Both clicks out of range, x not in range, and y not it range
        game.xclick = -151
        game.yclick = 100
        self.assertEqual(game.get_clicked_column(), None)
        game.xclick = 200
        game.yclick = 178
        self.assertEqual(game.get_clicked_column(), None)
        game.xclick = -197
        game.yclick = 43
        self.assertEqual(game.get_clicked_column(), None)

    # Testing 'click' method picks up coordinates & modifys click attributes
    def test_change_turn(self):
        game = Game([1, 2, 3], 'Red', [[1,2,3], [6,7,8]],
                    3 , 4, 'score_file1.txt', 'score_file2.txt')

        # Test 1- When current turn is red
        game.turn = 'Red'
        game.change_turn()
        self.assertEqual(game.turn, 'Yellow')        

        # Test 2 - When current is yellow
        game.turn = 'Yellow'
        game.change_turn()
        self.assertEqual(game.turn, 'Red')

        # Test 3 - Changing current color to white if current is not R or Y
        game.turn = 'Pink'
        game.change_turn()
        self.assertEqual(game.turn, 'White')

    def test_add_point(self):

        # Test 1- If winner turn is R, add point to only red score attribute
        game = Game([1, 2, 3], 'Red', [[1,2,3], [6,7,8]],
                    0 , 0, 'score_file1.txt', 'score_file2.txt')        
        game.turn = 'Red'
        game.add_point()
        self.assertEqual(game.r_score, 1)
        self.assertEqual(game.y_score, 0)

        # Test 2- If winner turn is Y, add point to only yellow score attribute
        game = Game([1, 2, 3], 'Red', [[1,2,3], [6,7,8]],
                    7 , 9, 'score_file1.txt', 'score_file2.txt')
        game.turn = 'Yellow'
        game.add_point()
        self.assertEqual(game.r_score, 7)
        self.assertEqual(game.y_score, 10)


    # Note: Turtle screen will pop up as a result of this test
    def test_is_move_valid(self):

        # Test 1- Empty circles taken list. Move adds to attribute move and list
        game = Game([-150,-100,-50,0,50,100], 'Red', [[1,2,3], [6,7,8]],
                    0 , 0, 'score_file1.txt', 'score_file2.txt')        
        game.circles_taken = []
        game.is_valid_move(-150)
        self.assertEqual(game.move, (-150,-150))
        self.assertEqual(game.circles_taken, [(-150,-150)])

        # Test 2- Adds next possible move for column, if previous move in list
        game.circles_taken = [(-150,-150)]
        game.is_valid_move(-150)
        self.assertEqual(game.move, (-150,-100))
        self.assertEqual(game.circles_taken, [(-150,-150), (-150,-100)])

        # Test 3- The next move is valid. 
        game.circles_taken = [(-150,-150)]
        temp = game.is_valid_move(-150)
        self.assertTrue(temp)

        # Test 4- The move is not valid is column is None
        game.circles_taken = [(-150,-150), (-150,-100)]
        var = game.is_valid_move(None)
        self.assertFalse(var)


    def test_write_score(self):

        # Test 1- If winner is R, write score in red file. Remove after test
        game = Game([1, 2, 3], 'Red', [[1,2,3], [6,7,8]],
                    5 , 8, 'red_score_test.txt', 'yellow_score_test.txt')        
        game.turn = 'Red'
        game.write_score()
        with open(game.red_scorefile, 'r') as infile:
            game.r_score = int(infile.read())      
        self.assertEqual(game.r_score, 5)
        self.assertEqual(game.y_score, 8)
        os.remove('red_score_test.txt')

        # Test 2- If winner is Y, write score in yellow file. Remove after test
        game = Game([1, 2, 3], 'Red', [[1,2,3], [6,7,8]],
                    5 , 8, 'red_score_test.txt', 'yellow_score_test.txt')        
        game.turn = 'Yellow'
        game.write_score()
        with open(game.yellow_scorefile, 'r') as infile:
            game.y_score = int(infile.read())      
        self.assertEqual(game.r_score, 5)
        self.assertEqual(game.y_score, 8)
        os.remove('yellow_score_test.txt')

    # Note: Turtle screen will pop up as a result of this test
    def test_click(self):
        game = Game([1, 2, 3], 'Red', [[1,2,3], [6,7,8]],
                    5 , 8, 'red_score_test.txt', 'yellow_score_test.txt')
        game.click(-151, 167)
        self.assertEqual(game.xclick, -151)
        self.assertEqual(game.yclick, 167)        


    def test_clear_turn(self):
        game = Game([1, 2, 3], 'Red', [[1,2,3], [6,7,8]], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')
        game.turn_display.clear()


    def test_moves_board(self):
        game = Game([1, 2, 3], 'Red',
                    [[(-150, -150), (-100, -150), (-50, -150),(0, -150),
                      (50, -150), (100, -150), (150, -150)],
                     [(-150, -100), (-100, -100), (-50, -100), (0, -100),
                      (50, -100), (100, -100), (150, -100)],
                     [(-150, -50), (-100, -50), (-50, -50), (0, -50),
                      (50, -50), (100, -50), (150, -50)],
                     [(-150, 0), (-100, 0), (-50, 0), (0, 0), (50, 0),
                      (100, 0), (150, 0)],
                     [(-150, 50), (-100, 50), (-50, 50), (0, 50), (50, 50),
                      (100, 50), (150, 50)],
                     [(-150, 100), (-100, 100), (-50, 100), (0, 100),
                      (50, 100), (100, 100), (150, 100)]], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')

        # Test 1- False when move is equal to board position in loop.
        game.move = (-100,-150)
        temp = (game.board[0][1] == game.move)
        self.assertTrue(temp)        

        # Test 2- False when move not equal to board position in loop.
        game.move = (-100,-150)
        self.turn = 'Yellow'
        temp = (game.board[1][3] == game.move)
        self.assertFalse(temp)


    def test_vertical_win(self):

        # Test 1- True when four in a row vertical. First random game
        # Make sure turn in game object below is set to right turn when testing
        game = Game([1, 2, 3], 'Red',
                    [['Red', 'Yellow', 'Yellow', (0, -150), (50, -150),
                      (100, -150), (150, -150)],
                     ['Red', 'Yellow', (-50, -100), (0, -100), (50, -100),
                      (100, -100), (150, -100)],
                     ['Red', (-100, -50), (-50, -50), (0, -50), (50, -50),
                      (100, -50), (150, -50)],
                     ['Red', (-100, 0), (-50, 0), (0, 0), (50, 0),
                      (100, 0), (150, 0)],
                     [(-150, 50), (-100, 50), (-50, 50), (0, 50), (50, 50),
                      (100, 50), (150, 50)],
                     [(-150, 100), (-100, 100), (-50, 100), (0, 100),
                      (50, 100), (100, 100), (150, 100)]], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')
        temp = game.check_vertical_win()
        self.assertTrue(temp)          

        # Test 2- True when four in a row vertical. Second random game
        game = Game([1, 2, 3], 'Yellow',
                    [[(-150, -150), (-100, -150), (-50, -150),
                      (0, -150), 'Red', 'Red', 'Yellow'],
                     [(-150, -100), (-100, -100), (-50, -100),
                      (0, -100), (50, -100), 'Red', 'Yellow'],
                     [(-150, -50), (-100, -50), (-50, -50), (0, -50),
                      (50, -50), 'Yellow', 'Red'],
                     [(-150, 0), (-100, 0), (-50, 0), (0, 0),
                      (50, 0), 'Yellow', 'Red'],
                     [(-150, 50), (-100, 50), (-50, 50), (0, 50),
                      (50, 50), 'Yellow', (150, 50)],
                     [(-150, 100), (-100, 100), (-50, 100), (0, 100),
                      (50, 100), 'Yellow', (150, 100)]], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')
        var = game.check_vertical_win()
        self.assertTrue(var)
        
        # Test 3- True when four in a row vertical. Third random game
        game = Game([1, 2, 3], 'Red',
                    [[(-150, -150), (-100, -150), 'Yellow', 'Red', 'Yellow',
                      (100, -150), (150, -150)],
                     [(-150, -100), (-100, -100), 'Red', 'Yellow',
                      (50, -100), (100, -100), (150, -100)],
                     [(-150, -50), (-100, -50), 'Red', 'Yellow',
                      (50, -50), (100, -50), (150, -50)],
                     [(-150, 0), (-100, 0), 'Red', (0, 0), (50, 0),
                      (100, 0), (150, 0)],
                     [(-150, 50), (-100, 50), 'Red', (0, 50), (50, 50),
                      (100, 50), (150, 50)],
                     [(-150, 100), (-100, 100), (-50, 100), (0, 100),
                      (50, 100), (100, 100), (150, 100)]], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')
        temp = game.check_vertical_win()
        self.assertTrue(temp)
        
        # Test 4- False when only 3 in a row
        game = Game([1, 2, 3], 'Red',
                    [[(-150, -150), 'Red', 'Yellow', (0, -150), (50, -150),
                      (100, -150), (150, -150)],
                     [(-150, -100), 'Red', 'Yellow', (0, -100), (50, -100),
                      (100, -100), (150, -100)],
                     [(-150, -50), (-100, -50), (-50, -50), (0, -50),
                      (50, -50), (100, -50), (150, -50)],
                     [(-150, 0), (-100, 0), (-50, 0), (0, 0), (50, 0),
                      (100, 0), (150, 0)],
                     [(-150, 50), (-100, 50), (-50, 50), (0, 50), (50, 50),
                      (100, 50), (150, 50)],
                     [(-150, 100), (-100, 100), (-50, 100), (0, 100),
                      (50, 100), (100, 100), (150, 100)]], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')
        temp = game.check_vertical_win()
        self.assertFalse(temp)        


    def test_horizontal_win(self):

        # Test 1- True when four in a row horizontal. First random game
        # Make sure turn in game object below is set to right turn when testing
        game = Game([1, 2, 3], 'Red',
                    [['Red', 'Red', 'Red', 'Red', (50, -150), (100, -150),
                      (150, -150)],
                     ['Yellow', 'Yellow', 'Yellow', (0, -100), (50, -100),
                      (100, -100), (150, -100)],
                     [(-150, -50), (-100, -50), (-50, -50), (0, -50),
                      (50, -50), (100, -50), (150, -50)],
                     [(-150, 0), (-100, 0), (-50, 0), (0, 0), (50, 0),
                      (100, 0), (150, 0)],
                     [(-150, 50), (-100, 50), (-50, 50), (0, 50), (50, 50),
                      (100, 50), (150, 50)],
                     [(-150, 100), (-100, 100), (-50, 100), (0, 100),
                      (50, 100), (100, 100), (150, 100)]], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')
        temp = game.check_horizontal_win()
        self.assertTrue(temp)          

        # Test 2- True when four in a row horizontal. Second random game
        game = Game([1, 2, 3], 'Yellow',
                    [[(-150, -150), 'Red', 'Red', 'Yellow', 'Red',
                      'Red', 'Red'],
                     [(-150, -100), 'Red', 'Yellow', 'Red', 'Yellow',
                      'Yellow', (150, -100)],
                     [(-150, -50), 'Red', 'Red', 'Yellow', 'Red', 'Yellow',
                      (150, -50)],
                     [(-150, 0), (-100, 0), 'Yellow', 'Yellow', 'Yellow',
                      'Yellow', (150, 0)],
                     [(-150, 50), (-100, 50), (-50, 50), (0, 50), (50, 50),
                      (100, 50), (150, 50)],
                     [(-150, 100), (-100, 100), (-50, 100), (0, 100),
                      (50, 100), (100, 100), (150, 100)]], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')
        var = game.check_horizontal_win()
        self.assertTrue(var)
        
        # Test 3- True when four in a horizontal. Third random game
        game = Game([1, 2, 3], 'Red',
                    [[(-150, -150), (-100, -150), 'Yellow', 'Yellow',
                      'Red', 'Red', 'Yellow'],
                     [(-150, -100), (-100, -100), 'Yellow', 'Red',
                      'Yellow', 'Yellow', 'Red'],
                     [(-150, -50), (-100, -50), 'Yellow', 'Yellow', 'Red',
                      'Red', 'Yellow'],
                     [(-150, 0), (-100, 0), (-50, 0), 'Red', 'Yellow',
                      'Yellow', 'Red'],
                     [(-150, 50), (-100, 50), (-50, 50), 'Yellow', 'Red',
                      'Red', 'Yellow'],
                     [(-150, 100), (-100, 100), (-50, 100), 'Red', 'Red',
                      'Red', 'Red']], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')
        temp = game.check_horizontal_win()
        self.assertTrue(temp)
        
        # Test 4- False when only 3 in a row
        game = Game([1, 2, 3], 'Red',
                    [['Yellow', 'Yellow', 'Red', 'Red', 'Red', (100, -150),
                      (150, -150)],
                     [(-150, -100), (-100, -100), (-50, -100), (0, -100),
                      (50, -100), (100, -100), (150, -100)],
                     [(-150, -50), (-100, -50), (-50, -50), (0, -50),
                      (50, -50), (100, -50), (150, -50)],
                     [(-150, 0), (-100, 0), (-50, 0), (0, 0), (50, 0),
                      (100, 0), (150, 0)],
                     [(-150, 50), (-100, 50), (-50, 50), (0, 50), (50, 50),
                      (100, 50), (150, 50)],
                     [(-150, 100), (-100, 100), (-50, 100), (0, 100),
                      (50, 100), (100, 100), (150, 100)]], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')
        temp = game.check_horizontal_win()
        self.assertFalse(temp) 


    def test_posdiag_win(self):
        # Test 1- True when four in a row diagonally (pos). First random game
        # Make sure turn in game object below is set to right turn when testing
        game = Game([1, 2, 3], 'Red',
                    [['Red', 'Yellow', 'Yellow', 'Yellow', (50, -150),
                      (100, -150), (150, -150)],
                     ['Yellow', 'Red', 'Red', 'Red', (50, -100),
                      (100, -100), (150, -100)],
                     [(-150, -50), (-100, -50), 'Red', 'Yellow', (50, -50),
                      (100, -50), (150, -50)],
                     [(-150, 0), (-100, 0), (-50, 0), 'Red', (50, 0),
                      (100, 0), (150, 0)],
                     [(-150, 50), (-100, 50), (-50, 50), (0, 50), (50, 50),
                      (100, 50), (150, 50)],
                     [(-150, 100), (-100, 100), (-50, 100), (0, 100),
                      (50, 100), (100, 100), (150, 100)]], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')
        temp = game.check_posdiag_win()
        self.assertTrue(temp)          

        # Test 2- True when four in a row diagonally (pos). Second random game
        game = Game([1, 2, 3], 'Yellow',
                    [['Red', 'Red', 'Yellow', 'Red', 'Red', 'Red',
                      (150, -150)],
                     [(-150, -100), (-100, -100), 'Red', 'Yellow',
                      'Yellow', 'Yellow', (150, -100)],
                     [(-150, -50), (-100, -50), 'Yellow', 'Red', 'Red',
                      'Red', (150, -50)],
                     [(-150, 0), (-100, 0), (-50, 0), 'Yellow', 'Yellow',
                      'Yellow', (150, 0)],
                     [(-150, 50), (-100, 50), (-50, 50), (0, 50), 'Yellow',
                      'Red', (150, 50)],
                     [(-150, 100), (-100, 100), (-50, 100), (0, 100),
                      (50, 100), 'Yellow', (150, 100)]], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')
        var = game.check_posdiag_win()
        self.assertTrue(var)
        
        # Test 3- True when four in a diagonally (pos). Third random game
        game = Game([1, 2, 3], 'Red',
                    [[(-150, -150), (-100, -150), (-50, -150),
                      'Red', 'Yellow', 'Yellow', 'Red'],
                     [(-150, -100), (-100, -100), (-50, -100), (0, -100),
                      'Red', 'Yellow', 'Yellow'],
                     [(-150, -50), (-100, -50), (-50, -50), (0, -50),
                      'Yellow', 'Red', 'Red'],
                     [(-150, 0), (-100, 0), (-50, 0), (0, 0), (50, 0),
                      (100, 0), 'Red'],
                     [(-150, 50), (-100, 50), (-50, 50), (0, 50), (50, 50),
                      (100, 50), (150, 50)],
                     [(-150, 100), (-100, 100), (-50, 100), (0, 100),
                      (50, 100), (100, 100), (150, 100)]], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')
        temp = game.check_posdiag_win()
        self.assertTrue(temp)
        
        # Test 4- False when only 3 in a row
        game = Game([1, 2, 3], 'Red',
                    [[(-150, -150), (-100, -150), (-50, -150), 'Red',
                      'Red', 'Red', 'Yellow'],
                     [(-150, -100), (-100, -100), (-50, -100), 'Yellow',
                      'Yellow', 'Yellow', 'Red'],
                     [(-150, -50), (-100, -50), (-50, -50), 'Red', 'Red',
                      'Red', 'Yellow'],
                     [(-150, 0), (-100, 0), (-50, 0), 'Red', (50, 0),
                      'Yellow', 'Red'],
                     [(-150, 50), (-100, 50), (-50, 50), (0, 50), (50, 50),
                      'Yellow', 'Yellow'],
                     [(-150, 100), (-100, 100), (-50, 100), (0, 100),
                      (50, 100), (100, 100), 'Yellow']], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')
        temp = game.check_posdiag_win()
        self.assertFalse(temp)


    def test_negdiag_win(self):
        # Test 1- True when four in a row diagonally (neg). First random game
        # Make sure turn in game object below is set to right turn when testing
        game = Game([1, 2, 3], 'Red',
                    [['Red', 'Yellow', 'Yellow', 'Yellow', (50, -150),
                      (100, -150), (150, -150)],
                     ['Red', 'Red', 'Yellow', 'Red', (50, -100),
                      (100, -100), (150, -100)],
                     ['Yellow', 'Yellow', 'Red', 'Yellow', (50, -50),
                      (100, -50), (150, -50)],
                     ['Red', 'Red', (-50, 0), (0, 0), (50, 0), (100, 0),
                      (150, 0)],
                     ['Red', (-100, 50), (-50, 50), (0, 50), (50, 50),
                      (100, 50), (150, 50)],
                     [(-150, 100), (-100, 100), (-50, 100), (0, 100),
                      (50, 100), (100, 100), (150, 100)]], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')
        temp = game.check_negdiag_win()
        self.assertTrue(temp)          

        # Test 2- True when four in a row diagonally (neg). Second random game
        game = Game([1, 2, 3], 'Yellow',
                    [[(-150, -150), (-100, -150), (-50, -150),
                      'Red', 'Red', 'Red', 'Yellow'],
                     [(-150, -100), (-100, -100), (-50, -100), 'Yellow',
                      'Yellow', 'Yellow', 'Red'],
                     [(-150, -50), (-100, -50), (-50, -50), 'Red',
                      'Yellow', (100, -50), (150, -50)],
                     [(-150, 0), (-100, 0), (-50, 0), 'Yellow', (50, 0),
                      (100, 0), (150, 0)],
                     [(-150, 50), (-100, 50), (-50, 50), (0, 50), (50, 50),
                      (100, 50), (150, 50)],
                     [(-150, 100), (-100, 100), (-50, 100), (0, 100),
                      (50, 100), (100, 100), (150, 100)]], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')
        var = game.check_negdiag_win()
        self.assertTrue(var)
        
        # Test 3- True when four in a diagonally (neg). Third random game
        game = Game([1, 2, 3], 'Yellow',
                    [[(-150, -150), 'Red', 'Yellow', 'Red', 'Yellow',
                      'Red', (150, -150)],
                     [(-150, -100), (-100, -100), 'Red', 'Red', 'Yellow',
                      'Yellow', (150, -100)],
                     [(-150, -50), (-100, -50), 'Yellow', 'Red', 'Yellow',
                      (100, -50), (150, -50)],
                     [(-150, 0), (-100, 0), 'Red', 'Yellow', (50, 0),
                      (100, 0), (150, 0)],
                     [(-150, 50), (-100, 50), 'Yellow', (0, 50), (50, 50),
                      (100, 50), (150, 50)],
                     [(-150, 100), (-100, 100), (-50, 100), (0, 100),
                      (50, 100), (100, 100), (150, 100)]], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')
        temp = game.check_negdiag_win()
        self.assertTrue(temp)
        
        # Test 4- False when only 3 in a row
        game = Game([1, 2, 3], 'Red',
                    [[(-150, -150), (-100, -150), (-50, -150), (0, -150),
                      'Red', 'Yellow', 'Yellow'],
                     [(-150, -100), (-100, -100), (-50, -100), (0, -100),
                      'Red', 'Yellow', 'Red'],
                     [(-150, -50), (-100, -50), (-50, -50), (0, -50),
                      'Yellow', 'Yellow', 'Red'],
                     [(-150, 0), (-100, 0), (-50, 0), (0, 0), 'Yellow',
                      'Red', (150, 0)],
                     [(-150, 50), (-100, 50), (-50, 50), (0, 50), (50, 50),
                      (100, 50), (150, 50)],
                     [(-150, 100), (-100, 100), (-50, 100), (0, 100),
                      (50, 100), (100, 100), (150, 100)]], 5 , 8,
                    'red_score_test.txt', 'yellow_score_test.txt')
        temp = game.check_negdiag_win()
        self.assertFalse(temp)

        
def main():

    unittest.main()

main()
