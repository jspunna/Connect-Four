
#Connect Four class Game

import turtle

ARROW_LOWY = 158
ARROW_HIGHY = 180

class Game:
    ''' class Game
        Attributes: y_coords, turn, board, r_score, y_score, red_scorefile,
                    yellow_scorefile, circles_taken, move, xclick, yclick,
                    turn_display
        Methods: show_turn, clear_turn, click, get_clicked_column,
                is_valid_move, make_token, change_turn, store_moves_board,
                check_vertical_win, check_horizontal_win, check_posdiag_win,
                check_negdiag_win, add_point, write_score,
                create_end_background, show_winner, show_tie
    '''
    
    def __init__(self, Y_COORDINATES, turn, tracker_board,
                 r_score, y_score, RED_FILE, YELLOW_FILE):
        '''
        Constructor - creates an new instance of a Game
        Parameters:
           self- the current object
           Y_COORDINATES - y-axis coordinates of the rows of the game (list)
           turn - turn of player. Red or Yellow (string)
           tracker_board - board that keeps track of all coordinates and moves
                           made by players. Basically the turtle board, behind
                           the scenes (list)
           r_score - keeps track of the number of times that red won game (int)
           y_score - keeps track of number of times that yellow won game (int)
           RED_FILE - txt file where integer of red wins is kept (string) 
           YELLOW_FILE - txt file where integer of yellow wins is kept (string)              
        '''  
        self.y_coords = Y_COORDINATES
        self.turn = turn
        self.board = tracker_board
        self.r_score = r_score
        self.y_score = y_score
        self.red_scorefile = RED_FILE
        self.yellow_scorefile = YELLOW_FILE
        self.circles_taken = []        
        self.move = 0        
        self.xclick = 0
        self.yclick = 0
        self.turn_display = turtle.Turtle()

    def show_turn(self, turn):
        '''
        Method - shows the turn of the player in the beginning and after move
        Parameters:
           self - the current object
           turn - turn of the player
        Returns nothing. Uses turtle to draw a circles of the next turn
        '''  
        self.turn_display.hideturtle()
        self.turn_display.speed(0)
        self.turn_display.penup()
        self.turn_display.goto(-400,100)
        self.turn_display.color('white')
        self.turn_display.write(str(self.turn), align = 'center',
                           font = ('Arial', 18,'bold'))
        self.turn_display.goto(-400,65)
        self.turn_display.write("It's your turn!", align = 'center',
                                font = ('Arial', 16,'bold'))
        self.turn_display.goto(-400,15)
        if self.turn == 'Red':
            self.turn_display.hideturtle()
            self.turn_display.fillcolor('red')
            self.turn_display.begin_fill()
            self.turn_display.circle(20)
            self.turn_display.end_fill()
        elif self.turn == 'Yellow':
            self.turn_display.hideturtle()
            self.turn_display.fillcolor('yellow')
            self.turn_display.begin_fill()
            self.turn_display.circle(20)
            self.turn_display.end_fill()
        else:
            self.turn_display.hideturtle()
            self.turn_display.fillcolor('White')
            self.turn_display.begin_fill()
            self.turn_display.circle(20)
            self.turn_display.end_fill()            

    def clear_turn(self):
        '''
        Method - clears current turn display after a move,
                in preparation to show next turn
        Parameters:
           self - the current object
        Returns nothing
        '''         
        self.turn_display.clear()        
    
    def click(self, x, y):
        '''
        Method - takes x and y coordinates of click and then proceeds to call
                functions that play the rest of the game
        Parameters:
           self - the current object
           x - x coordinate of the click
           y - y coordinate of the click
        Returns nothing. Executes other functions of the game on click
        '''          
        self.xclick = x
        self.yclick = y
        col = self.get_clicked_column()
        valid_move = self.is_valid_move(col)
        if valid_move == True:
            self.store_moves_board()
            vert = self.check_vertical_win()
            horz = self.check_horizontal_win()
            pdiag = self.check_posdiag_win()
            ndiag = self.check_negdiag_win()
            if (vert == True or horz == True or pdiag == True or ndiag == True):
                self.add_point()
                self.write_score()
                self.create_end_background()
                self.show_winner()
                self.turn = 'White'
            if (len(self.circles_taken) == 42 and vert == False and
                horz == False and pdiag == False and ndiag == False):
                self.create_end_background()
                self.show_tie()
                self.turn = 'White'
            self.change_turn()
            self.clear_turn()
            self.show_turn(self.turn)

    def get_clicked_column(self):
        '''
        Method - When players clicks an arrow, based of the the x and y
                coordinates of that click, gets the column axis in order to know
                which column the player wants to drop the token into
        Parameters:
           self - the current object
        Returns x-axis of the choosen column
        '''         
        if (self.xclick > -162 and self.xclick < -140
            and self.yclick < ARROW_HIGHY and self.yclick > ARROW_LOWY):
            clicked_column = -150
            return clicked_column
        elif (self.xclick > -112 and self.xclick < -89
              and ARROW_HIGHY > self.yclick > ARROW_LOWY):
            clicked_column = -100
            return clicked_column
        elif (self.xclick > -63 and self.xclick < -40
            and self.yclick < ARROW_HIGHY and self.yclick > ARROW_LOWY):
            clicked_column = -50
            return clicked_column
        elif (self.xclick > -11 and self.xclick < 11
            and self.yclick < ARROW_HIGHY and self.yclick > ARROW_LOWY):
            clicked_column = 0
            return clicked_column
        elif (self.xclick > 31 and self.xclick < 60
            and self.yclick < ARROW_HIGHY and self.yclick > ARROW_LOWY):
            clicked_column = 50
            return clicked_column
        elif (self.xclick > 88 and self.xclick < 110
            and self.yclick < ARROW_HIGHY and self.yclick > ARROW_LOWY):
            clicked_column = 100
            return clicked_column
        elif (self.xclick > 139 and self.xclick < 162
            and self.yclick < ARROW_HIGHY and self.yclick > ARROW_LOWY):
            clicked_column = 150
            return clicked_column

    def is_valid_move(self, col):
        '''
        Method - Once x-axis of the chosen column is stored, we need to find the
                next available row in the column. Once the next row in the
                y_coords is found, together they make up the coordinates of
                that move. Added it to self.move and list of circles_taken
                or positions on the board taken
        Parameters:
           self - the current object
           col - x-axis of the column chosen
        Returns True or False. If the next move in the column is available, then
                the move is valid. If not, it does nothing
        '''  
        for row in self.y_coords:
            if (col, row) not in self.circles_taken:
                if col == None:
                    return False
                else:
                    self.circles_taken.append((col, row))
                    self.move = ((col, row))
                    self.make_token(col, row)
                    return True
            
    def make_token(self, col, row):
        '''
        Method - Makes a token at the column & row coordinates of current move
        Parameters:
           self - the current object
           col - x-axis of the column chosen
           row - y-axis of the row 
        Returns nothing. Draws token at the coordinates of desired move
        '''         
        token = turtle.Turtle()
        token.speed(0)
        token.hideturtle()
        token.penup()
        token.setposition(col, row)
        token.fillcolor(self.turn)
        token.begin_fill()
        token.circle(20)
        token.end_fill()
        
    def change_turn(self):
        '''
        Method - Changes the turn of a player once current move ends
        Parameters:
           self - the current object
        Returns nothing. Change turn attribute to next player's color
        ''' 
        if self.turn == 'Red':
            self.turn = 'Yellow'
        elif self.turn == 'Yellow':
            self.turn = 'Red'
        else:
            self.turn = 'White'

    def store_moves_board(self):
        '''
        Method - Stores all of the moves made in a board. Through the nested
                loop, if the coordinate in the board is equal to a move that
                the player made, then changes that coordiate to the color of
                the player
        Parameters:
           self - the current object
        Returns nothing. Tracks moves of the players
        ''' 
        for i in range(len(self.board)):
            for j in range(len(self.board)+1):   
                if self.move == self.board[i][j]:
                      self.board[i][j] = self.turn
        
    def check_vertical_win(self):
        '''
        Method - Checks to see if there is a four in a row, vertically 
        Parameters:
           self - the current object
        Returns True if there is a four in a row vertically
        '''
        for i in range(len(self.board)-3):
            for j in range(len(self.board)+1):
                if (self.board[i][j] == self.turn
                    and self.board[i+1][j] == self.turn
                    and self.board[i+2][j] == self.turn
                    and self.board[i+3][j] == self.turn):
                    return True
        return False

    def check_horizontal_win(self):
        '''
        Method - Checks to see if there is a four in a row, horizontally 
        Parameters:
           self - the current object
        Returns True if there is a four in a row horizontally
        '''        
        for i in range(len(self.board)):
            for j in range(len(self.board)-2):
                if (self.board[i][j] == self.turn
                    and self.board[i][j+1] == self.turn
                    and self.board[i][j+2] == self.turn
                    and self.board[i][j+3] == self.turn):
                    return True
        return False
                
    def check_posdiag_win(self):
        '''
        Method - Checks to see if there is a four in a row when there is a
                positive sloped diagonal
        Parameters:
           self - the current object
        Returns True if there is a four in a row on a positiive sloped diagonal
        '''         
        for i in range(len(self.board)-3):
            for j in range(len(self.board)-2):
                if (self.board[i][j] == self.turn
                    and self.board[i+1][j+1] == self.turn
                    and self.board[i+2][j+2] == self.turn
                    and self.board[i+3][j+3] == self.turn):
                    return True
        return False
                
    def check_negdiag_win(self):
        '''
        Method - Checks to see if there is a four in a row when there is a
                negative sloped diagonal
        Parameters:
           self - the current object
        Returns True if there is a four in a row on a negative sloped diagonal
        '''          
        for i in range(len(self.board)-3):
            for j in range(3, (len(self.board)+1)):
                if (self.board[i][j] == self.turn
                    and self.board[i+1][j-1] == self.turn
                    and self.board[i+2][j-2] == self.turn
                    and self.board[i+3][j-3] == self.turn):
                    return True
        return False

    def add_point(self):
        '''
        Method - Adds point to score attribute of the winner
        Parameters:
           self - the current object
        Returns nothing
        ''' 
        if self.turn == 'Red':
            self.r_score += 1
        else:
            self.y_score += 1

    def write_score(self):
        '''
        Method - updates score file with most recent score of winner
        Parameters:
           self - the current object
        Returns nothing
        '''         
        try:
            if self.turn == 'Red':
                with open(self.red_scorefile, 'w') as outfile:
                    outfile.write(str(self.r_score))
            elif self.turn == 'Yellow':
                with open(self.yellow_scorefile, 'w') as outfile:
                    outfile.write(str(self.y_score))                
        except OSError:
            print('Oh No, we were not able to update your score')

    def create_end_background(self):
        '''
        Method - if there is a draw or winner, changes the background to white
        Parameters:
           self - the current object
        Returns nothing
        '''          
        end_background = turtle.Turtle()
        end_background.hideturtle()
        end_background.penup()
        end_background.speed(0)
        end_background.goto(-650,500)
        end_background.fillcolor('white')
        end_background.begin_fill()
        end_background.forward(1200)
        end_background.right(90)
        end_background.forward(800)
        end_background.right(90)
        end_background.forward(1200)
        end_background.right(90)
        end_background.forward(800)
        end_background.end_fill()

    def show_winner(self):
        '''
        Method - if there is a winner, shows message of who won the game
        Parameters:
           self - the current object
        Returns nothing
        '''           
        show_winner = turtle.Turtle()
        show_winner.hideturtle()
        show_winner.penup()        
        show_winner.goto(0,0)
        show_winner.color('black')
        show_winner.write('We have a winner! Congrats to ..........',
                          align = 'center', font = ('Arial', 30,'bold'))
        show_winner.goto(0,-50)
        show_winner.color(self.turn)
        show_winner.write(str(self.turn), align = 'center',
                          font = ('Arial', 30,'bold'))

    def show_tie(self):
        '''
        Method - if there is a tie, shows message that there was a tie
        Parameters:
           self - the current object
        Returns nothing
        '''           
        show_tie = turtle.Turtle()
        show_tie.hideturtle()
        show_tie.penup()        
        show_tie.goto(0,0)
        show_tie.color('black')
        show_tie.write('Game Over. Tough battle results in a tie',
                        align = 'center', font = ('Arial', 30,'bold'))       
