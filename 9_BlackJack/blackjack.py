import random
from blackjack_graphics import logo
card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Draw card function
def draw_card(deck):
  return random.choice(card_list)

# Player draw card 
def player_draw_card(player_cards):
  new_card = draw_card(card_list)
  player_cards.append(new_card)

# Computer draw card
def comp_draw_card(comp_cards):
  new_card = draw_card(card_list)
  comp_cards.append(new_card)

# Calculate total card value and adjust Ace value
def count_total_card_value(cards):
  card_total = sum(cards)
  while card_total > 21 and 11 in cards:
    ace_index = cards.index(11)
    cards[ace_index] = 1
    card_total = sum(cards)
  return card_total 

# check if there is backjack
def balckjack(card_total):
  if card_total == 21:
    return False

# check for winner
def determine_winner(player_total, comp_total):
  if player_total > 21:
    print("Computer Wins")
  if comp_total > 21:
    print("You won")
  elif player_total == comp_total:
    print("Draw")
  elif (player_total-21) > (comp_total-21):
    print("You won")
  elif (player_total-21) < (comp_total-21):
    print("You Loose")


''' ------------ MAIN LOGIC ------------ '''
# game logic function
def balckjack_game():
  # prints game logo
  print(logo)

  player_card_list = []
  comp_card_list = []

  # Draw 2 cards for player and computer 
  for card in range(2):
    player_draw_card(player_card_list)
    comp_draw_card(comp_card_list)

  game_continue = True

  while game_continue:
    # calculate player's total card value
    player_total = count_total_card_value(cards=player_card_list)
    # prints player's curret cards, total values and computer's first card
    print(f"Your cards: {player_card_list} player total: {player_total}")
    print(f"Computer first card: [{comp_card_list[0]}]")

    # ckeck if player has balckjack or total card value is over 21
    if player_total == 21:
      print("Blackjack! You win!")
      game_continue = False
      break
    # check if player card total value if over 21
    if player_total > 21:
      print("You lost the game")
      game_continue = False
      break

    # ask player if he/she wants to get another card
    draw_another_card = input("Type 'y' to get another card or type 'n' to pass: ").lower()

    # if "Yes" draw a card for the player
    if draw_another_card == "y":
      player_draw_card(player_card_list)

    # If player do not want to draw, computer starts drawing cards 
    elif draw_another_card == "n":
      # calculates computer's total card value
      comp_total = count_total_card_value(cards=comp_card_list)
      # computer draw card until it's score is at least card total is 16
      while comp_total <= 16:
        comp_draw_card(comp_card_list)
        comp_total = count_total_card_value(cards=comp_card_list)
      # prints player's cards + total value and computer's card + total value
      print(f"Your cards: {player_card_list} player total: {player_total}")
      print(f"Computer cards: {comp_card_list} Computer total: {comp_total}")
      # checks who won the game
      determine_winner(player_total, comp_total)
      game_continue = False

  return

# game loop function
def main():
  new_game = True
  while new_game:
    balckjack_game()
    start_new_game = input("Press 'y' for new game\nPress 'n' to quit\nWould you like to play another game?: ")
    if start_new_game != "y":
      new_game = False

main()


