from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

myscreen = Screen()
myscoreboard = Scoreboard()

myscreen.setup(width = 800, height = 600)
myscreen.bgcolor('black')
myscreen.title('Pong')

position1 = (380, 0)
position2 = (-380, 0)

right_paddle = Paddle(position1)
left_paddle = Paddle(position2)

myball = Ball()

myscreen.listen()
myscreen.tracer(0)

myscreen.onkey(right_paddle.move_paddle_up, 'Up')
myscreen.onkey(right_paddle.move_paddle_down, 'Down')

myscreen.onkey(left_paddle.move_paddle_up, 'w')
myscreen.onkey(left_paddle.move_paddle_down, 's')

game = True

l_score = 0
r_score = 0

while game:
    time.sleep(myball.move_speed)
    myscreen.update()
    myball.ball_move()

    if myball.ycor() > 280 or myball.ycor() < -280:
        myball.ball_bounce_y()

    if myball.xcor() > 320 and myball.distance(right_paddle) < 50 or myball.xcor() < -320 and myball.distance(left_paddle) < 50:
        myball.ball_bounce_x()

    if myball.xcor() > 380:
        myball.reset_position()
        myball.ball_bounce_x()
        l_score = l_score + 10
        print('l_score is:' + str(l_score))
        myscoreboard.update_score(l_score, r_score)

    if myball.xcor() < -380:
        myball.reset_position()
        myball.ball_bounce_x()
        r_score = r_score + 10
        print('r_score is:' + str(r_score))
        myscoreboard.update_score(l_score, r_score)

myscreen.exitonclick()