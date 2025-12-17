count_steps=0
def turn_back():
    centre=round(count_steps/2)
    for i in range(centre):
        move()
    put()
    done()
while True:
    move()
    count_steps+=1
    if wall_in_front():
        turn_left()
        turn_left()
        turn_back()
