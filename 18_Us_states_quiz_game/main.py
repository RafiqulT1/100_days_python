#import turtle & pandas
import turtle
import pandas

# adding data form 50_states.csv file to pandas data frame
data = pandas.read_csv("50_states.csv")
# make list of state name & transform state name to lowercase
state_list = data.state.str.lower().to_list()
print(state_list)

# set turtle window
screen = turtle.Screen()
# screen.setup(725, 491)
screen.title('U.S. States Game')

# Set image for turtle to use
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


game_on = True

while game_on:
    user_guess = screen.textinput(title="Guess The State", prompt="Please guess another state:").lower()
    print(user_guess)

    for state in state_list:
        if user_guess == state:
            print(True)




turtle.mainloop()
