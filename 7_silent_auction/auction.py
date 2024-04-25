import subprocess
from graphics import logo
#HINT: You can call clear() to clear the output in the console.

bid_data = {}
more_bid = True

# this function adds name and bid value to the bid_data dictionary
def add_bids(name, bid, bidding_logs):
  bidding_logs[name] = bid
#  print(bid_logs)

def get_highest_bidder(bidding_logs):
  higest_bidder = ""
  higest_bid = 0
  
  for name in bid_data:
    bid_amount = bid_data[name]
    if higest_bid < bid_amount:
      higest_bid = bid_amount
      higest_bidder = name
  print(f"The winner is {higest_bidder} with a bid of ${higest_bid}")

while more_bid:
  print(logo)
  # ask bidder name and how much they want to bid
  name = input("What is your name?:\n")
  bid = int(input("What is your bid?: $\n"))
  # call fucntion to add the bidder name and bid value to the bid_data dictionary
  add_bids(name=name, bid=bid, bidding_logs=bid_data)
  
  # check if there is more bidders
  continue_biding = input("Are there any other bidders? Type \"yes\" or \"no\":\n")
  
  # if "no"
  if continue_biding == "no":
    # Get the higest bidder name and bidding amount
    get_highest_bidder(bidding_logs=bid_data)
    # assaign more_bid to False for exiting
    more_bid = False
  elif continue_biding == "yes":
    # clears the terminal screen
    subprocess.run("clear", shell=True)

  

