
number=int(input("Enter the number to check for prime: "))

def prime_checker(number):
    if number == 0 or number == 1:
        print(f"The number {number} is not prime!")
        quit()
    elif number == 2:
        print(f"The number {number} is prime!")
        quit()
    else:
        for i in range(2,number-1):
            factor=number%i
            if factor==0:
                print(f"The number {number} is not prime!")
                quit()
        print(f"The number {number} is a prime!")

prime_checker(number)

