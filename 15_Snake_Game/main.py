from turtle import Screen
from snake import Snake
import time

snake_body = []
# change_x_axes = 0

# Turtle Screen Setup
SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.bgcolor("black")
SCREEN.title("Snake Game")
SCREEN.tracer(0)

# Create snake object
snake = Snake()

SCREEN.listen()
SCREEN.onkey(snake.up, "Up")
SCREEN.onkey(snake.down, "Down")
SCREEN.onkey(snake.left, "Left")
SCREEN.onkey(snake.right, "Right")


GAME_ON = True

# snake.create_snake_body()
while GAME_ON:
    SCREEN.update()
    time.sleep(0.1)
    snake.move()


SCREEN.exitonclick()