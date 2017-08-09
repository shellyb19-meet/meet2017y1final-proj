#settings 

import turtle
import random
turtle.tracer(1,0)

x_size=800
y_size=700
turtle.setup(x_size,y_size)
SQUARE_SIZE=20
farmer = turtle.clone()
##farmer_xsize = 100
##farmer_ysize = 100
ground = -750

good_food_names = ["apple", "banana", "strawberry", "orange", "grape"]
good_food_clones = []
bad_food_names = ["bad_apple", "bad_banana", "bad_strawberry", "bad_orange", "bad_grape"]
bad_food_clones = []
other_names = ["gun", "handbomb", "rocket", "soldier"]
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
   obj2 = turtle.clone()
   shape_name = bad_food_names[i] + ".gif"
   turtle.register_shape(shape_name)
   obj2.shape(shape_name)
   bad_food_clones.append(obj2)

# make other_clones list
for i in range(len(other_names)):
   obj2 = turtle.clone()
   shape_name = other_names[i] + ".gif"
   turtle.register_shape(shape_name)
   obj2.shape(shape_name)
   other_clones.append(obj2)

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
    chosen_fallen_item.hideturtle()
    print("You have collected food!")

def touching_ground ():
    chosen_Fallen_item.hideturtle|()
    print("You missed food!")
