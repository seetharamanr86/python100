
print("Welcome to Treasure Island!!")

direction=input("Which direction do you want to take? right or left: ")

if direction=='left':
    cross=input("How do you want to cross the water to reach island? boat or swim: ")
    if cross=='boat':
        door=input("Which door you want to open? yellow or red or blue: ")
        if door=='yellow':
            print("Hurray, found the treasure!!")
        elif door=='blue':
            print("Sorry, got killed by Lion")
        else:
            print("Sorry, got killed by Ghost")
    else:
        print("Sorry, you were eaten by crocodile")
else:
    print("Sorry, you fell into the hole")