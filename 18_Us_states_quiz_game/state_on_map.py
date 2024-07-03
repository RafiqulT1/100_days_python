from turtle import Turtle
from read_csv import df

class StatePlacement(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.hideturtle()
        self.penup()

    def to_x_y_pos(self, guessed):
        guessed_state_data = df[df.state == guessed]
        # print(guessed_state_data)
        # print(f"{guessed_state_data.x}, {guessed_state_data.y}")
        self.goto(int(guessed_state_data.x), int(guessed_state_data.y))
        self.write(guessed)