from turtle import Screen
from turtle import Turtle

SCREEN = Screen()
SCREEN.title("PONG")
SCREEN.setup(width=800, height=600)
SCREEN.bgcolor("black")
SCREEN.tracer(0)


new_paddle = Turtle(shape="square")
new_paddle.turtlesize(stretch_wid=None, stretch_len=5, outline=10)
new_paddle.right(90)
new_paddle.color("white")
new_paddle.penup()
new_paddle.speed(0)
new_paddle.goto(x=350, y=0)

def move_up():
    new_y_axis = new_paddle.ycor() + 20
    new_paddle.goto(new_paddle.xcor(), new_y_axis)
def move_down():
    new_y_axis = new_paddle.ycor() - 20
    new_paddle.goto(new_paddle.xcor(), new_y_axis)

SCREEN.listen()
SCREEN.onkey(move_up, "Up")
SCREEN.onkey(move_down, "Down")

game_on = True

while game_on:
    SCREEN.update()

SCREEN.exitonclick()
