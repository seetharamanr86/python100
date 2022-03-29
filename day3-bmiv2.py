weight=input("Enter your weight in kgs: ")
height=input("Enter your height in meters: ")

bmi=float(weight)/float(height)**2

int_bmi = int(bmi)

print("Your bmi is "+ str(int_bmi))

if int_bmi<18.5:
    print("You are under weight")
elif int_bmi>=18.5 and int_bmi<=25:
    print("You are normal weight")
elif int_bmi>25 and int_bmi<=30:
    print("You are over weight")
elif int_bmi>30 and int_bmi<=35:
    print("You are obese")
else:
    print("You are clinically obese")