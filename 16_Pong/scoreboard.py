from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, x_axes_pos, y_axes_pos):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.player_score = 0
        # self.right_score = 0
        self.goto(x_axes_pos, y_axes_pos)
        self.increase_point()
        
    
    def increase_point(self):
        self.clear()
        self.write(self.player_score, align="center", font=("arial", 60))
        self.player_score += 1