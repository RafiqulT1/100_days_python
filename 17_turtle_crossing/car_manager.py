from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_POSITION = (310, 0)
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_GENERATOR_FREQUENCY = 6


class CarManager():
    """Generate cars randomly"""
    def __init__(self):
        self.cars = []

    def create_car(self):
        "create car object and append to cars list"
        if random.randint(1, CAR_GENERATOR_FREQUENCY) == 6:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.turtlesize(stretch_wid=None, stretch_len=2, outline=0)
            new_car.penup()
            new_car.goto(310, random.randint(-250, 290))
            self.cars.append(new_car)

    def move(self):
        """Move cars forward"""
        for car in self.cars:
            new_x_axis = car.xcor() - STARTING_MOVE_DISTANCE
            car.goto(new_x_axis, car.ycor())

