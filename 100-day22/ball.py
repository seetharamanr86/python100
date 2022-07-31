from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def ball_move(self):
        x_val = self.xcor() + self.x_move
        y_val = self.ycor() + self.y_move
        self.goto(x_val, y_val)

    def ball_bounce_y(self):
        self.y_move *= -1

    def ball_bounce_x(self):
        self.move_speed *= 0.5
        self.x_move *= -1

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0, 0)

