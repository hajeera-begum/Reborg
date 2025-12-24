width=0
while True:
    move()
    width+=1
    if wall_in_front():
        turn_left()
        turn_left()
        w=round(width/2)
        for i in range(w):
            move()
        put()
        done()
          
    
