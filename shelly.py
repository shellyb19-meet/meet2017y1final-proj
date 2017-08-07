#changing shape
#a = the names of all the items
a = ["apple", "banana", "strawberry", "orange", "grape"]

a.sort()

clones_list = []
for n in range(len(a)):
    obj = turtle.clone()
    clones_list.append(obj)
    turtle.register_shape(a[n])
    obj.shape(a[n])



good_food_turtles
good_food_names

bad_food_turtles
bad_food_names

other_stuff_turtles
other_stuff_names

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

