import random

card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# card_list = [11, 10, 10, 23, 10, 32, 11, 141, 61, 12, 106, 10, 10]
player_card_list = []
comp_card_list = []
# player_draw_card = True
# comp_draw_card = True

# Draw card function
def draw_card(deck):
  drawed_card = random.choice(card_list)
  return drawed_card

# Player draw card 
def player_draw_card():
  new_card = draw_card(card_list)
  player_card_list.append(new_card)

# Computer draw card
def comp_draw_card():
  new_card = draw_card(card_list)
  comp_card_list.append(new_card)

# Calculate total player's and computer's total card value and check Ace value
def count_total_card_value(player_cards, comp_cards):
  player_total = sum(player_cards)
  comp_total = sum(comp_cards)

  while player_total > 21 and 11 in player_cards:
    player_cards = adjust_ace_value(player_cards)
  while comp_total > 21 and 11 in comp_cards:
    comp_cards = adjust_ace_value(comp_cards)

  return player_cards, comp_cards, player_total, comp_total 

# adjust Ace value to 1 if card total value is > 21 else Ace value is 11
def adjust_ace_value(card_list):
  index = card_list.index(11)
  card_list[index] = 1
  return card_list

# Check if player or computer has Blackjack
def balckjack_checker(game_ends, player_total, comp_total):
  if player_total == 21:
    print("you won")
    return True
  elif comp_total == 21:
    print("You loose! Computer got 21")
    return True
  elif player_total > 21:
    print("You loose")
    return True
  elif comp_total > 21:
    print("You win")
    return True

def end_game_score_checker(player_total, comp_total):
  if player_total < comp_total:
    print("You won")
    return True
  elif comp_total > player_total:
    print("You Loose")
    return True
  elif player_total == comp_total:
    print("Draw")
    return True



''' ------------ START ------------ '''


# Print card lists at the start
# print(f"Your card: {player_card_list} \nComp card: {comp_card_list}")

# print(player_card_list)
# Display computer's first card
# print(f"Conmputer's fist card: {comp_card_list[0]}")

  # Draw 2 cards for player and computer 
for cards in range(2):
  player_draw_card()
  comp_draw_card()

def balckjack_game(player_card_list, comp_card_list):
  game_ends = False
  while not game_ends:
    # print(f"Your cards: {player_card_list}")
    # print(f"Computer cards: {comp_card_list}")

    # Count total and adjust Ace value
    player_card_list, comp_card_list, player_total, comp_total = count_total_card_value(player_cards=player_card_list, comp_cards=comp_card_list)

    # incase player or computer get 2xAce at the beginning of the game
    if player_total > 21 or comp_total > 21:
      player_card_list, comp_card_list, player_total, comp_total = count_total_card_value(player_cards=player_card_list, comp_cards=comp_card_list)
      
    # Display player's card and display card total
    print(f"Your cards: {player_card_list} player total: {player_total}")
    print(f"Computer cards: {comp_card_list} player total: {comp_total}")

    # game ends immediately when player or computer socre is 21
    game_ends = balckjack_checker(game_ends, player_total, comp_total)

    if game_ends == True:
      return game_ends

    draw_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if draw_another_card == "y":
      player_draw_card()
      balckjack_game(player_card_list, comp_card_list)
    elif draw_another_card == "n":
      while comp_total <= 16:
        comp_draw_card()
        player_card_list, comp_card_list, player_total, comp_total = count_total_card_value(player_cards=player_card_list, comp_cards=comp_card_list)
      game_ends = end_game_score_checker(player_total, comp_total)
      game_ends = balckjack_checker(game_ends, player_total, comp_total)

    if game_ends == True:
      return game_ends
    

balckjack_game(player_card_list, comp_card_list)





# player_ask_for_card = input("Type 'y' to get another card or type 'n' to pass:").lower()
# if player_ask_for_card == "y":
#   player_draw_card = True
#   draw_card(card_list, player_draw_card, comp_draw_card)

# print(f"Your card: {player_card_list} \n Comp card: {comp_card_list}")































############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.






