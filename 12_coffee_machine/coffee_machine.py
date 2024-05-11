import subprocess
from machine_data import MENU, resources, HOT_DRINK


def drink_list():
    """ Get all the hot drink names from hot_drinks dictionary 
    and prints them while this function is called """
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

def total_money():
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

    if total >= 2.50:
        change = total - 2.50
        print(f"You inserted {total}€. Here is {change}€ in change")
        resources["money"] += 2.50
        return True

    print(f"Sorry, not enough money. {total}€ has been refunded")
    return False

def make_drink(drink):
    # print(MENU)
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    # print(resources)
# make_drink("Espresso")


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
        elif int(user_request) in range(1,4):
            # get wanted drink to and assign to drink variable
            drink = HOT_DRINK[user_request]
            print(f"{drink} cost 2.50€")
            print("Only 2€ / 1€ / 50c are accepted. Please insert your coins.")

            if total_money():
                # if enough money make drink
                make_drink(drink)
                # drink gets served
                print(f"Here is your {drink} ☕️. Enjoy!")


run_machine()