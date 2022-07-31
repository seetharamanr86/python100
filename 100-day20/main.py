from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

myscreen = Screen()
myscreen.setup(width = 600, height = 600)
myscreen.bgcolor('black')

myscreen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

myscreen.listen()

myscreen.onkey(snake.up, 'Up')
myscreen.onkey(snake.down, 'Down')
myscreen.onkey(snake.left, 'Left')
myscreen.onkey(snake.right, 'Right')

game = True

running_score = 0

while game:
    myscreen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        running_score = running_score+10
        scoreboard.score_update(running_score)

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game = False
        scoreboard.gameover()

    for instance in snake.turtle_instances[1:]:
        if snake.head.distance(instance) < 10:
            game = False
            scoreboard.gameover()








myscreen.exitonclick()