import turtle

# Vẽ móc cột
color = 'red'
size = 5

turtle.color(color)
turtle.pensize(size)
turtle.penup()

# Tọa độ móc cột
x = -150
y = 0

turtle.goto(x, y)
turtle.pendown()

for i in range(2):
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)

# Vẽ mái hiên
color = 'yellow'
turtle.color(color)
turtle.begin_fill()
turtle.penup()

# Tọa độ mái hiên
x = -150
y = 0

turtle.goto(x, y)
turtle.pendown()

turtle.setheading(45)
turtle.forward(212)
turtle.setheading(0)
turtle.forward(212)
turtle.setheading(-45)
turtle.forward(300)
turtle.setheading(90)
turtle.forward(30)
turtle.end_fill()

# Vẽ tường nhà
color = 'blue'
turtle.color(color)
turtle.begin_fill()
turtle.penup()

# Tọa độ tường nhà
x = -70
y = -110

turtle.goto(x, y)
turtle.pendown()

for i in range(2):
    turtle.forward(140)
    turtle.right(90)
    turtle.forward(140)
    turtle.right(90)

turtle.end_fill()

# Vẽ cửa ra vào
color = 'brown'
turtle.color(color)
turtle.penup()

# Tọa độ cửa ra vào
x = -40
y = -110

turtle.goto(x, y)
turtle.pendown()

turtle.setheading(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(70)

# Vẽ cửa sổ
color = 'white'
turtle.color(color)
turtle.penup()

# Tọa độ cửa sổ
x = 50
y = -60

turtle.goto(x, y)
for i in range(2):
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for j in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    x += 50