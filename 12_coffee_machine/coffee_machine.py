import subprocess
from machine_data import MENU, resources, HOT_DRINK


def drink_list():
    """ Get all the hot drink names from hot_drinks dictionary 
    and prints them while this function is called """
    print("") #print an empty line
    print("  -----HOT FLAVOUR LIST-----")
    for num, drink in HOT_DRINK.items():
        print(f"{num}. {drink}")

def report():
    """ Get ingredients from resources dictionary
    and prints them while this function is called """

    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print("-----REPORT-----")
    print(f"Water = {water} ml")
    print(f"Milk = {milk} ml")
    print(f"Coffee = {coffee} g")
    print(f"Money = {money} €")
    # MY VSCODE DID NOT LIKE IF I PRINTED LIKE:
    # print(f"Water = {resources["water"]}")
    # IT RETURN "SyntaxError". NOT SURE WHY!

def check_enough_ingredient(drink):
    """ Check if there is enough ingredient """
    print("") #print an empty line
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry, not enough water ⚠️")
        return False
    if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
        print("Sorry, not enough milk ⚠️")
        return False
    if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry not enough coffee ⚠️")
        return False
    return True

def total_money(cost):
    """ 
    - Ask user what coins they are inserting and how many.
    - calculate total money.
    - subtract 2.50€ from total.
    - gave change back
    - add money to the resources dictionary
    - if not enough money refund money
    - serve the drink
    """
    euro_2 = int(input("How many 2€ coins: "))
    euro_1 = int(input("How many 1€ coins: "))
    cent_50 = int(input("How many 50c coins: "))
    # calculate total
    total = 2*euro_2 + 1*euro_1 + 0.50*cent_50

    if total >= cost:
        change = total - cost
        print("") #print an empty line
        print(f"You inserted {total}€. Here is {change}€ in change")
        resources["money"] += cost
        return True
    
    print("") #print an empty line
    print(f"Sorry, not enough money. ⚠️\n{total}€ has been refunded. ✅")
    return False

def make_drink(drink):
    """ Make a drink and subtract ingredient from the resources. """
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]

    # drink gets served
    print(f"Here is your {drink} ☕️. Enjoy! ✅")


def run_machine():
    """ Main machine logic """
    power_on = True
    while power_on:

        # prints all drinks from the hot drink list
        drink_list()
        # ask the user which drink they want to have
        user_request = input("What would you like?\nPlease insert hot drink number: ").lower()
        # Ask for coins
        if user_request == "report":
            report()
        elif user_request == "off":
            power_on = False
            print("POWERING OFF")
            break
        elif HOT_DRINK[user_request] and check_enough_ingredient(HOT_DRINK[user_request]):
            # get wanted drink to and assign to drink variable
            drink = HOT_DRINK[user_request]
            # assign drink's cost to cost variable
            cost = cost = MENU[drink]["cost"]
            print("") #print an empty line
            print(f"{drink} cost 2.50€")
            print("Only 2€ / 1€ / 50c are accepted. Please insert your coins.")

            if total_money(cost):
                # if enough money make drink
                make_drink(drink)


run_machine()