import turtle
import math

# Hình thứ nhất - ellipse
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(0, 0)
pen.pendown()

# Vẽ nửa ellipse đầu tiên
a = 100
b = 50
t = 0
while t <= 90:
    x = a * math.cos(math.radians(t))
    y = b * math.sin(math.radians(t))
    pen.goto(x, y)
    t += 1

# Vẽ nửa ellipse thứ hai
a = 100
b = 50
t = 90
while t <= 180:
    x = a * math.cos(math.radians(t))
    y = b * math.sin(math.radians(t))
    pen.goto(x, y)
    t += 1

# Hình thứ hai - ellipse quay
pen.penup()
pen.goto(0, -150)
pen.pendown()

angle = 0
a = 100
b = 50
while True:
    # Thiết lập màu khác nhau cho bút vẽ
    if angle % 2 == 0:
        pen.color("red")
    else:
        pen.color("blue")

    # Vẽ ellipse
    t = 0
    while t <= 360:
        x = a * math.cos(math.radians(t))
        y = b * math.sin(math.radians(t))
        pen.goto(x, y)
        t += 1

    # Thay đổi góc quay
    angle += 10
    pen.setheading(angle)

    # Kiểm tra điều kiện kết thúc vòng lặp
    if angle >= 360:
        break

turtle.done()