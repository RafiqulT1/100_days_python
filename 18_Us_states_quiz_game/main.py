from read_csv import df, all_state_list
from state_on_map import StatePlacement
import turtle


# global variables
total_states = len(all_state_list)
correct_guesses = 0




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



game_on = True

while correct_guesses < total_states:
    user_guess = screen.textinput(title=f"{correct_guesses}/{total_states} Correct Guesses",
    prompt="Please guess another state:").title()

    for state in all_state_list:
        if user_guess == state:
            correct_guesses += 1
            state_placement.to_x_y_pos(user_guess)


turtle.mainloop()
