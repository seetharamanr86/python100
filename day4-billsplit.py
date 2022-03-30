import random

names=input("Provide a list of folks who wants to pay for lunch, separated by comma and space: ")

names_list=names.split(", ")

random_name=random.randint(0,len(names_list)-1)

print(f"Bill will be paid by {names_list[random_name]}")