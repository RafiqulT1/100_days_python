from read_csv import df, all_state_list
from state_on_map import StatePlacement
import pandas
import turtle


# global variables
guessesed_states = []
total_states = len(all_state_list)
total_guesses = len(guessesed_states)


# set turtle window
screen = turtle.Screen()
screen.setup(725, 491)
screen.title('U.S. States Game')
# Set image for turtle to use
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# create class
state_placement = StatePlacement()



while total_guesses < total_states:
    user_guess = screen.textinput(title=f"{total_guesses}/{total_states} Correct Guesses",
    prompt="Please guess another state:").title()

    for state in all_state_list:
        if user_guess == state:
            guessesed_states.append(user_guess)
            all_state_list.remove(user_guess)
            state_placement.to_x_y_pos(user_guess)

    if user_guess == "Exit":
        unguessed_states = all_state_list
        unguessed_states_data = pandas.DataFrame(unguessed_states)
        unguessed_states_data.to_csv("unguessed_states.csv")
        guessed_states_data = pandas.DataFrame(guessesed_states)
        guessed_states_data.to_csv("guessed_states.csv")
        break

