import tkinter as tk

# Tạo một cửa sổ giao diện
root = tk.Tk()
root.title("Vẽ nhà với cây và chim chồn")

# Tạo một canvas để vẽ trên
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Vẽ ngôi nhà
canvas.create_rectangle(50, 100, 250, 200, fill="lightblue")  # Thân nhà
canvas.create_polygon(50, 100, 150, 50, 250, 100, fill="gray")  # Mái nhà
canvas.create_rectangle(90, 120, 130, 200, fill="brown")  # Cửa nhà
canvas.create_rectangle(180, 120, 220, 160, fill="yellow")  # Cửa sổ

# Vẽ mặt trời
canvas.create_oval(10, 10, 60, 60, fill="yellow")

# Vẽ cỏ xung quanh nhà
canvas.create_rectangle(0, 200, 400, 300, fill="green")

# Vẽ cây
canvas.create_rectangle(300, 100, 330, 200, fill="brown")  # Thân cây
canvas.create_polygon(250, 100, 350, 100, 300, 50, fill="darkgreen")  # Lá cây

# Vẽ chim chồn
canvas.create_polygon(100, 80, 110, 70, 120, 80, fill="gray")  # Cánh chim chồn
canvas.create_oval(100, 80, 120, 100, fill="gray")  # Thân chim chồn
canvas.create_line(110, 100, 110, 110, fill="black")  # Chân chim chồn
canvas.create_line(115, 100, 115, 110, fill="black")  # Chân chim chồn

# Chạy vòng lặp chính của ứng dụng
root.mainloop()