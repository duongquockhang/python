import turtle as t
import random

# Khai báo biến run
run = True

# Tạo khung cảnh và vẽ các cột mốc bên trái đường đua
screen = t.Screen()
screen.setup(height=500, width=600)
pen = t.Turtle(visible=False)
pen.penup()
pen.speed(0)
pen.goto(-250, 200)
for i in range(21):
    pen.write(i)
    pen.forward(25)

# Vẽ các đường đứt đoạn trên đường đua và
# đánh dấu các cột mốc bên phải đường đua
x = -250
pen.goto(-250, 200)
pen.right(90)
for i in range(21):
    for j in range(10):
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.forward(10)
    pen.penup()
    pen.forward(5)
    pen.write(i)
    pen.goto(x + (i + 1) * 25, 200)

# Khai báo biến all_turtles và y_position
all_turtles = []
y_position = [160, 100, 40, -20]

# Tạo các rùa và thêm vào all_turtles
colors = ['red', 'green', 'blue', 'black']
for turtle in range(0, 4):
    turtles = t.Turtle(shape="turtle")
    turtles.penup()
    # Di chuyển rùa về vị trí ban đầu,
    # bên trái cùng của đường đua
    turtles.goto(x=-250, y=y_position[turtle])
    # Màu của rùa
    turtles.color(colors[turtle])
    for i in range(5):
        turtles.left(72)
    # Lưu vào list
    all_turtles.append(turtles)

# Hàm random_walk
def random_walk(turtles):
    global run
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        # Kiểm tra điều kiện cán đích
        # Khi 1 con cán đích thì dừng lại
        if turtle.xcor() > 250:
            run = False
    run = True

# Vòng lặp chính
while run:
    random_walk(all_turtles)

# Kết thúc chương trình
screen.exitonclick()