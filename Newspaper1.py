def turn_right():
    for i in range(3):
        turn_left()
def up_down():
    turn_left()
    move()
    turn_right()
def movement():
    for i in range(2):
        move()
take("star")
for i in range(3):
    up_down()
    movement()
​
while object_here("token"):
   take("token")
​
put("star")
turn_left()
turn_left()
​
for i in range(3):
    movement()
    up_down()
