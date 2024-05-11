from game_data import data
from game_graphics import logo, vs
import random
import subprocess

# choose random data form game_data
def choose_data():
    rand_num = random.randint(0, len(data)-1)
    name = data[rand_num]["name"]
    followers = data[rand_num]["follower_count"]
    description = data[rand_num]["description"]
    country = data[rand_num]["country"]
    return name, followers, description, country


# Campare A & B followers and check if user answer is correct
def compare_follower(guess, A_follower, B_follower):
    if A_follower > B_follower and guess == 'a':
        return True
    elif B_follower > A_follower and guess == 'b':
        return True
    elif (B_follower == A_follower or A_follower == B_follower) and (guess == 'a' or guess == 'b'):
        return True
    else:
        return False


def game_logic(A_name, A_follower, A_description, A_country, score, correct_guess):

    while correct_guess:
        # assaign data in to B group variables 
        B_name, B_follower, B_description, B_country = choose_data()
        
        # prints A and B group variables
        print(f"{A_name}, {A_follower}, {A_description}, {A_country}")
        print(vs) # print game logo
        print(f"{B_name}, {B_follower}, {B_description}, {B_country}")

        # ask user to guess who/which has the most followers
        print("")
        guess = input("Who has more followers? Type (A/a) or (B/b): ").lower()


        correct_guess = compare_follower(guess, A_follower, B_follower)

        if correct_guess:
            # assaign B group variables to new A group valiable
            A_name = B_name
            A_follower = B_follower
            A_description = B_description
            A_country = B_country
            score += 1 # add + 1 to the score 

            # Clear the termianl screen
            subprocess.run("clear", shell=True)
            print(logo) # print game logo
            print(f"That's Correct. Your Score: {score}") # let the user know that the guess it correct

            # call for game logic with new A group variable
            game_logic(A_name, A_follower, A_description, A_country, score, correct_guess)

        elif not correct_guess:
            subprocess.run("clear", shell=True)
            print(logo)
            print(f"Sorry, {guess.upper()} is wrong answer.")
            print(f"A: {A_name} has {A_follower}M followers")
            print(f"B: {B_name} has {B_follower}M followers")
            print( f"You final score is {score}")

        # exit while loop if wrong guess
        break 



def main():
    correct_guess = True
    game_ends = False
    score = 0
    while not game_ends:
        subprocess.run("clear", shell=True)
        print(logo)

        # assaign data in to A group variables 
        A_name, A_follower, A_description, A_country = choose_data()

        # calls for game logic with A group variable values
        game_logic(A_name, A_follower, A_description, A_country, score, correct_guess)

        game_ends = True # change game_ends value to False

        print("")
        # asks user if they wants to play a new game
        new_game = input("Do you want to play a new game? Type (Y/y) or (N/n): ").lower()
        if game_ends == True and new_game == 'y':
            main()
        
        break
            
main()





