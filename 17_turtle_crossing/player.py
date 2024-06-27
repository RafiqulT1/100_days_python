from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Create Turtle Player"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.right(-90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_forward(self):
        """Move turtle player forward"""
        new_y_axis = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y_axis)

    def cross_finish_line(self):
        """Check if the turtle player have reached the finish line"""
        return self.ycor() == FINISH_LINE_Y
    
    def reset_position(self):
        """Reset player position"""
        self.goto(STARTING_POSITION)

