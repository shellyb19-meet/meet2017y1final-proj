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

    RIGHT_EDGE = 200
    LEFT_EDGE = -200
    RIGHT_EDGE = 380
    LEFT_EDGE = -380

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


#changing shape
#a = the names of all the items
happy = turtle.clone()
sad = turtle.clone()
happy.register_shape("happy_face.gif")
sad.register_shape("sad_face.gif")

a = ["apple.gif", "banana.gif", "strawberry.gif", "orange.gif", "grape.gif"]

a.sort()

clones_list = []
for n in range(len(a)):
    obj = turtle.clone()
    clones_list.append(obj)
    turtle.register_shape(a[n])
    obj.shape(a[n])



##good_food_turtles
##good_food_names
##
##bad_food_turtles
##bad_food_names
##
##other_stuff_turtles
##other_stuff_names

#good food
for good_food in clones_list:
    if good_food.pos() == farmer.pos():
        score = score + 1
        happy.stamp()
        print("Yay!")

#bad food
for bad_food in clones_list:
    if bad_food.pos() == farmer.pos():
        score = score - 1
        sad.stamp()
        print("Oh no!")

#hit the edge
for good_food in clones_list:
    if good_food.pos()>=RIGHT_EDGE:
        score = score - 1
        sad.stamp()
        print("Oh no!")

#other stuff
for other_stuff in clones_list:
    if other_stuff.pos() == farmer.pos():
        print("Game over!")
        quit()

