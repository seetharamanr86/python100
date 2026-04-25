
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
    "money": 0
}


def print_report():
    print("Water: " + str(resources['water']) + "ml")
    print("Milk: " + str(resources['milk']) + "ml")
    print("Coffee: " + str(resources['coffee']) + "g")
    print("Money: $" + str(resources['money']))


def check_resources(coffee):
    ingredients = MENU[coffee]['ingredients']
    for ingredient, amount in ingredients.items():
        if resources[ingredient] < amount:
            print(f"Sorry there is not enough {ingredient}.")
            return 'unavailable'
    return 'available'


def check_money(coffee, money_collected):
    cost = MENU[coffee]['cost']
    if money_collected < cost:
        print("Sorry there is not enough money. Money refunded.")
        return 'not enough'
    return 'enough'


def get_money():
    print("Please insert coins.")
    count_quarters = int(input("how many quarters?: "))
    count_dimes = int(input("how many dimes?: "))
    count_nickles = int(input("how many nickles?: "))
    count_pennies = int(input("how many pennies?: "))
    return 0.25 * count_quarters + 0.10 * count_dimes + 0.05 * count_nickles + 0.01 * count_pennies


def make_drink(coffee):
    resource_status = check_resources(coffee)
    money_collected = get_money()
    money_status = check_money(coffee, money_collected)
    if resource_status == 'available' and money_status == 'enough':
        cost = MENU[coffee]['cost']
        for ingredient, amount in MENU[coffee]['ingredients'].items():
            resources[ingredient] -= amount
        resources['money'] += cost
        print(f"Here is your {coffee} ☕️. Enjoy!")
        change = round(money_collected - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change")


def get_user_choice():
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ")
    while drink_choice not in ('espresso', 'latte', 'cappuccino', 'report', 'off'):
        print("Invalid Entry, Please Try Again!!")
        drink_choice = input("What would you like? (espresso/latte/cappuccino): ")
    return drink_choice


drink_choice = get_user_choice()

while drink_choice != 'off':
    if drink_choice == 'report':
        print_report()
    elif drink_choice in MENU:
        make_drink(drink_choice)
    drink_choice = get_user_choice()

