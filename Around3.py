#This solution works for Around 1 & Around 2 too
put()
​
def turn_right():
    turn_left()
    turn_left()
    turn_left()
​
while True:
    if wall_in_front():
        turn_left()
    if right_is_clear():
        turn_right()
    if front_is_clear():
        move()
    if object_here():
        take()
        done()
    
