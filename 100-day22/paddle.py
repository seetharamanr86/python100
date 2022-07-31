from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_paddle(self.position)

    def create_paddle(self, position):
        self.paddle = Turtle()
        self.penup()
        self.shape('square')
        self.left(90)
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.color('white')
        self.speed('fastest')
        self.position = position
        self.setposition(self.position)

    def move_paddle_up(self):
        self.setheading(90)
        self.forward(80)

    def move_paddle_down(self):
        self.setheading(270)
        self.forward(80)