# import colorgram
#
# colors = colorgram.extract('image.jpeg', 10)
#
# colors_list = []
#
# for i in range(0,len(colors)-1):
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#     colors_tuple = (r, g, b)
#     colors_list.append(colors_tuple)
#
# print(colors_list)

def column_builder():
    for _ in range(10):
        row_builder()
        my_turtle.backward(500)
        my_turtle.left(90)
        my_turtle.forward(50)
        my_turtle.right(90)

def row_builder():
    for _ in range(10):
        my_turtle.pendown()
        my_turtle.fillcolor(random.choice(colors_list))
        my_turtle.begin_fill()
        my_turtle.pendown()
        my_turtle.circle(10)
        my_turtle.end_fill()
        my_turtle.penup()
        my_turtle.forward(50)

colors_list = [(221, 152, 99), (12, 127, 178), (225, 165, 9), (210, 8, 58), (16, 186, 93)]

from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_screen = Screen()

my_screen.colormode(255)

my_turtle.speed(15)
my_turtle.penup()
my_turtle.goto(-200, -200)
my_turtle.hideturtle()

column_builder()

my_screen.exitonclick()

