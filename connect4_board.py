
#Connect Four class Board


import turtle
import random

class Board:
    ''' class Board
        Attributes: x, y, red_scorefile, yellow_scorefile
        Methods: creat_sq, create_grid, create_arrows, first_turn,
                games_won_display, make_tracker_board, initialize_red_score,
                initialize_yellow_score
    '''
    
    def __init__(self, X_COORDINATES, Y_COORDINATES, RED_FILE, YELLOW_FILE):
        '''
        Constructor - creates an new instance of a Board
        Parameters:
           self- the current object
           X_COORDINATES - x-axis coordinates of the columns of the game (list)
           Y_COORDINATES - y-axis coordinates of the rows of the game (list)
           RED_FILE - txt file where integer of red wins is kept (string) 
           YELLOW_FILE - txt file where integer of yellow wins is kept (string)              
        ''' 
        self.x = X_COORDINATES
        self.y = Y_COORDINATES
        self.red_scorefile = RED_FILE
        self.yellow_scorefile = YELLOW_FILE

    def create_sq(self):
        '''
        Method - draws that blue square of the grid, behind the circles
        Parameters:
           self - the current object
        Returns nothing. 
        '''         
        blue_sq = turtle.Turtle()
        blue_sq.hideturtle()
        blue_sq.penup()
        blue_sq.speed(0)
        blue_sq.fillcolor('blue')
        blue_sq.begin_fill()
        blue_sq.forward(175)
        blue_sq.right(90)
        blue_sq.forward(160)
        blue_sq.right(90)
        blue_sq.forward(350)
        blue_sq.right(90)
        blue_sq.forward(310)
        blue_sq.right(90)
        blue_sq.forward(350)
        blue_sq.right(90)
        blue_sq.forward(150)
        blue_sq.end_fill()

    def create_grid(self):
        '''
        Method - uses nested loop of the x and y coordinates to draw
                circles grid, in front of blue square
        Parameters:
           self - the current object
        Returns nothing. 
        '''           
        grid_circles = turtle.Turtle()
        grid_circles.hideturtle()
        grid_circles.pencolor('white')
        for y in self.y:
            for x in self.x:
                grid_circles.penup()
                grid_circles.speed(0)
                grid_circles.setposition(x, y)
                grid_circles.fillcolor('white')
                grid_circles.begin_fill()
                grid_circles.circle(20)
                grid_circles.end_fill()
    
    def create_arrows(self):
        '''
        Method - creates arrrows at the x-axis of the columns
        Parameters:
           self - the current object
        Returns nothing. 
        '''          
        for x in self.x:
            arrow = turtle.Turtle()
            arrow.shape('arrow')
            arrow.color('white')
            arrow.penup()
            arrow.speed(0)
            arrow.setposition(x, 170)
            arrow.right(90)

    def first_turn(self):
        '''
        Method - randomly picks who gets to go first
        Parameters:
           self - the current object
        Returns player who gets to go first (string)
        '''          
        integer = random.randint(1,2)
        if integer == 1:
            player_one = 'Red'
        else:
            player_one = 'Yellow'

        return player_one

    def games_won_display(self):
        '''
        Method - Shows the number of games won for each player above the grid
        Parameters:
           self - the current object
        Returns nothing
        '''         
        games_won_display = turtle.Turtle()
        games_won_display.hideturtle()
        games_won_display.speed(0)
        games_won_display.penup()
        games_won_display.goto(-100,200)
        games_won_display.color('white')
        games_won_display.write('Games won:', align = 'center',
                               font = ('Arial', 16,'bold'))
        games_won_display.goto(0,200)
        games_won_display.color('red')
        games_won_display.write('Red-', align = 'center',
                               font = ('Arial', 16,'bold'))
        games_won_display.goto(50,200)
        games_won_display.color('white')
        games_won_display.write(str(self.r_score), align = 'center',
                          font = ('Arial', 16,'bold'))
        games_won_display.goto(115,200)
        games_won_display.color('yellow')
        games_won_display.write('Yellow-', align = 'center',
                               font = ('Arial', 16,'bold'))
        games_won_display.goto(175,200)
        games_won_display.color('white')
        games_won_display.write(str(self.y_score), align = 'center',
                          font = ('Arial', 16,'bold'))


    def make_tracker_board(self):
        '''
        Method - Takes the x axis coordinates and the y axis coordinates and
                combine them through nested loop to create all the coordinates
                of the game board (list). Then takes that list of coordiantes
                and divides it after every 7 coordinates to split the
                coordinates up into the 7 columns and 6 rows of the board. We'll
                use this board the track all of the moves being done on turtle
                grid, behind the scenes
        Parameters:
           self - the current object
        Returns nested list of the coordinates broken out the represent board
        ''' 
        board_coords = []
        tracker_board = []

        for i in range(len(self.y)):
            for j in range(len(self.x)):
                board_coords.append((self.x[j], self.y[i]))

        i = 0
        while i < len(board_coords):
            tracker_board.append(board_coords[i:i+7])
            i+=7

        return tracker_board

    def initialize_red_score(self):
        '''
        Method - reads red score file & initializes red's amount of games won.
                r_score is sent to 'games_won _display' to draw score
                on the turtle screen.
        Parameters:
           self - the current object
        Returns the number of games that red had won (int). Will use it for the
                game class as well
        '''         
        try:
            with open(self.red_scorefile, 'r') as infile:
                self.r_score = int(infile.read())
                return self.r_score
        except OSError:
            self.r_score = 0
            return self.r_score

    def initialize_yellow_score(self):
        '''
        Method - reads yellow score file & initializes yellow's amount of
                games won. y_score is sent to 'games_won _display' to draw score
                on the turtle screen.
        Parameters:
           self - the current object
        Returns the number of games that yellow had won (int). Will use it for
                the game class as well
        '''          
        try:
            with open(self.yellow_scorefile, 'r') as infile:
                self.y_score = int(infile.read())
                return self.y_score
        except OSError:
            self.y_score = 0
            return self.y_score
    
