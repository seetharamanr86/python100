print("Welcome to Leap Year Checker!")

year=int(input("Enter the year to check if it is leap: "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("It is a leap year!")
        else:
            print("It is not a leap year!")
    else:
        print("It is a leap year!")
else:
    print("It is not a leap year!")