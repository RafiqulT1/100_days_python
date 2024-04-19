rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_choice = int(input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0, 2)
move_list = [rock, paper, scissors]

if user_choice >= 3 or user_choice < 0:
  print("Please chose number between 0-2")
else:
  print("You chose:")
  print(move_list[user_choice])
  print("Computer chose:")
  print(move_list[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("You win")
  elif user_choice == 1 and computer_choice == 0:
    print("You win")
  elif user_choice == 2 and computer_choice == 1:
    print("You win")
  elif user_choice == computer_choice:
    print("Draw")
  else:
    print("You lose")

#Win:
# 0 win 2
# 1 win 0
# 2 win 1

#Lose:
# 0 lose 1
# 1 lose 2
# 2 lose 0

#Draw:
# 0 draw 0
