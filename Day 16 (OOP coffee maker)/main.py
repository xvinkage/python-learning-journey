from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
is_on = True
drink_menu = Menu()
money = MoneyMachine()
# item = MenuItem(print, "water", "milk", "coffee", "cost")

while is_on:
    options = drink_menu.get_items()
    user_choice = input(f"What would you like? ({options}): ")
    if user_choice == "report":
        coffee_machine.report()
        money.report()
    elif user_choice == "off":
        print("The coffee machine was shut of for maintenance.")
        is_on = False
    else:
        drink = drink_menu.find_drink(user_choice)
        if user_choice == drink.name:
            enough_resources = coffee_machine.is_resource_sufficient(drink)
            if enough_resources:
                money.make_payment(drink.cost)
                coffee_machine.make_coffee(drink)