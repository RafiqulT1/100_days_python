def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go_around_wall():
    while wall_on_right():
        if not at_goal():
            while wall_in_front():
                turn_left()
            move()

while not at_goal():
    if front_is_clear():
        move()
    elif not wall_on_right():
        turn_right()
        move()
    else:
        go_around_wall()