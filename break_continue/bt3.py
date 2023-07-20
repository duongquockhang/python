import turtle
import math

# Tạo đối tượng turtle và màn hình
t = turtle.Turtle()
screen = turtle.Screen()

# Thiết lập màu nền và màu rùa
screen.bgcolor("white")
t.pencolor("blue")

# Thiết lập giá trị ban đầu
a = 0
b = 5
theta = 0
r = 100  # Bán kính mong muốn

# Vẽ đường xoắn ốc
while True:
    # Tính toán vị trí x và y của rùa trên mặt phẳng
    x = (a + b * theta) * math.cos(theta)
    y = (a + b * theta) * math.sin(theta)
    t.goto(x, y)
    # Tăng giá trị theta để vẽ đường xoắn ốc
    theta += 0.1
    # Kiểm tra nếu đường xoắn ốc đã đạt đến bán kính mong muốn thì dừng lại
    if (a + b * theta) >= r:
        break

# Chạy chương trình và đóng màn hình khi kết thúc
turtle.done()