from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    "Show score on the game window and and let user know when the game is over"
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("Black")
        self.penup()
        self.goto(-280, 270)
        self.hideturtle()
        self.increase_level()

    def increase_level(self):
        """Show on game level on the game window"""
        self.clear()
        self.write(f"Level: {self.level}",  move=False, align=ALIGNMENT, font=FONT)
        self.level += 1

    def game_over(self):
        """Show game over text on the screen"""
        self.goto(-70, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
