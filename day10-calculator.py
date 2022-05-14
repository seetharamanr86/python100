logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print (logo)

operations=['+','-','*','/']

first_number=float(input("Enter your first number: "))
for i in range(0,len(operations)):
    print(operations[i])
selected_operation=input("Choose the operation to perform: ")
second_number=float(input("Enter your second number: "))

def add(n1, n2):
    return n1+n2;

def sub(n1, n2):
    return n1-n2;

def mul(n1, n2):
    return n1*n2;

def div(n1, n2):
    return n1/n2;

proceed='y'
result=0

while proceed=='y':
    if selected_operation == '+':
        result=add(first_number, second_number)
        print(result)
    elif selected_operation == '-':
        result = sub(first_number, second_number)
        print(result)
    elif selected_operation == '*':
        result = mul(first_number, second_number)
        print(result)
    elif selected_operation == '/':
        result = div(first_number, second_number)
        print(result)
    else:
        print ("Chosen operation is invalid!")
    proceed = input("Do you like to continue with number "+str(result)+" or exit? Type 'y' or 'n'")
    if proceed=='y':
        first_number = float(result)
        for i in range(0, len(operations)):
            print(operations[i])
        selected_operation = input("Choose the operation to perform: ")
        second_number = float(input("Enter your next number: "))



