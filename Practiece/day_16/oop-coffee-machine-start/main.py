from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
item_list = []


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True




while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_resources = coffee_maker.is_resource_sufficient(drink)

        if is_enough_resources:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

        

# menu_item = MenuItem(item_list[0], item_list[1], item_list[2], item_list[3], item_list[4])
# resource = CoffeeMaker.is_resource_sufficient(menu_item)
# print(resource)