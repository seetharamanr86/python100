from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.pendown()
my_turtle.pensize(2)
my_turtle.speed(25)

my_turtle.shape()

colors = ["red", "green", "blue", "black", "brown"]

for i in range(0,360, 15):
    my_turtle.color(random.choice(colors))
    my_turtle.setheading(i)
    my_turtle.circle(100, 360)

my_screen = Screen()
my_screen.exitonclick()