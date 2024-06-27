import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle_player = Player()
cars = CarManager()

# Listen to keyboard input
screen.listen()
screen.onkey(turtle_player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()

    # Detect collision with car
    for car in cars.cars_list:
        if turtle_player.distance(car) < 30:
            game_is_on = False

    # Check if player cross the finish line
    
