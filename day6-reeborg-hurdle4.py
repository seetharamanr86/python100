def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump_block():
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear():
        move()
    turn_left()
while not at_goal():
    while front_is_clear() and not at_goal():
        move()
    if at_goal():
        done()
    jump_block()
