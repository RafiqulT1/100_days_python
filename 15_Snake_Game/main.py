from turtle import Screen, Turtle
import time

square_boxes = []
change_x_axis = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

for i in range(3):
    new_squire_box = Turtle(shape="square")
    new_squire_box.color("white")
    new_squire_box.penup()
    new_squire_box.goto(x=0 + change_x_axis, y=0)
    square_boxes.append(new_squire_box)
    change_x_axis -= 20


game_on = True

while game_on:
    screen.update()
    time.sleep(1)
    for box in square_boxes:
        box.forward(10)













screen.exitonclick()




