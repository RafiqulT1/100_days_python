from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    """Generate cars randomly"""
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.turtlesize(stretch_wid=None, stretch_len=2, outline=0)

    def move_car(self):
        """Move cars forward"""
        # new_x_axis = self.xcor

