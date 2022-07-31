from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=500, height=400)

user_color = my_screen.textinput('Your bet', 'which color turtle? ')

turtle_colors = ['red', 'blue', 'green', 'purple', 'brown', 'black']
turtle_names = ['tim', 'tom', 'john', 'brian', 'mike', 'sam']

turtle_instances = []

race = False

def turtle_setup():
    x = -230
    y = -80
    for i in range(0, 6):
        turtle_names[i] = Turtle(shape= 'turtle')
        turtle_names[i].penup()
        turtle_names[i].goto(x, y)
        y = y + 40
        turtle_names[i].color(turtle_colors[i])
        turtle_instances.append(turtle_names[i])


turtle_setup()

if user_color:
    race = True

while race:
    for t in turtle_instances:
        if t.xcor() > 230:
            if t.pencolor() == user_color:
                print(f"{user_color} turtle has Won!")
            else:
                print(f"{user_color} turtle has Lost!")
            race = False
        t.penup()
        t.forward(random.randint(0, 10))



turtle_names[0].forward(10)

my_screen.exitonclick()