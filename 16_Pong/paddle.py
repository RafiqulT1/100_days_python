from turtle import Turtle

class Paddle(Turtle):
    """Create paddle"""
    def __init__(self, x_axes, y_axes):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=None, stretch_len=5, outline=10)
        self.right(90)
        self.penup()
        self.speed(0)
        self.goto(x=x_axes, y=y_axes)

    # movement of the paddle
    def move_up(self):
        """Move the paddle up"""
        new_y_axis = self.ycor() + 20
        self.goto(self.xcor(), new_y_axis)

    def move_down(self):
        """Move the paddle down"""
        new_y_axis = self.ycor() - 20
        self.goto(self.xcor(), new_y_axis)