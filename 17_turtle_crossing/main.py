import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen to keyboard input
SCREEN.listen()
SCREEN.onkey(player.move_forward, "Up")

GAME_IS_OVER = True
while GAME_IS_OVER:
    time.sleep(0.1) #update the screen after every 1 sec
    SCREEN.update()
    car_manager.create_car()
    car_manager.move()

    # Check if player cross the finish line
    if player.cross_finish_line():
        scoreboard.increase_level()
        player.reset_position()
        car_manager.increase_speed()

    # Detect collision with car
    for car in car_manager.cars_list:
        if player.distance(car) < 24:
            GAME_IS_OVER = False
            scoreboard.game_over()


SCREEN.exitonclick()
