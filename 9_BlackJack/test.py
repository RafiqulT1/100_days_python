# Initial card list
card_list = [11, 2, 4, 11, 5, 3]

# Function to get the total of the card list
def get_total(cards):
    return sum(cards)

# Function to adjust 11 to 1 if the total is over 21
def adjust_ace(cards):
    while get_total(cards) > 30 and 11 in cards:
        # Find the index of the first occurrence of 11 and change it to 1
        index = cards.index(11)
        cards[index] = 1
    return cards

# Calculate the initial total
initial_total = get_total(card_list)
print("Initial Total:", initial_total)

# Adjust the list if the total is over 21
if initial_total > 21:
    card_list = adjust_ace(card_list)

print(card_list)
# Calculate the new total
new_total = get_total(card_list)
print("Adjusted Card List:", card_list)
print("New Total:", new_total)