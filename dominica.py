import random
import turtle

fallen_item = turtle.clone()
turtle.penup()
size_x = 800
size_y = 700
turtle.setup(size_x,size_y)
square_size = 20

good_food_names = ["apple", "banana", "strawberry", "orange"]
good_food_clones = []
bad_food_names = ["bad_apple", "bad_banana", "bad_strawberry", "bad_orange"]
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



##
##r = random.randint(0, len(war_items) - 1)
##random_thing = war_items[r]
##rx = random.randint(-390,390)
##war_items.goto(rx, 300)
##war_items.showturtle()
##farmer_xpos = farmer.pos()[0]
##farmer_ypos = farmer.pos()[1]
##fallen_item_xpos = c.pos()[0]
##fallen_item_ypos = c.pos()[1]


##down_edge = -350
##
##while fallen_item_ypos >= down_edge:
##    fallen_item.goto(fallen_item_xpos, fallen_item_ypos - 20)






##for n in range(len(a)):
####    turtle.register_shape(food_list[n])
##    obj = turtle.clone()
##    obj.hideturtle()
##    food_clones.append(obj)
##    obj.shape(a[n])


food_clones = [turtle.clone()]

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

    taken_x = []
    for clone in chosen_fallen_item:
        # makes sure to generate random non-overlapping positions
        multiple = random.randint(0, 24)
        random_x = -370 + (30 * multiple)
        while random_x in taken_x:
            multiple = random.randint(0, 24)
            random_x = -370 + (30 * multiple)
        # make visible changes and record the random_x
        clone.showturtle()
        clone.goto(random_x, 200)
        taken_x.append(random_x)

set_up_sky_stuff()


def make_food():
    min_x=-int(size_x/2/square_size)+1
    max_x=int(size_x/2/square_size)-1
    food_x=random.randint(min_x,max_x)*square_size
    food_y=350
    chosen_fallen_item.goto(food_x,food_y)
    food_pos.append((food_x,food_y))
    f= chosen_fallen_item.stamp()
    food_stamp.append (f)


#make_food()    
##for i in range(len(names)):
##    print(names[i])
