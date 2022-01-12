from turtle import Screen
from player import Player
from car import CarManager
from scoreboard import Scoreboard
import time

# Setup the screen
screen = Screen()
screen.bgcolor("black")
screen.colormode(255)
screen.setup(width=600, height=600)
screen.title("Don't Squish The Turtle")
screen.tracer(0) # turns off animations

the_turtle = Player()
score_keeper = Scoreboard()
car_manager = CarManager()

# Listen for keystrokes
screen.listen()
screen.onkeypress(the_turtle.move, "Up")

game_in_progress = True
while game_in_progress:
    screen.update()  # to update the screen since animations are turned off
    time.sleep(0.1)

    car_manager.create_car() # Generate a new car
    car_manager.move() # Move all cars across the screen

    # Check if the user passed the level
    if the_turtle.reached_finish_line():
        score_keeper.update_score()
        score_keeper.display_score()
        the_turtle.go_to_start()
        car_manager.increase_speed()

    # Detect collision with a car
    for each_car in car_manager.cars:
        if the_turtle.distance(each_car.pos()) < 30:
            game_in_progress = False
            score_keeper.game_over()

screen.exitonclick()
