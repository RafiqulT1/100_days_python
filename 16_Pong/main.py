from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

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
# Crate scoreboard
left_paddle_board = Scoreboard(-100, 200)
right_paddle_board = Scoreboard(100, 200)

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
        ball.wall_bounce()

    if ball.xcor() > 325 and ball.distance(right_paddle) < 55:
        ball.color("blue")
        ball.paddle_bounce()  
    elif ball.xcor() < -325 and ball.distance(left_paddle) < 55:
        ball.color("red")
        ball.paddle_bounce()

    if ball.xcor() > 375:
        ball.reset_ball_position()
        left_paddle_board.increase_point()

    if ball.xcor() < -375:
        ball.reset_ball_position()
        right_paddle_board.increase_point()

SCREEN.exitonclick()
