put()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while True:
    move()
    if wall_in_front():
        turn_left()
    if right_is_clear():
        turn_right()
    if object_here():
        take()
        done()
