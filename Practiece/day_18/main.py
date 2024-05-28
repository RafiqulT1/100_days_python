from turtle import Screen, Turtle

# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")

# for _e in range(4):
#     tim.forward(100)
#     tim.left(90)





# screen = Screen()
# screen.exitonclick()


tim = Turtle()
number_sides = 10

def draw(number_sides):
    angle = 360 / number_sides
    for _ in range(number_sides):
        tim.forward(100)
        tim.right(angle)

for number_sides in range(3, 11):
    draw(number_sides)

screen = Screen()
screen.exitonclick()