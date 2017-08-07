a = ["apple", "banana", "strawberry", "orange", "grape"]

a.sort()

clones_list = []
for n in range(len(a)):
    obj = turtle.clone()
    clones_list.append(obj)
    turtle.register_shape(a[n])
    obj.shape(a[n])

for good_food in clones_list:
    if good_food.pos() == farmer.pos():


good_food_turtles
good_food_names

bad_food_turtles
bad_food_names

other_stuff_turtles
other_stuff_names
