import turtle
turtle.tracer(1,0)

x_size=800
y_size=700
turtle.setup(x_size,y_size)
SQUARE_SIZE=20

def farmer():
    turtle.hideturtle()
    turtle.register_shape("farmer.gif")
    farmer=turtle.clone()
    farmer.shape("farmer.gif")

    farmer.penup()
    farmer.goto(0,-320)
    farmer.showturtle()

    LEFT_ARROW="Left"
    RIGHT_ARROW="Right"
    LEFT=0
    RIGHT=1
    direction=LEFT

    RIGHT_EDGE = 400
    LEFT_EDGE = -400
    RIGHT_EDGE = 350
    LEFT_EDGE = -350

    def left():
        
        global direction
        direction=LEFT
        move_farmer()
        print('you moved the farmer left')
        print(farmer.pos())
        
    def right():
        
        global direction
        direction=RIGHT
        move_farmer()
        print('you moved the farmer right')
        print(farmer.pos())

    def move_farmer():
        x=farmer.pos()[0]
        y=farmer.pos()[1]
        
        if direction == LEFT:
            farmer.goto(x-SQUARE_SIZE,y)
        elif direction == RIGHT:
            farmer.goto(x+SQUARE_SIZE,y)
        if x>RIGHT_EDGE:
            quit()
        elif x<LEFT_EDGE:
            quit()

    turtle.onkeypress(left,LEFT_ARROW)
    turtle.onkeypress(right,RIGHT_ARROW)
    turtle.listen()



=======
#changing shape
happy = turtle.clone()
sad = turtle.clone()
happy.register_shape("happy_face.gif")
sad.register_shape("sad_face.gif")

a = ["apple.gif", "banana.gif", "strawberry.gif", "orange.gif", "grape.gif"]
b = ["bad_apple.gif", "bad_banana.gif", "bad_strawberry.gif", "bad_orange.gif"
     , "bad_grape.gif"]
c = ["gun.gif", "handbomb.gif", "rocket.gif", "soldjier.gif"]

a.sort()
b.sort()
c.sort()

bad_clones_list = []
good_clones_list = []
war_clones_list = []

for n in range(len(a)):
    good_obj = turtle.clone()
    good_clones_list.append(good_obj)
    turtle.register_shape(a[n])
    good_obj.shape(a[n])

for x in range(len(b)):
    bad_obj = turtle.clone()
    bad_clones_list.append(bad_obj)
    turtle.register_shape(b[x])
    bad_obj.shape(b[x])

for y in range(len(c)):
    war_obj = turtle.clone()
    war_clones_list.append(war_obj)
    turtle.register_shape(c[y])
    war_obj.shape(c[y])


#good food
for good_food in good_clones_list:
    if good_food.pos() == farmer.pos():
        score = score + 1
        happy.stamp()
        print("Yay!")

#bad food
for bad_food in bad_clones_list:
    if bad_food.pos() == farmer.pos():
        score = score - 1
        sad.stamp()
        print("Oh no!")

#hit the edge
for good_food in good_clones_list:
    if good_food.pos()>=RIGHT_EDGE:
        score = score - 1
        sad.stamp()
        print("Oh no!")

#other stuff
for other_stuff in war_clones_list:
    if other_stuff.pos() == farmer.pos():
        print("Game over!")
        quit()


