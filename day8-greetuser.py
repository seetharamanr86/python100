def greet_user(name, location):
    print(f"Hello {name}")
    print(f"How is weather at {location}")

name=input("What is your name?: ")
location=input("Which location are you from?: ")

greet_user(name, location)

#greet_user(location="Virginia", name="Rahul")
#greet_user(name="Rahul", location="Virginia")