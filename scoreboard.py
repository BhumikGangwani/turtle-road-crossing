from turtle import Turtle

# Value that can be changed with preference
FONT = ("Arial", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.ht()
        self.pu()
        self.goto(x=-295, y=260)
        self.display_score()

    # Increases the level by 1
    def update_score(self):
        self.level += 1

    # Displays the current level of the game
    def display_score(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT, align="left")

    # Displays the Game Over text
    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", font=FONT, align="center")
