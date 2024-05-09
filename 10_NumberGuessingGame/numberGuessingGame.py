import random
import subprocess
from numberGuessingGame_graphics import logo
num = random.choice(range(1,100))
print(f"The hidden number is: {num}")

# ----- MAIN GAME LOGIC ----
def game():
    print(logo)
    print("I'm thinking of a number between 1 and 100")

    # ask player what diffecult level they wanna start this game with
    difficulty_level = input("Choose a difficulty.\nType 'e' for easy or 'h' for Hard: ").lower()
    # for easy level player gets 10 guess attempts
    if difficulty_level == "e":
        attempts = 10
    # for hard level player gets 5 guess attempts
    elif difficulty_level == "h":
        attempts = 5
    print(f"You have {attempts} guesses")

    while attempts != 0:
        # ask the player to guess a number
        guessed_num = int(input("Guess the number: "))
        # check if the number is higher or lower
        if guessed_num < num:
            print("Your guess is too low")
        elif guessed_num > num:
            print("Your guess is too high")
        elif guessed_num == num:
            print(f"You guessed it! The answer is {num}")
            break
        # subtract guesses if guessed wrong number
        attempts -= 1

        print(f"You have {attempts} guesse left")
        # if player is out of guess attempts he/she loses
        if attempts == 0:
            print("You lost! You've run out of guesses 😓")
            print(f"The number I was thinking was: {num}")

# ----- FUNCTION LOOP -----
def main():
    while True:
        game()
        new_game = input("Wanna play again\nType (y/n): ").lower()
        if new_game != "y":
            return False
        subprocess.run("clear", shell=True)

main()