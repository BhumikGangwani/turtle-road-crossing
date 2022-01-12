from turtle import Turtle

# Constant values for the game
STARTING_POS = (0, -280)
MOVE_DIST = 10
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color((9, 96, 0))
        self.seth(90)
        self.pu()
        self.go_to_start()

    # Positions the turtle at the starting point
    def go_to_start(self):
        self.goto(STARTING_POS)

    # Moves the turtle forward with every keypress
    def move(self):
        self.fd(MOVE_DIST)

    # Checks if the user has completed the current level
    def reached_finish_line(self):
        return self.ycor() == FINISH_LINE