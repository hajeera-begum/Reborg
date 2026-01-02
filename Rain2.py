def turn_right():
    for i in range(3):
        turn_left()
def movement():
    for i in range(3):
        move()
movement()
turn_right()
#wall_count=6
​
#while not wall_count==0:
while True:
    move()
    if not wall_on_right() and right_is_clear():
        turn_right()
        build_wall()
        turn_left()
    elif right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
        #wall_count-=1
move()
move()
   
    
