import random
from hangman_wordlist import word_list # import word list from hangman_wordlist file
from hangman_graphics import logo, stages # import logo and hangman graphics from hangman_graphics file

# Randomly choose a word from word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word) #prints the hidden word for debuging or test
# defines lives
lives = 6

'''---------GAME-LOGIC---------'''

# Stars the game by priting TITLE (logo) of the game
print(logo)

# Careate empty list and asigned it to variable display
display = []
# For each letter in the chosen_word, add a "_" to 'display' list.
for i in range(word_length):
  display.append("_")

#print the "_" display list
print(display)


# Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
while "_" in display and lives > 0:
  # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
  guess = input("Guess a letter: ").lower()
  
  # If the user has entered a letter they've already guessed, inform the player about it.
  if guess in display:
    print(f"The \"{guess}\” has already been guessed")

  # Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  print(display)
  
  # If guess is not a letter in the chosen_word, reduce 'lives' by 1.
  # If lives goes down to 0 then the game stops and it should print "You lose."
  if guess not in chosen_word:
    lives -= 1
    print(f"This letter is not in the word. Your have {lives} lives remain")
    if lives == 0:
      print("SORRY, YOU LOOSE THE GAME")

  # Check if user has got all letters.
  if "_" not in display:
    print("GREAT, YOU WON THE GAME")

  # print graphics of hangman
  print(stages[lives])
  
