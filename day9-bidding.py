import os
bid_dict ={}

bidder_available = "yes"
bid_winner=""
bid_winner_value=0

def bid_intake(bid_person, bid_value):
    bid_dict[bid_person]=bid_value

while bidder_available == "yes":
    os.system('clear')
    bid_person = input("Enter your name: ")
    bid_value = int(input("Enter bid value:$"))
    bid_intake(bid_person, bid_value)
    bidder_available = input("Are there additional bidders available to continue? yes or no: ")

print(bid_dict)

for item in bid_dict:
    if bid_dict[item] > bid_winner_value:
        bid_winner=item

print(f"The winner of the bid is {bid_winner}")