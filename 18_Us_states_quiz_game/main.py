# import calss and variables from files
from read_csv import all_states
from state_on_map import StatePlacement
# import pandas and turtle
import pandas
import turtle

# global variables
guessed_states = []
total_states = len(all_states)
# total_guesses = len(guessed_states)

# set turtle window
screen = turtle.Screen()
screen.setup(725, 491)
screen.title('U.S. States Game')
# Set image for turtle to use
image = "./image_file/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# create object from StatePlacement class
state_placement = StatePlacement()

# main logic
while len(guessed_states) < total_states:
    #set up prompt window
    user_guess = screen.textinput(title=f"{len(guessed_states)}/{total_states} Correct Guesses",
    prompt="Please guess another state:").title()

    # check user guess and place state name on map if the guess is correct
    for state in all_states:
        if user_guess == state:
            # append correctly guessed state to guessed_states list and remove from all_state_list
            guessed_states.append(user_guess)
            print(f"here: {guessed_states}")
            all_states.remove(user_guess)
            # place state name on map
            state_placement.to_x_y_pos(user_guess)

    # check if user wants to exit the game
    if user_guess == "Exit" or len(guessed_states) == total_states:
        # create csv file of unguessed states
        unguessed_states_data = pandas.DataFrame(all_states)
        unguessed_states_data.to_csv("./game_record_files/unguessed_states.csv")
        # create csv file of guessed states
        guessed_states_data = pandas.DataFrame(guessed_states)
        guessed_states_data.to_csv("./game_record_files/guessed_states.csv")
        break
