MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

units = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
    "money": "$",

}
# TODO: 1. Print report of coffeemachine resources


def report():
    """Prints report of current resources"""
    for item in resources:
        if item == "money":
            print(f"{item}: {units[item]}{resources[item]:.2f}")
        else:
            print(f"{item}: {resources[item]}{units[item]}")

    # return resources

# TODO 2. Check resources sufficient.


def check_resources(user_choice):
    #use the table instead of each individual variable
    required_ingredients = MENU[user_choice]["ingredients"]
    insufficient = []

    for item in required_ingredients:
            resources_level = resources[item]
            resources_needed = MENU[user_choice]["ingredients"][item]
            if resources_level < resources_needed:
                insufficient.append(item)
    if insufficient:
            return f"Sorry there is not enough {" and ".join(insufficient)} "
    return True

# TODO 3. Process coins if there are sufficient resources. calculate monetary value

coins= {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies ": 0.01}

#TODO 4. Check transaction was nenough money and the money is added a resource, machine offers change


def calc_money():
    grand_total = 0
    print("Please insert coins")
    for coin, price in coins.items():
        amount = int(input(f"How many {coin}?: "))
        coin_total = price * amount
        grand_total += coin_total
    return grand_total


def make_drink(user_choice):
    required_ingredients = MENU[user_choice]["ingredients"]
    for item in required_ingredients:
        resources[item] -= required_ingredients[item]
    return resources

# TODO 5. Make cofee if transcation successful and enough resources, deduct the ingredidents from resources


machine_on = True

while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if user_choice == "off":
        machine_on = False

    elif user_choice == "report":
        report()

    elif user_choice in MENU:

        enough_resources = check_resources(user_choice)
        if enough_resources == True:
            money_inserted = calc_money()
            # print(money_inserted)
            if money_inserted >= MENU[user_choice]["cost"]:
                resources["money"] += MENU[user_choice]["cost"]
                if money_inserted > MENU[user_choice]["cost"]:
                    change = money_inserted - MENU[user_choice]["cost"]
                    print(f"Here is ${change:.2f} in change.")
                make_drink(user_choice)
                print(f"Here is your {user_choice}. Enjoy!")

            elif money_inserted < MENU[user_choice]["cost"]:
                print(f"Sorry that's not enough money. Money refunded ${money_inserted}")
        else:
            print(enough_resources)
    else:
        print("Enter a valid selection")