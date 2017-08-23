#settings 

import turtle
import random
##turtle.tracer(1,0)
scorevalue = 0
x_size=800
y_size=700
turtle.setup(x_size,y_size)
SQUARE_SIZE=20

background = turtle.clone()
turtle.register_shape("background.gif")
background.shape("background.gif")
background.penup()
background.goto(0,0)
background.stamp()
background.hideturtle()

turtle.register_shape("farmer.gif")
farmer=turtle.clone()
farmer.shape("farmer.gif")
farmer.pu()
farmer_xsize = 50
farmer_ysize = 50
farmer_xpos = farmer.pos()[0]
farmer_ypos = farmer.pos()[1]
farmer_xpos_list = [farmer_xpos, farmer_xpos + farmer_xsize/2, farmer_xpos - farmer_xsize/2]
farmer_ypos_list = [farmer_ypos, farmer_ypos + farmer_ysize/2, farmer_ypos - farmer_ysize/2]
ground = -650

good_food_names = ["apple", "banana", "strawberry", "orange", "grape"]
good_food_clones = []
bad_food_names = ["bad_apple", "bad_banana", "bad_strawberry", "bad_orange"]
bad_food_clones = []
other_names = ["gun", "handbomb", "rocket"]
other_clones = []
turtle.penup()
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
happy.shape('happy_face.gif')
turtle.register_shape("sad_face.gif")
sad.shape('sad_face.gif')
happy.penup()
happy.goto(-x_size/2+50,y_size/2 - 50)
happy.hideturtle()
sad.penup()
sad.goto(-x_size/2+50,y_size/2 - 50)
sad.hideturtle()

LEFT_ARROW="Left"
RIGHT_ARROW="Right"
LEFT=0
RIGHT=1
direction=LEFT
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
    global farmer_xpos_list
    global farmer_ypos_list
    global farmer_xpos
    global farmer_ypos
    
    x=farmer.pos()[0]
    y=farmer.pos()[1]
        
    if direction == LEFT:
        farmer.goto(x-SQUARE_SIZE*5,y)
        farmer_xpos = farmer.pos()[0]
        farmer_ypos = farmer.pos()[1]
        farmer_xpos_list = [farmer_xpos, farmer_xpos + SQUARE_SIZE, farmer_xpos + 2*SQUARE_SIZE, farmer_xpos - SQUARE_SIZE, farmer_xpos - 2*SQUARE_SIZE]
        farmer_ypos_list = [farmer_ypos, farmer_ypos + SQUARE_SIZE, farmer_ypos + 2*SQUARE_SIZE, farmer_ypos - SQUARE_SIZE, farmer_ypos - 2*SQUARE_SIZE]
    elif direction == RIGHT:
        farmer.goto(x+SQUARE_SIZE*5,y)
        farmer_xpos = farmer.pos()[0]
        farmer_ypos = farmer.pos()[1]
        farmer_xpos_list = [farmer_xpos, farmer_xpos + farmer_xsize/2, farmer_xpos - farmer_xsize/2]
        farmer_ypos_list = [farmer_ypos, farmer_ypos + farmer_ysize/2, farmer_ypos - farmer_ysize/2]
        

scoreboard=turtle.clone()
scoreboard.color("Black")
scoreboard.hideturtle()
scoreboard.pu()
scoreboard.goto(x_size/2 - 150,y_size/2 - 50)
def score():
    scoreboard.clear()
    scoreboard.write("score:" + str(scorevalue), font=("Aerial",24, "normal") )
    if scorevalue < 0:
        quit()
score()


turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()
chosen_fallen_item = []
def set_up_sky_stuff():
    # choose which items are going to fall
    max_falling_items = 1
    for n in range(max_falling_items):
        r = random.randint(1, 10)
        if r < 9: # get a good food
            good_i = random.randint(0, len(good_food_names) - 1)
            good_food = good_food_clones[good_i]
            chosen_fallen_item.append(good_food)
        elif r == 9: # get a bad food
            bad_i = random.randint(0, len(bad_food_names) - 1)
            bad_food = bad_food_clones[bad_i]
            chosen_fallen_item.append(bad_food)
        else: # get a war item
            other_i = random.randint(0, len(other_names) - 1)
            other = other_clones[other_i]
            chosen_fallen_item.append(other)

def make_food():
    set_up_sky_stuff()
    min_x=-int(x_size/2/SQUARE_SIZE)+1
    max_x=int(x_size/2/SQUARE_SIZE)-1
    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=350
    temp_list = chosen_fallen_item[:]
    print(temp_list)
    for chosen_fall_item in temp_list:
        chosen_fall_item.goto(food_x,food_y)
        chosen_fall_item.showturtle()
        chosen_fallen_item_xpos = food_x
        chosen_fallen_item_ypos = food_y
        #food_pos.append((food_x,food_y))
        #f= chosen_fall_item.stamp()
        #food_stamp.append (f)
        while not chosen_fallen_item_xpos in farmer_xpos_list and not chosen_fallen_item_ypos in farmer_ypos_list :
            chosen_fallen_item_xpos =    chosen_fall_item.pos()[0]
            chosen_fallen_item_ypos = chosen_fall_item.pos()[1]
            chosen_fallen_item_ypos += -20
            chosen_fall_item.goto(chosen_fallen_item_xpos, chosen_fallen_item_ypos)
            if chosen_fallen_item_ypos <= ground:
                touching_ground(chosen_fall_item)
                break
            elif chosen_fallen_item_xpos in farmer_xpos_list and not chosen_fallen_item_ypos in farmer_ypos_list :
                touching_farmer(chosen_fall_item)
                break
    turtle.ontimer(make_food,200)
            
def touching_farmer (chosen_fall_item):
    global scorevalue, chosen_fallen_item
    print(chosen_fallen_item)
    print(chosen_fall_item)
    if chosen_fall_item in good_food_clones:
        chosen_fall_item.hideturtle()
        ind = chosen_fallen_item.index(chosen_fall_item)
        chosen_fallen_item.pop(ind)
        print("You have collected food!")
        scorevalue = scorevalue + 1
        score()
        happy.showturtle()
        sad.hideturtle()
    elif chosen_fall_item in bad_food_clones:
        chosen_fall_item.hideturtle()
        ind = chosen_fallen_item.index(chosen_fall_item)
        chosen_fallen_item.pop(ind)
        print("You have collected the worng food!")
        scorevalue = scorevalue - 1
        score()
        sad.showturtle()
        happy.hideturtle()
    else:
        chosen_fall_item.hideturtle()
        ind = chosen_fallen_item.index(chosen_fall_item)
        chosen_fallen_item.pop(ind)
        print("You have collected deadly item!")
        sad.showturtle()
        happy.hideturtle()
        quit()        
        

def touching_ground (chosen_fall_item):
    global scorevalue, chosen_fallen_item
    print(chosen_fallen_item)
    print(chosen_fall_item)
    if chosen_fall_item in good_food_clones:
        chosen_fall_item.hideturtle()
        ind = chosen_fallen_item.index(chosen_fall_item)
        chosen_fallen_item.pop(ind)
        print("You have missed food!")
        sad.showturtle()
    elif chosen_fall_item in bad_food_clones:
        chosen_fall_item.hideturtle()
        ind = chosen_fallen_item.index(chosen_fall_item)
        chosen_fallen_item.pop(ind)
    else:
        chosen_fall_item.hideturtle()
        ind = chosen_fallen_item.index(chosen_fall_item)
        chosen_fallen_item.pop(ind)


make_food()
