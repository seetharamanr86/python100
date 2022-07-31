from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(-30, 280)
        self.hideturtle()
        self.running_score = 0
        self.write(f'Screen : {self.running_score}', move=False, align = 'left', font= ('Arial', 10, 'normal'))

    def score_update(self, running_score):
        self.reset()
        self.color('white')
        self.penup()
        self.goto(-30, 280)
        self.hideturtle()
        self.running_score = running_score
        self.write(f'Screen : {self.running_score}', move=False, align = 'left', font= ('Arial',10, 'normal'))

    def gameover(self):
        self.goto(0, 0)
        self.write(f'Game Over!!!   ', move=False, align='left', font=('Arial', 10, 'normal'))