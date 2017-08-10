import turtle
import random
turtle.tracer(1,0)

x_size=800
y_size=700
turtle.setup(x_size,y_size)
turtle.penup()
background = turtle.clone()
turtle.register_shape("background.gif")
background.shape("background.gif")
background.penup()
background.goto(0,0)
background.stamp()
background.hideturtle()

turtle.mainloop()
