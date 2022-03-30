import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_input=int(input("Enter one of your choice - 0 for Rock, 1 for Paper, 2 for Scissors: "))

if user_input==0:
    user_choice='Rock'
    user_graphic=rock
elif user_input==1:
    user_choice = 'Paper'
    user_graphic = paper
else:
    user_choice = 'Scissors'
    user_graphic = scissors

print(user_choice)
print(user_graphic)

computer_input=random.randint(0,2)

if computer_input==0:
    computer_choice='Rock'
    computer_graphic=rock
elif computer_input==1:
    computer_choice = 'Paper'
    computer_graphic = paper
else:
    computer_choice = 'Scissors'
    computer_graphic = scissors

print(computer_choice)
print(computer_graphic)

if user_choice == computer_choice:
    print("Its a tie!!")
elif user_choice == 'Rock' and computer_choice == 'Paper':
    print("Computer Won!!")
elif user_choice == 'Rock' and computer_choice == 'Scissors':
    print("You Won!!")
elif user_choice == 'Paper' and computer_choice == 'Rock':
    print("You Won!!")
elif user_choice == 'Paper' and computer_choice == 'Scissors':
    print("Computer Won!!")
elif user_choice == 'Scissors' and computer_choice == 'Rock':
    print("Computer Won!!")
elif user_choice == 'Scissors' and computer_choice == 'Paper':
    print("You Won!!")
else:
    print("Something went wrong!!")