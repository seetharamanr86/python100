from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()


print("Welcome to Coffee Shop!!")
print("------------------------")

drink_flag = True

while drink_flag:
    print("** Choose from the below list of available drinks :")
    print(menu.get_items())
    customer_drink = input("** Enter the drink you like: ")
    if customer_drink == 'report':
        print(coffee_maker.report())
        print(money_machine.report())
    elif customer_drink == 'off':
        exit()
    else:
        try:
            drink_name_exists = menu.find_drink(customer_drink).name
        except:
            drink_name_exists = 'Invalid_Name'
        print("drink_name_exists"+drink_name_exists)
        if customer_drink == 'report':
            coffee_maker.report()
            money_machine.report()
        elif customer_drink == 'off':
            exit()
        elif drink_name_exists == 'Invalid_Name':
            print("Invalid Entry, Please Try Again!")
        elif drink_name_exists != 'Invalid_Name':
            drink_available = coffee_maker.is_resource_sufficient(menu.find_drink(customer_drink))
            if drink_available is True:
                money_paid_status = money_machine.make_payment(menu.find_drink(customer_drink).cost)
                if money_paid_status is True:
                    coffee_maker.make_coffee(menu.find_drink(customer_drink))
            else:
                print("Sorry, We are out of stock!")

