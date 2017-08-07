import turtle
turtle.tracer(1,0)

x_size=800
y_size=700
turtle.setup(x_size,y_size)
SQUARE_SIZE=20

farmer_pos_list=[]
farmer_stamp_list=[]

turtle.hideturtle
turtle.register_shape("farmer.gif")
farmer=turtle.clone()
farmer.shape("farmer.gif")

farmer.penup()
farmer.goto(0,-350)

LEFT_ARROW="Left"
RIGHT_ARROW="Right"
LEFT=0
RIGHT=1
direction=LEFT

UP_EDGE = 350
DOWN_EDGE = -350
RIGHT_EDGE = 400
LEFT_EDGE = -400

def left():
    global direction
    direction=LEFT
    x=farmer.pos()[0]
    y=farmer.pos()[1]
    farmer.goto(x-SQUARE_SIZE,y)
    print('you moved the farmer laft')
    print(farmer.pos())
##    farmer_stamp_list.append(farmer.stamp())
##    farmer_stamp_list.pop(0)
##    print(farmer_stamp_list)
    
def right():
    global direction
    direction=RIGHT
    x=farmer.pos()[0]
    y=farmer.pos()[1]
    farmer.goto(x+SQUARE_SIZE,y)
    print('you moved the farmer right')
    print(farmer.pos())
##    farmer_stamp_list.append(farmer.stamp())
##    farmer_stamp_list.pop(0)
##    print(farmer_stamp_list)
    
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

