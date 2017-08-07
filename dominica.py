import random
import turtle

food = turtle.clone()
turtle.penup()
size_x = 800
size_y = 700
turtle.setup(size_x,size_y)
square_size = 20
food_list = ['square','triangle','circle']
food_clones = []
for n in range(len(food_list)):
##    turtle.register_shape(food_list[n])
    obj = turtle.clone()
    obj.hideturtle()
    food_clones.append(obj)
    obj.shape(food_list[n])

def set_up(food_clones):
    """
    For every clone in the list,
    it will position it at random
    positions along a horizontal line
    at y = 200
    """
    taken_x = []
    for clone in food_clones:
        min_x=int(size_x/2/square_size)+1
        max_x=int(size_x/2/square_size)-1
        print(min_x, max_x)
        food_x=random.randint(min_x,max_x)*square_size
        while food_x in taken_x:
            min_x=int(size_x/2/square_size)+1
            max_x=int(size_x/2/square_size)-1
            food_x=random.randint(min_x,max_x)*square_size
        clone.goto(food_x, 200)
        clone.showturtle()


set_up(food_clones)


def make_food(y):
    min_x=int(size_x/2/square_size)+1
    max_x=int(size_x/2/square_size)-1
    food_x=random.randint(min_x,max_x)*square_size
    food.goto(food_x)
    food_pos.append((food_x,food_y))
    f= food.stamp()
    food_stamp.append (f)
    
##for i in range(len(names)):
##    print(names[i])
