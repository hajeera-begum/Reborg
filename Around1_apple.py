move()
while not at_goal():
    if front_is_clear():
        if object_here():
            take()
    if wall_in_front():
        turn_left()
        if object_here():
            take()
    move()
