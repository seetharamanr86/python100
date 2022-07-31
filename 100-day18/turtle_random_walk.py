from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_screen = Screen()

my_screen.colormode(255)

my_turtle.pendown()
my_turtle.pensize(4)
my_turtle.speed(25)

my_turtle.shape()
my_turtle.color('red')



colors = ["red", "green", "blue", "black", "brown"]

def one(my_turtle, color_choice):
    my_turtle.pencolor(color_choice)
    my_turtle.left(90)
    my_turtle.forward(10)

def two(my_turtle, color_choice):
    my_turtle.pencolor(color_choice)
    my_turtle.right(90)
    my_turtle.forward(10)

def three(my_turtle, color_choice):
    my_turtle.pencolor(color_choice)
    my_turtle.right(90)
    my_turtle.backward(10)

def four(my_turtle, color_choice):
    my_turtle.pencolor(color_choice)
    my_turtle.right(90)
    my_turtle.backward(10)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

numbers = [1, 2, 3, 4]


for i in range(1,200):
    move_choice = random.choice(numbers)
    # color_choice = random.choice(random_color)
    color_choice = random_color()
    if move_choice == 1:
        one(my_turtle, color_choice)
    elif move_choice == 2:
        two(my_turtle, color_choice)
    elif move_choice == 3:
        three(my_turtle, color_choice)
    else:
        four(my_turtle, color_choice)



my_screen.exitonclick()