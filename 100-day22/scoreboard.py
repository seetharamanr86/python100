from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 280)
        self.write(self.l_score, align='center', font=('Arial', 16, 'normal'))
        self.goto(100, 280)
        self.write(self.r_score, align='center', font=('Arial', 16, 'normal'))

    def update_score(self, l_score, r_score):
        self.clear()
        self.goto(-100, 280)
        self.l_score = l_score
        self.write(self.l_score, align='center', font=('Arial', 16, 'normal'))
        self.goto(100, 280)
        self.r_score = r_score
        self.write(self.r_score, align='center', font=('Arial', 16, 'normal'))
