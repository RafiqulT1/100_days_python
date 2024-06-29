from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_POSITION = (310, 0) # car get created in this position
STARTING_MOVE_DISTANCE = 5 # starting car speed
MOVE_INCREMENT = 3 # car speed increase by 3
TRAFFIC_DENSITY = 6 #NOTE:decrease the int to increase traffic density

class CarManager():
    """Generate cars randomly"""
    def __init__(self):
        self.cars_list = []
        self.cars_speed = STARTING_MOVE_DISTANCE
        self.car_gen_freq = TRAFFIC_DENSITY

    def create_car(self):
        "create car object and append to cars list"
        random_chance = random.randint(1, TRAFFIC_DENSITY)
        if random_chance == 6: #reduce the car generation frequency
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.turtlesize(stretch_wid=None, stretch_len=2, outline=0)
            new_car.penup()
            new_car.goto(310, random.randint(-250, 290))
            self.cars_list.append(new_car)

    def move(self):
        """Move cars forward"""
        for car in self.cars_list:
            new_x_axis = car.xcor() - self.cars_speed
            car.goto(new_x_axis, car.ycor())

    def increase_speed(self):
        """Increase car speed"""
        self.cars_speed += MOVE_INCREMENT





### for future improvement ###
        # self.increase_generation_frequency()
        # self.remove_car()

    # def increase_generation_frequency(self):
    #     """Increase car generation frequency"""
    #     if self.car_gen_freq == 1:
    #         pass

    #     self.car_gen_freq -= 1
    #     print(f"car freq: {self.car_gen_freq}")

    # def remove_car(self):
    #     if len(self.cars_list) > 30:
    #         for i in self.cars_list:
    #             self.cars_list.pop(i)
