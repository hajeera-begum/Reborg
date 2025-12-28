def turn_right():
    for i in range(3):
        turn_left()
move()
turn_right()
wall_count=4
while not wall_count==0:
    move()
    if not wall_on_right():
        turn_right()
        build_wall()
        turn_left()
    elif wall_in_front():
        turn_left()
        wall_count-=1
move()
move()
