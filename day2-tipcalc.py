
print("Welcome to the TIP Calculator!!")

bill_amt = input("What is your total bill amount :$")

tip = input("How much % tip do you want to pay? 12, 14 or 18: ")

total_person = input("How many persons to share the bill? ")

tip_percent = int(tip)/100

tip_value = int(bill_amt) * tip_percent

bill_with_tip = int(bill_amt)+tip_value

bill_per_person = round((bill_with_tip / int(total_person)),2)

print(f"Each person should share bill ${bill_per_person} for bill value ${bill_amt} and tip {tip}%")



