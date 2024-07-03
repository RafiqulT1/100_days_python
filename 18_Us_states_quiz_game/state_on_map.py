from turtle import Turtle
from read_csv import df

class StatePlacement(Turtle):
    "create turtle object for placing state name on map"
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.hideturtle()
        self.penup()

    def to_x_y_pos(self, guessed):
        "place guessed state on map according to x & y axis"
        guessed_state_data = df[df.state == guessed]
        self.goto(int(guessed_state_data.x), int(guessed_state_data.y))
        self.write(guessed)