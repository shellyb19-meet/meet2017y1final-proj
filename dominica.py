import random
import turtle

food = turtle.clone()
 
size_x = 800
size_y = 700
turtle.setup(size_x,size_y)
square_size = 20
food_list = ['a','b','c','d','e']
for n in range(22):
    random_index = random.randint(0, len(food_list) - 1)
    print(food_list[random_index])
    

def make_food():
    min_x=int(size_x/2/square_size)+1
    max_x=int(size_x/2/square_size)-1
    food_x=random.randint(min_x,max_x)*square_size
    food.goto(food_x)
    food_pos.append((food_x,food_y))
    f= food.stamp()
    food_stamp.append (f)
    
##for i in range(len(names)):
##    print(names[i])
