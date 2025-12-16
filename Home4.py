def jump():
    move()
    move()
    move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def L_shape():
    jump()
    turn_left()
    jump()
    turn_right()
    move()
    turn_right()
​
for _ in range(3):
    L_shape()
jump()
turn_left()
jump()
