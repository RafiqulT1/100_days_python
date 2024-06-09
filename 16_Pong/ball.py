from turtle import Turtle
# angle = 45

class Ball(Turtle):
    """Create ball"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(x=0, y=0)
        self.go_x_direction = 0.15
        self.go_y_direction = 0.15

    def move_ball(self):
        """Move the ball"""
        new_x = self.xcor() + self.go_x_direction
        new_y = self.ycor() + self.go_y_direction
        self.goto(new_x, new_y)

    def wall_bounce(self):
        """Bounce from wall. When ball hit the wall,
        we reverse the Y axes direction but multiplying -1 """
        self.go_y_direction *= -1

    def paddle_bounce(self):
        """Bounce from paddle. When ball hit the paddle,
        we reverse the x axes direction but multiplying -1"""
        self.go_x_direction *= -1
        self.go_x_direction += 0.002
        self.go_y_direction += 0.002

    def reset_ball_position(self):
        """Reset ball position to (0,0) and
        alternately ball changes its starting direction"""
        self.goto(x=0, y=0)
        self.go_x_direction *= -1
        self.go_x_direction = 0.15
        self.go_y_direction = 0.15
    