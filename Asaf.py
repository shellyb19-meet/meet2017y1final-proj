import turtle
turtle.tracer(1,0)

x_size=800
y_size=700
turtle.setup(x_size,y_size)
SQUARE_SIZE=20

def farmer():
    turtle.hideturtle()
    turtle.register_shape("farmer.gif")
    farmer=turtle.clone()
    farmer.shape("farmer.gif")

    farmer.penup()
    farmer.goto(0,-320)
    farmer.showturtle()

    LEFT_ARROW="Left"
    RIGHT_ARROW="Right"
    LEFT=0
    RIGHT=1
    direction=LEFT

    RIGHT_EDGE = 200
    LEFT_EDGE = -200
    RIGHT_EDGE = 380
    LEFT_EDGE = -380

    def left():
        
        global direction
        direction=LEFT
        move_farmer()
        print('you moved the farmer laft')
        print(farmer.pos())
        
    def right():
        
        global direction
        direction=RIGHT
        move_farmer()
        print('you moved the farmer right')
        print(farmer.pos())

    def move_farmer():
        x=farmer.pos()[0]
        y=farmer.pos()[1]
        
        if direction == LEFT:
            farmer.goto(x-SQUARE_SIZE,y)
        elif direction == RIGHT:
            farmer.goto(x+SQUARE_SIZE,y)
        if x>RIGHT_EDGE:
            quit()
        elif x<LEFT_EDGE:
            quit()

    turtle.onkeypress(left,LEFT_ARROW)
    turtle.onkeypress(right,RIGHT_ARROW)
    turtle.listen()

