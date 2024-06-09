from turtle import Screen
from paddle import Paddle
from ball import Ball

# Screen settings
SCREEN = Screen()
SCREEN.title("PONG")
SCREEN.setup(width=800, height=600)
SCREEN.bgcolor("black")
SCREEN.tracer(0)

# Create left and right paddle
right_paddle = Paddle(x_axes=350, y_axes=0)
left_paddle = Paddle(x_axes=-350, y_axes=0)

# Create ball
ball = Ball()

# listening to keyboard input for left_paddle & right_paddle movement
SCREEN.listen()
SCREEN.onkey(right_paddle.move_up, "Up")
SCREEN.onkey(right_paddle.move_down, "Down")
SCREEN.onkey(left_paddle.move_up, "w")
SCREEN.onkey(left_paddle.move_down, "s")

game_on = True

while game_on:
    SCREEN.update()
    ball.move()

    # Detect ball collision with wall
    if ball.ycor() >= 286 or ball.ycor() <= -286:
        ball.color("red")
        ball.wall_bounce()
    elif ball.xcor() >= 325 or ball.xcor() <= -325:
        ball.color("blue")
        ball.paddle_bounce()

        # ball.move(-0.4)
        # ball.bounce()

        # ball.change_direction()

SCREEN.exitonclick()
