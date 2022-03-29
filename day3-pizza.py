print("Welcome to Dominos!!")

size=input("What size of pizza do you want? S, M or L: ")

pepperoni = input("Do you need pepperoni topping? Y or N: ")

cheese = input("Do you need extra cheese? Y or N: ")

price=0

if size == 'S':
    price=15
    if pepperoni == 'Y':
        price+=2
    if cheese == 'Y':
        price += 1
elif size == 'M':
    price = 20
    if pepperoni == 'Y':
        price += 3
    if cheese == 'Y':
        price += 1
elif size == 'L':
    price = 25
    if pepperoni == 'Y':
        price += 3
    if cheese == 'Y':
        price += 1

print(f"Price for your order is {price}")

