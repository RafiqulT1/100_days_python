from turtle import Turtle, Screen
import random

is_race_on = False 
screen = Screen() #create screen object from Screen() class 
screen.setup(width=500, height=400) #set window size
#ask for user input
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"] # color list
colored_turtles = [] #list to hold turtle objects
change_y_axis = 0

# loop to create turle objects based on color name
for color in colors:
    turtle_name = color
    print(turtle_name)
    turtle_name = Turtle(shape="turtle")
    turtle_name.color(color)
    turtle_name.penup()
    #place turtles side by side
    turtle_name.goto(x=-230, y=-110 + change_y_axis) 
    colored_turtles.append(turtle_name)
    change_y_axis += 50

#race starts if user has chosen the turtle color
if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in colored_turtles:
        if turtle.xcor() > 215: #finnish line of the race
            is_race_on = False 
            winner = turtle.pencolor()
            #let user know if their turle won / lost this race
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")

        # turtle goes forward randomly
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

# window close when clicked 
screen.exitonclick()









# def move_forwards():
#     tim.forward(10)
# def move_backword():
#     tim.backward(10)

# def turn_right():
#     tim.right(5)
# def turn_left():
#     tim.left(5)
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()


# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="s", fun=move_backword)
# screen.onkey(key="c", fun=clear_screen)