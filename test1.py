import turtle

# Khởi tạo turtle
t = turtle.Turtle()

# Thiết lập màu sắc và kích thước nét vẽ
t.color("black", "white")
t.pensize(3)

# Vẽ Bát quái Thái Cực đen trắng
t.begin_fill()

# Vẽ từng đoạn thẳng và cung với độ dài và góc tương ứng
for i in range(8):
    if i in [0, 1, 2, 4, 5, 6]:
        t.forward(100)
    else:
        t.circle(50, 180)
        t.forward(50)
        t.circle(50, 180)
        t.forward(50)

    t.left(45)

    if i in [1, 3, 5, 7]:
        t.color("white", "black")
    else:
        t.color("black", "white")

t.end_fill()

# Hiển thị kết quả
turtle.done()