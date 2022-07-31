from turtle import Turtle

TURTLE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.turtle_positons = [(0, 0), (-20, 0), (-40, 0)]
        self.turtle_instances = []
        self.create_snake()
        self.head = self.turtle_instances[0]

    def create_snake(self):
        for position in TURTLE_POSITIONS:
            self.add_instances(position)

    def add_instances(self, position):
        myturtle = Turtle(shape='square')
        myturtle.fillcolor('white')
        myturtle.penup()
        myturtle.goto(position)
        self.turtle_instances.append(myturtle)

    def extend(self):
        self.add_instances(self.turtle_instances[-1].position())

    def move(self):
        for instance in range(len(self.turtle_instances) - 1, 0, -1):
            x = self.turtle_instances[instance - 1].xcor()
            y = self.turtle_instances[instance - 1].ycor()
            self.turtle_instances[instance].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
