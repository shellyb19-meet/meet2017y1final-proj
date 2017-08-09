#settings 

import turtle
import random
turtle.tracer(1,0)
score_frame = turte.clone()
score_frame.shape("rectangle")
score_frame.color("orange")

score = 0
x_size=800
y_size=700
turtle.setup(x_size,y_size)
SQUARE_SIZE=20
farmer = turtle.clone()
farmer_xsize = 50
farmer_ysize = 50
farmer_xpos = farmer.pos()[0]
farmer_ypos = farmer.pos()[1]
farmer_xpos_list = [farmer_xpos, farmer_xpos + farmer_xsize\2, farmer_xpos - farmer_xsize\2]
farmer_ypos_list = [farmer_ypos, farmer_ypos + farmer_ysize\2, farmer_ypos - farmer_ysize\2]
ground = -750

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
happy.register_shape("happy_face.gif")
sad.register_shape("sad_face.gif")
happy.penup()
happy.goto(-350,300)
happy.hideturtle()
sad.penup()
sad.goto(-350,300)
sad.hideturtle()

# ---------------------------------------------------------------------------------------
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
        
        
    def right():
        
        global direction
        direction=RIGHT
        move_farmer()
        print('you moved the farmer right')
        

    def move_farmer():
        x=farmer.pos()[0]
        y=farmer.pos()[1]
        
        if direction == LEFT:
            farmer.goto(x-SQUARE_SIZE,y)
            farmer_xpos = farmer.pos()[0]
            farmer_ypos = farmer.pos()[1]
            farmer_xpos_list = [farmer_xpos, farmer_xpos + farmer_xsize\2, farmer_xpos - farmer_xsize\2]
            farmer_ypos_list = [farmer_ypos, farmer_ypos + farmer_ysize\2, farmer_ypos - farmer_ysize\2]
        elif direction == RIGHT:
            farmer.goto(x+SQUARE_SIZE,y)
            farmer_xpos = farmer.pos()[0]
            farmer_ypos = farmer.pos()[1]
            farmer_xpos_list = [farmer_xpos, farmer_xpos + farmer_xsize\2, farmer_xpos - farmer_xsize\2]
            farmer_ypos_list = [farmer_ypos, farmer_ypos + farmer_ysize\2, farmer_ypos - farmer_ysize\2]
        if x>RIGHT_EDGE:
            quit()
        elif x<LEFT_EDGE:
            quit()

    turtle.onkeypress(left,LEFT_ARROW)
    turtle.onkeypress(right,RIGHT_ARROW)
    turtle.listen()
# ---------------------------------------------------------------------------------------

"""
1. Randomize falling items, and then randomize the x-position (with a constant y)
    so that they will start off in the sky
2. Apply "gravity" to the falling objects until they touch EITHER the farmer OR the ground
    2a. If it touches the farmer: ###
    2b. If it touches the ground: ###
"""


    
##def rain():
##    upto = len(fallen_items)
##    chosen_fallen_item_num = random_randint(0,upto)
##    chosen_fallen_item = fallen_items_list.index(chosen_fallen_item_num)
##
##    rx = random.randint(size_x - 0.5*size_x, (size_x - 0.5*size_x)*-1)
##    chosen_fallen_item.goto(rx, size_y - 0.5*size_y)
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
    if chosen_fallen_item in good_food_clones:
        chosen_fallen_item.hideturtle()
        print("You have collected food!")
        score = score + 1
        score()
        happy.showturtle()
    elif chosen_fallen_item in bad_food_clones:
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
    if chosen_fallen_item in good_food_clones:
        chosen_fallen_item.hideturtle|()
        print("You have missed food!")
        sad.showturtle()
    elif chosen_fallen_item in bad_food_clones:
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

     
   
