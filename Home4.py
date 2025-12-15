def jump():
    move()
    move()
    move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def forward():
    jump()
    turn_left()
    jump()
    turn_right()
    move()
    turn_right()
​
for i in range(3):
    forward()
                   
jump()
turn_left()
jump()
