def rain():
    upto = len(fallen_items)
    chosen_fallen_item_num = random_randint(0,upto)
    chosen_fallen_item = fallen_items_list.index(chosen_fallen_item_num)
    rx = random.randint(size_x - 0.5*size_x, (size_x - 0.5*size_x)*-1)
    chosen_fallen_item.goto(rx, size_y - 0.5*size_y)
    while not chosen_fallen_item_xpos in farmer_xpos_list and not chosen_fallen_item_ypos in farmer_ypos_list :
    chosen_fallen_item_xpos =    chosen_fallen_item.pos()[0]
    chosen_fallen_item_ypos = chosen_fallen_item.pos()[1]
    chosen_fallen_item_ypos += -20]
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
