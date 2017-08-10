#settings 

import turtle
import random
turtle.tracer(1,0)
score = 0
x_size=800
y_size=700
turtle.setup(x_size,y_size)
SQUARE_SIZE=20

#background
background = turtle.clone()
turtle.register_shape("background.gif")
background.shape("background.gif")
background.penup()
background.goto(0,0)
background.stamp()
background.hideturtle()

#farmer
farmer = turtle.clone()
turtle.register_shape("farmer.gif")
farmer.shape("farmer.gif")
farmer_xsize = 50
farmer_ysize = 50
farmer_xpos = farmer.pos()[0]
farmer_ypos = farmer.pos()[1]
farmer_xpos_list = [farmer_xpos, farmer_xpos + farmer_xsize/2, farmer_xpos - farmer_xsize/2]
farmer_ypos_list = [farmer_ypos, farmer_ypos + farmer_ysize/2, farmer_ypos - farmer_ysize/2]
ground = -650

farmer.penup()
farmer.goto(0,-320)
farmer.showturtle()

good_food_names = ["apple", "banana", "strawberry", "orange", "grape"]
good_food_clones = []
bad_food_names = ["bad_apple", "bad_banana", "bad_strawberry", "bad_orange", "bad_grape"]
bad_food_clones = []
other_names = ["gun", "handbomb", "rocket"]
other_clones = []

turtle.hideturtle()
# make good_food_clones list
for i in range(len(good_food_names)):
    obj = turtle.clone()
    shape_name = good_food_names[i] + ".gif"
    turtle.register_shape(shape_name)
    obj.shape(shape_name)
    good_food_clones.append(obj)

# make bad_food_clones list
for i in range(len(bad_food_names)):
   obj1 = turtle.clone()
   shape_name = bad_food_names[i] + ".gif"
   turtle.register_shape(shape_name)
   obj1.shape(shape_name)
   bad_food_clones.append(obj1)

# make other_clones list
for i in range(len(other_names)):
   obj2 = turtle.clone()
   shape_name = other_names[i] + ".gif"
   turtle.register_shape(shape_name)
   obj2.shape(shape_name)
   other_clones.append(obj2)

#make face
happy = turtle.clone()
sad = turtle.clone()
turtle.register_shape("happy_face.gif")
turtle.register_shape("sad_face.gif")
happy.shape("happy_face.gif")
sad.shape("sad_face.gif")
happy.penup()
happy.goto()
happy.hideturtle()
sad.penup()
sad.goto()
sad.hideturtle()

# --------------------------------------------------------------------------------------
LEFT_ARROW = "Left"
RIGHT_ARROW = "Right"

LEFT = 0 
RIGHT = 1

RIGHT_EDGE = 200
LEFT_EDGE = -200
RIGHT_EDGE = 380
LEFT_EDGE = -380
direction = LEFT

def left():
    global direction
    direction=LEFT
##    move_farmer()
##    if direction == LEFT:
##        farmer.goto(x-SQUARE_SIZE,y)
##        print('you moved the farmer laft')
##        print(farmer.pos())
    
def right():
    global direction
    direction=RIGHT
##    move_farmer()
##    if direction == RIGHT:
##        farmer.goto(x+SQUARE_SIZE,y)
##        print('you moved the farmer right')
##        print(farmer.pos())

turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

def move_farmer():
    x=farmer.pos()[0]
    y=farmer.pos()[1]
    
    if direction == LEFT:
        farmer.goto(x-SQUARE_SIZE,y)
    else:
        farmer.goto(x+SQUARE_SIZE,y)

    if x>RIGHT_EDGE:
        quit()
    if x<LEFT_EDGE:
        quit()


move_farmer()
##LEFT_ARROW="Left"
##RIGHT_ARROW="Right"
##LEFT=0
##RIGHT=1
##direction=LEFT
##def left():
##    global direction
##    direction=LEFT
##    move_farmer()
##    print('you moved the farmer left')
##        
##        
##def right():
##    global direction
##    direction=RIGHT
##    move_farmer()
##    print('you moved the farmer right')
##        
##
##def move_farmer():
##    global farmer_xpos_list
##    global farmer_ypos_list
##    global farmer_xpos
##    global farmer_ypos
##    
##    x=farmer.pos()[0]
##    y=farmer.pos()[1]
##        
##    if direction == LEFT:
##        farmer.goto(x-SQUARE_SIZE,y)
##        farmer_xpos = farmer.pos()[0]
##        farmer_ypos = farmer.pos()[1]
##        farmer_xpos_list = [farmer_xpos, farmer_xpos + farmer_xsize/2, farmer_xpos - (farmer_xsize/2)]
##        farmer_ypos_list = [farmer_ypos, farmer_ypos + farmer_ysize/2, farmer_ypos - (farmer_ysize/2)]
##    elif direction == RIGHT:
##        farmer.goto(x+SQUARE_SIZE,y)
##        farmer_xpos = farmer.pos()[0]
##        farmer_ypos = farmer.pos()[1]
##        farmer_xpos_list = [farmer_xpos, farmer_xpos + farmer_xsize/2, farmer_xpos - farmer_xsize/2]
##        farmer_ypos_list = [farmer_ypos, farmer_ypos + farmer_ysize/2, farmer_ypos - farmer_ysize/2]
##        
##
##turtle.onkeypress(left,LEFT_ARROW)
##turtle.onkeypress(right,RIGHT_ARROW)
##turtle.listen()


   
# ---------------------------------------------------------------------------------------

