from turtle import Screen
from paddle import Paddle

# Screen settings
SCREEN = Screen()
SCREEN.title("PONG")
SCREEN.setup(width=800, height=600)
SCREEN.bgcolor("black")
SCREEN.tracer(0)

# Create left and right paddle
right_paddle = Paddle(x_axes=350, y_axes=0)
left_paddle = Paddle(x_axes=-350, y_axes=0)

# listening to keyboard input for left_paddle & right_paddle movement
SCREEN.listen()
SCREEN.onkey(right_paddle.move_up, "Up")
SCREEN.onkey(right_paddle.move_down, "Down")
SCREEN.onkey(left_paddle.move_up, "w")
SCREEN.onkey(left_paddle.move_down, "s")

game_on = True

while game_on:
    SCREEN.update()

SCREEN.exitonclick()
