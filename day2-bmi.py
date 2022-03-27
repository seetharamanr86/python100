weight=input("Enter your weight in kgs: ")
height=input("Enter your height in meters: ")

bmi=float(weight)/float(height)**2

int_bmi = int(bmi)

print("Your bmi is "+ str(int_bmi))