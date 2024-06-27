import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# Listen to keyboard input
SCREEN.listen()
SCREEN.onkey(player.move_forward, "Up")

GAME_IS_OVER = True
while GAME_IS_OVER:
    time.sleep(0.1) #update the screen after every 1 sec
    SCREEN.update()
    cars.create_car()
    cars.move()

    # Check if player cross the finish line
    if player.cross_finish_line():
        scoreboard.increase_level()
        player.reset_position()
        cars.increase_speed()

    # # increase traffic density depending on the level
    # if scoreboard.level >= 3 and scoreboard.level <= 5:
    #     cars.increase_generation_frequency()
    # elif scoreboard.level >= 7 and scoreboard.level <= 12:
    #     cars.increase_generation_frequency()



    # Detect collision with car
    for car in cars.cars_list:
        if player.distance(car) < 24:
            GAME_IS_OVER = False
            scoreboard.game_over()
    

    

SCREEN.exitonclick()
