import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# Listen to keyboard input
screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    # Check if player cross the finish line
    if player.cross_finish_line():
        scoreboard.increase_level()
        player.reset_position()
        cars.increase_speed()

    # Detect collision with car
    for car in cars.cars_list:
        if player.distance(car) < 22:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
