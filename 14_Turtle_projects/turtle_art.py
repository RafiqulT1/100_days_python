from turtle import Screen, Turtle
import random

t = Turtle()
screen = Screen()

t.speed(0)
screen.colormode(255)

def random_Color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

t.penup()
t.hideturtle()
t.setheading(-225)
t.forward(300)
t.setheading(0)

for loop in range(0, 10):
    for _ in range(0, 10):
        t.color(random_Color())
        t.dot(20)
        t.forward(50)
    t.setheading(0)
    t.right(90)
    t.forward(50)
    if loop%2 == 0:
        t.right(90)
    else:
        t.left(90)
    t.forward(50)


screen.exitonclick()