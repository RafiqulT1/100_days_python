from turtle import Screen, Turtle
import random

color_list = [
    "black", "blue", "brown", "cyan", "darkblue", "darkcyan", "darkgreen",
    "darkgrey", "darkmagenta", "darkorange", "darkred", "darksalmon",
    "darkviolet", "green", "grey", "indigo", "maroon", "mediumblue",
    "mediumorchid", "mediumpurple", "midnightblue", "navy", "olive",
    "orange", "orangered", "purple", "red", "saddlebrown", "seagreen",
    "sienna", "slategrey", "teal", "tomato", "violet"
]

# creating turtle object
tim = Turtle()
tim.shape("turtle")
tim.speed(0)
tim.pensize(15)
# tim.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

for _ in range(300):
    tim.color(random.choice(color_list))
    tim.forward(40)
    tim.setheading(90 * random.randint(1,4)) 

screen = Screen()
screen.exitonclick()


# number_sides = 10

# def draw(number_sides):
#     angle = 360 / number_sides
#     for _ in range(number_sides):
#         tim.forward(100)
#         tim.right(angle)

# for number_sides in range(3, 11):
#     draw(number_sides)

# screen = Screen()
# screen.exitonclick()