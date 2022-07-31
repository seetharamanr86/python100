import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    sum=0
    for x in cards:
        sum=sum+x

    if len(cards)==2:
        if 11 in cards:
            if 10 in cards:
                sum=0
                return sum

    if 11 in cards:
        if sum>21:
            sum = 0
            for x in range(len(cards)):
                if cards[x] == 11:
                    cards[x] = 1
            for x in cards:
                sum = sum + x

    return sum

def compare(user_score,computer_score):
    print(user_cards)
    print(computer_cards)
    print("User Score is: " + str(user_score))
    print("Computer Score is: " + str(computer_score))
    if user_score == computer_score:
        print("DRAW")
        exit()
    elif user_score > computer_score:
        print("USER WINS")
        exit()
    elif user_score < computer_score:
        print("COMPUTER WINS")
        exit()

def check(user_score,computer_score):
    if user_score == 0 and computer_score == 0:
        print("DRAW")
        exit()
    elif user_score == 0:
        print ("USER WINS")
        exit()
    elif computer_score == 0:
        print ("COMPUTER WINS")
        exit()
    elif user_score > 21:
        print ("COMPUTER WINS")
        exit()
    elif computer_score > 21:
        print ("USER WINS")
        exit()

def process():
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    check(user_score, computer_score)

user_cards = []
computer_cards = []

user_cards.append(deal_card())
user_cards.append(deal_card())
computer_cards.append(deal_card())
computer_cards.append(deal_card())

print(user_cards)
# print(computer_cards)


user_score=calculate_score(user_cards)
computer_score=calculate_score(computer_cards)

check(user_score,computer_score)

user_choice='yes'

while user_choice=='yes':
    user_choice = input("Do you want to draw card? yes or no: ")
    if user_choice == 'yes':
        user_cards.append(deal_card())
        print(user_cards)
        print(computer_cards)
    process()
    if computer_score < 17:
        computer_cards.append(deal_card())
        print(user_cards)
        print(computer_cards)
    process()

compare(user_score,computer_score)



