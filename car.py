from turtle import Turtle
from random import choice, randint

# Values that can be changed with preference
COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
MOVE_DIST = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = MOVE_DIST

    # Creates a new car to move across the screen
    def create_car(self):
        if randint(1, 5) == 5: # Essentially spawns a new car 1 in every 5 iterations of the while loop in main.py
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.seth(180)
            new_car.pu()
            new_car.goto(315, randint(-240, 240))
            self.cars.append(new_car)

    # Moves all the cars across the screen
    def move(self):
        for car in self.cars:
            car.fd(self.speed)

    # Increases the speed after every level
    def increase_speed(self):
        self.speed += MOVE_INCREMENT
