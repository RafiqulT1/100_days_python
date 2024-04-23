#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Step 1 
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word)
lives = 6

# For each letter in the chosen_word, add a "_" to 'display'.

display = []

for i in range(word_length):
  display.append("_")
  
print(display)
# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.


# Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
while "_" in display or lives > 0:
  guess = input("Guess a letter: ").lower()

#Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  print(display)
  
#If guess is not a letter in the chosen_word, reduce 'lives' by 1.
#If lives goes down to 0 then the game stops and it should print "You lose."
  if guess not in chosen_word:
    lives -= 1
    print(f"Lives left {lives}")
    if lives == 0:
      print("you lose")

  if "_" not in display:
    print("You did it!")

  print(stages[lives])
  
