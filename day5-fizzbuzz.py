# divisible by 3=fizz, 5=buzz, 3&5 = fizzbuzz upto 100

for number in range(1,101):
    if number%3 ==0 and number%5 ==0:
        print("fizzbuzz")
    elif number%3 ==0:
        print("fizz")
    elif number%5 ==0:
        print("buzz")
    else:
        print(number)
