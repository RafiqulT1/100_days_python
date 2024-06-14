from turtle import Turtle, Screen


tim = Turtle()


def draw_shape(num_sides):
    angle = 360 / num_sides
    
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
















screen = Screen()
screen.exitonclick()