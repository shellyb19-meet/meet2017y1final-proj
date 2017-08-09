#settings 

import turtle
import random
turtle.tracer(1,0)

x_size=800
y_size=700
turtle.setup(x_size,y_size)
SQUARE_SIZE=20
farmer = turtle.clone()
farmer_xsize = 100
farmer_ysize = 100
x_size = 800
y_size = 700
turtle.setup(x_size, y_size)
ground = -750

a = ["apple", "banana", "strawberry", "orange", "grape"]
b = ["bad_apple", "bad_banana", "bad_strawberry", "bad_orange"
     , "bad_grape"]
c = ["gun", "handbomb", "rocket", "soldier"]
fallen_items = bad_food_list + good_food_list 
farmer_xpos =farmer.pos()[0]
farmer_ypos = farmer.pos()[1]
farmer_xpos_list = [farmer_xpos, farmer_xpos + farmer_xsize, farmer_xpos - farmer_xsize]
farmer_ypos_list = [farmer_ypos, farmer_ypos + farmer_ysize, farmer_ypos - farmer_ysize]
