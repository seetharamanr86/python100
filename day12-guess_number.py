import random

print("Welcome to the number guessing game!")

print("I am thinking of a number between 1 and 100")

level = input("Choose a difficulty level. Type 'easy' or 'difficult': ")

random_number = random.randint(1, 100)

print(random_number)

result = "invalid"

counter = 0

def validate(user_number, random_number):
    if user_number==random_number:
        return "valid"
    else:
        if user_number > random_number:
            print ("Too high")
        else:
            print ("Too low")
        return "invalid"

if level == "easy":
    while counter != 10:
        print("You hv " + str(10 - counter) + " attempts remaining to guess the number")
        counter = counter + 1
        user_number = int(input("Make a guess: "))
        result = validate(user_number, random_number)
        if result == "valid":
            print ("Your guess is correct")
            exit()
    print ("Better luck next time")
elif level == "difficult":
    while counter != 5:
        print("You hv " + str(5 - counter) + " attempts remaining to guess the number")
        counter = counter + 1
        user_number = int(input("Make a guess: "))
        result = validate(user_number, random_number)
        if result == "valid":
            print ("Your guess is correct")
            exit()
    print ("Better luck next time")







