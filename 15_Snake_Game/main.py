from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake_body = []
# change_x_axes = 0

# Turtle Screen Setup
SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.bgcolor("black")
SCREEN.title("Snake Game")
SCREEN.tracer(100)

# Create snake object
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect food collision with snake head and create new food
    if snake.snake_head.distance(food) < 18:
        food.refresh()
        scoreboard.increase_core()
        snake.add_snake_body()

    # Detect collision with wall.
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -300 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        GAME_ON = False
        scoreboard.game_over()
    
    # Detect snake head collision with body
    for body_part in snake.snake_body[1:]:
        if snake.snake_head.distance(body_part) < 10:
            GAME_ON = False
            scoreboard.game_over()


SCREEN.exitonclick()