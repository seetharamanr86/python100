from day14_extra_gamedata import data
from os import system
import random

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def picker():
    option=random.choice(data)
    return(option)

def user_input():
    user_choice=input("Pick your choice: A or B ")
    return(user_choice)

def picker_validate(option1, option2):
    while option1 == option2:
        option2 = picker()
    return (option2)

def real_choice(option1, option2):
    if option1['follower_count'] > option2['follower_count']:
        return ('a')
    else:
        return ('b')

score = 0

flag='pass'

option1 = picker()
option2 = picker()
option2 = picker_validate(option1, option2)
print(logo)

while flag == 'pass':
    print("Your current score is : " + str(score))
    option1 = option2
    option2 = picker()
    option2 = picker_validate(option1, option2)
    true_choice = real_choice(option1, option2)
    print(f"Compare A: {option1['name']}, {option1['description']}, from {option1['country']}")
    print(vs)
    print(f"Against B: {option2['name']}, {option2['description']}, from {option2['country']}")
    user_choice = input("Pick your choice: A or B ").lower()
    if true_choice == user_choice:
        score = score + 1
        flag = 'pass'
        system('clear')
        print(logo)
        print("Your choice is right!!")
    else:
        flag = 'fail'
        system('clear')
        print(logo)
        print("Sorry, your choice is wrong!!")

print("Your final score is : " + str(score))






