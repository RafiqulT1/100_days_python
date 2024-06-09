from turtle import Turtle
# SPEED = 0.2
# angle = 45

class Ball(Turtle):
    """Create ball"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        # self.penup()
        self.speed(0)
        self.goto(x=0, y=0)
        self.go_x_direction = 0.4
        self.go_y_direction = 0.4



    def move(self):
        """Move the ball"""
        new_x = self.xcor() + self.go_x_direction
        new_y = self.ycor() + self.go_y_direction
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.go_y_direction *= -1 

    def paddle_bounce(self):
        self.go_x_direction *= -1 
    # def move(self):
    #     """Move the ball"""
    #     self.setheading(self.angle)
    #     new_x = self.xcor() + SPEED
    #     new_y = self.ycor() + SPEED
    #     self.goto(new_x, new_y)
    

    # def bounce(self):
    #     new_x = (self.xcor()) * -2
    #     new_y = (self.ycor()) * -2
    #     self.goto(new_x, new_y)

    # def change_direction(self):
    #     new_x = self.xcor() - 4
    #     new_y = self.ycor() - 4
    #     self.goto(new_x, new_y)