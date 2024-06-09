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
    ball.move_ball()

    # Detect ball collision with wall
    if ball.ycor() >= 286 or ball.ycor() <= -286:
        ball.color("red")
        ball.wall_bounce()

    if ball.xcor() > 325 and ball.distance(right_paddle) < 55 or ball.xcor() < -325 and ball.distance(left_paddle) < 55:
        ball.color("blue")
        ball.paddle_bounce()

    if ball.xcor() > 375:
    # and not ball.distance(right_paddle) < 55 or ball.xcor() < -325 and not ball.distance(left_paddle) < 55:
        # print("right paddle lost")
        # game_on = False
        ball.reset_ball_position(120)
    if ball.xcor() < -375:
        # print("left paddle lost")
        ball.reset_ball_position(120)
        # game_on = False

    # or ball.xcor() <= -325:
        # ball.paddle_bounce()

SCREEN.exitonclick()