"""
1. Randomize falling items, and then randomize the x-position (with a constant y)
    so that they will start off in the sky
2. Apply "gravity" to the falling objects until they touch EITHER the farmer OR the ground
    2a. If it touches the farmer: ###
    2b. If it touches the ground: ###
"""
def set_up_sky_stuff():
    # choose which items are going to fall
    chosen_fallen_item = []
    max_falling_items = 1
    for n in range(max_falling_items):
        r = random.randint(1, 3)
        if r == 1: # get a good food
            good_i = random.randint(0, len(good_food_names) - 1)
            good_food = good_food_clones[good_i]
            chosen_fallen_item.append(good_food)
        elif r == 2: # get a bad food
            bad_i = random.randint(0, len(bad_food_names) - 1)
            bad_food = bad_food_clones[bad_i]
            chosen_fallen_item.append(bad_food)
        else: # get a war item
            other_i = random.randint(0, len(other_names) - 1)
            other = other_clones[other_i]
            chosen_fallen_item.append(other)

def make_food():
    min_x=-int(size_x/2/square_size)+1
    max_x=int(size_x/2/square_size)-1
    food_x=random.randint(min_x,max_x)*square_size
    food_y=350
    chosen_fallen_item.goto(food_x,food_y)
    food_pos.append((food_x,food_y))
    f= chosen_fallen_item.stamp()
    food_stamp.append (f)
    while not chosen_fallen_item_xpos in farmer_xpos_list and not chosen_fallen_item_ypos in farmer_ypos_list :
        chosen_fallen_item_xpos =    chosen_fallen_item.pos()[0]
        chosen_fallen_item_ypos = chosen_fallen_item.pos()[1]
        chosen_fallen_item_ypos += -20
        chosen_fallen_item.goto(chosen_fallen_item_xpos, chosen_fallen_item_ypos)
        if chosen_fallen_item_ypos <= ground:
            touching_ground()
        if chosen_fallen_item_xpos in farmer_xpos_list and not chosen_fallen_item_ypos in farmer_ypos_list :
            touching_farmer()


    

#gravity
    while not chosen_fallen_item_xpos in farmer_xpos_list and not chosen_fallen_item_ypos in farmer_ypos_list :
        chosen_fallen_item_xpos =    chosen_fallen_item.pos()[0]
        chosen_fallen_item_ypos = chosen_fallen_item.pos()[1]
        chosen_fallen_item_ypos += -20
        chosen_fallen_item.goto(chosen_fallen_item_xpos, chosen_fallen_item_ypos)
        if chosen_fallen_item_ypos <= ground:
            touching_ground()
        if chosen_fallen_item_xpos in farmer_xpos_list and not chosen_fallen_item_ypos in farmer_ypos_list :
            touching_farmer()

def touching_farmer ():
    if chosen_fallen_item in good_food_names:
        chosen_fallen_item.hideturtle()
        print("You have collected food!")
        score = score + 1
        score()
        happy.showturtle()
    elif chosen_fallen_item in bad_food_names:
        chosen_fallen_item.hideturtle()
        print("You have collected the worng food!")
        score = score - 1
        score()
        sad.showturtle()
    else:
        chosen_fallen_item.hideturtle()
        print("You have collected deadly item!")
        sad.showturtle()
        quit()        
        

def touching_ground ():
    if chosen_fallen_item in good_food_names:
        chosen_fallen_item.hideturtle|()
        print("You have missed food!")
        sad.showturtle()
    elif chosen_fallen_item in bad_food_names:
        chosen_fallen_item.hideturtle()
    else:
        chosen_fallen_item.hideturtle()

def score():
    score.turtle.clone()
    score.color("White")
    score.hideturtle()
    score.pu()
    score.goto(300,325)
    score.write("score:" + str(score), font=("Aerial",24, "normal") )
    if score < 0:
        quit()

     
   
