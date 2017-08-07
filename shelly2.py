import turtle
snake=turtle.clone()
love=turtle.clone()
turtle.goto(20,0)
love.goto(23,0)
snake.goto(20,0)
turtle_pos = turtle.pos()
turtle_pos_x = turtle.pos()[0]
snake_pos = snake.pos()
love_pos = love.pos()
my_list = [snake_pos, love_pos]
for i in my_list:
    if i[0] == turtle_pos_x:
        print("YAY!")
