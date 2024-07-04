# import calss and variables from files
from read_csv import all_states
from state_on_map import StatePlacement
# import pandas and turtle
import pandas
import turtle


# global variables
guessesed_states = []
total_states = len(all_states)
total_guesses = len(guessesed_states)


# set turtle window
screen = turtle.Screen()
screen.setup(725, 491)
screen.title('U.S. States Game')
# Set image for turtle to use
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# create object from StatePlacement class
state_placement = StatePlacement()

# main logic
while total_guesses < total_states:
    #set up prompt window
    user_guess = screen.textinput(title=f"{total_guesses}/{total_states} Correct Guesses",
    prompt="Please guess another state:").title()

    # check user guess and place state name on map if the guess is correct
    for state in all_states:
        if user_guess == state:
            # append correctly guessed state to guessesed_states list and remove from all_state_list
            guessesed_states.append(user_guess)
            all_states.remove(user_guess)
            # place state name on map
            state_placement.to_x_y_pos(user_guess)

    # check if user wants to exit the game
    if user_guess == "Exit":
        unguessed_states = all_states
        # create csv file of unguessed states
        unguessed_states_data = pandas.DataFrame(unguessed_states)
        unguessed_states_data.to_csv("unguessed_states.csv")
        # create csv file of guessed states
        guessed_states_data = pandas.DataFrame(guessesed_states)
        guessed_states_data.to_csv("guessed_states.csv")
        break

