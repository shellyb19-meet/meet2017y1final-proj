#settings 

import turtle
import random
turtle.tracer(1,0)
score = 0
x_size=800
y_size=700
turtle.setup(x_size,y_size)
SQUARE_SIZE=20
turtle.register_shape("farmer.gif")
farmer=turtle.clone()
farmer.shape("farmer.gif")

farmer_xsize = 50
farmer_ysize = 50
farmer_xpos = farmer.pos()[0]
farmer_ypos = farmer.pos()[1]
farmer_xpos_list = [farmer_xpos, farmer_xpos + farmer_xsize\2, farmer_xpos - farmer_xsize\2]
farmer_ypos_list = [farmer_ypos, farmer_ypos + farmer_ysize\2, farmer_ypos - farmer_ysize\2]
ground = -650

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
happy.goto()
happy.hideturtle()
sad.penup()
sad.goto()
sad.hideturtle()
