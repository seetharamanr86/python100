

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

# Function to print report

def print_report():
    print ("Water: " + str(resources['water']) +"ml")
    print ("Milk: " + str(resources['milk']) + "ml")
    print ("Coffee: " + str(resources['coffee']) + "g")
    print ("Money: $" + str(resources['money']))

# Function to make espresso

def make_espresso():
    resource_status=check_resources("espresso")
    money_collected = get_money()
    money_status = check_money("espresso", money_collected)
    if resource_status == 'available' and money_status == 'enough':
        resources['water'] = resources['water'] - 50
        resources['coffee'] = resources['coffee'] - 18
        resources['money'] = resources['money'] + 1.5
        print("Here is your espresso ☕️. Enjoy!")
        if money_collected > 1.5:
            print("Here is $"+ str(money_collected-1.5) +"in change")
    else:
        exit()

# Function to make espresso

def make_latte():
    resource_status=check_resources("latte")
    money_collected = get_money()
    money_status = check_money("latte",money_collected)
    if resource_status == 'available' and money_status == 'enough':
        resources['water'] = resources['water'] - 200
        resources['milk'] = resources['milk'] - 150
        resources['coffee'] = resources['coffee'] - 24
        resources['money'] = resources['money'] + 2.5
        print("Here is your latte ☕️. Enjoy!")
        if money_collected > 2.5:
            print("Here is $"+ str(money_collected-2.5) +"in change")
    else:
        exit()

# Function to make espresso

def make_cappuccino():
    resource_status = check_resources("cappuccino")
    money_collected = get_money()
    money_status = check_money("cappuccino", money_collected)
    if resource_status == 'available' and money_status == 'enough':
        resources['water'] = resources['water'] - 250
        resources['milk'] = resources['milk'] - 100
        resources['coffee'] = resources['coffee'] - 24
        resources['money'] = resources['money'] + 3
        print("Here is your cappuccino ☕️. Enjoy!")
        if money_collected > 3:
            print("Here is $"+ str(money_collected-3) +"in change")
    else:
        exit()


# Function to check if enough resources present

def check_resources(coffee):
    if coffee == 'espresso':
        if resources['water'] < 50:
            print("Sorry there is not enough water.")
            exit()
        elif resources['coffee'] < 18:
            print("Sorry there is not enough coffee.")
            exit()
        else:
            return 'available'
    elif coffee == 'latte':
        if resources['water'] < 200:
            print("Sorry there is not enough water.")
            exit()
        elif resources['coffee'] < 24:
            print("Sorry there is not enough coffee.")
            exit()
        elif resources['milk'] < 150:
            print("Sorry there is not enough milk.")
            exit()
        else:
            return 'available'
    elif coffee == 'cappuccino':
        if resources['water'] < 250:
            print("Sorry there is not enough water.")
            exit()
        elif resources['coffee'] < 24:
            print("Sorry there is not enough coffee.")
            exit()
        elif resources['milk'] < 100:
            print("Sorry there is not enough milk.")
            exit()
        else:
            return 'available'

# Function to check if enough money

def check_money(coffee,money_collected):
    if coffee == 'espresso':
        if money_collected < 1.5:
            print("Sorry there is not enough money. Money refunded.")
            return 'not enough'
        else:
            return 'enough'
    elif coffee == 'latte':
        if money_collected < 2.5:
            print("Sorry there is not enough money. Money refunded.")
            return 'not enough'
        else:
            return 'enough'
    elif coffee == 'cappuccino':
        if money_collected < 3:
            print("Sorry there is not enough money. Money refunded.")
            return 'not enough'
        else:
            return 'enough'

def get_money():
    print("Please insert coins.")
    count_quarters = int(input("how many quarters?: "))
    count_dimes = int(input("how many dimes?: "))
    count_nickles = int(input("how many nickles?: "))
    count_pennies = int(input("how many pennies?: "))
    money_collected = 0.25 * count_quarters + 0.10 * count_dimes + 0.05 * count_nickles + 0.01 * count_pennies
    return money_collected

# Function to Prompt user to choose the drink

def get_user_choice():
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ")
    while drink_choice not in ('espresso','latte','cappuccino','report','off'):
        print("Invalid Entry, Please Try Again!!")
        drink_choice = input("What would you like? (espresso/latte/cappuccino): ")
    return drink_choice

# Get user choice

drink_choice = get_user_choice()

# Take action as per user choice

while drink_choice in ('espresso','latte','cappuccino','report','off'):
    if drink_choice == 'report':
        print_report()
        drink_choice=get_user_choice()
    if drink_choice == 'espresso':
        make_espresso()
        drink_choice = get_user_choice()
    if drink_choice == 'latte':
        make_latte()
        drink_choice=get_user_choice()
    if drink_choice == 'cappuccino':
        make_cappuccino()
        drink_choice=get_user_choice()
    if drink_choice == 'off':
        exit()

