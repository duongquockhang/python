import tkinter as tk

def draw_hotel(canvas):
    # Vẽ biển
    canvas.create_rectangle(0, 200, 500, 300, fill="brown")

    # Vẽ núi
    canvas.create_polygon(50, 200, 200, 50, 350, 200, fill="gray")

    # Vẽ tòa nhà
    canvas.create_rectangle(100, 100, 400, 250, fill="gray")

    # Vẽ cửa chính
    canvas.create_rectangle(190, 150, 230, 250, fill="brown")

    # Vẽ cửa sổ
    canvas.create_rectangle(120, 150, 160, 190, fill="blue")
    canvas.create_rectangle(280, 150, 320, 190, fill="blue")

    # Vẽ mái nhà
    canvas.create_polygon(100, 100, 250, 50, 400, 100, fill="red")

    # Vẽ cây
    canvas.create_rectangle(20, 180, 70, 230, fill="brown")
    canvas.create_polygon(10, 180, 80, 180, 45, 120, fill="darkgreen")
    canvas.create_polygon(10, 150, 80, 150, 45, 90, fill="darkgreen")

    # Vẽ động vật (ví dụ: chim)
    canvas.create_polygon(200, 120, 210, 110, 220, 120, fill="gray")
    canvas.create_oval(210, 120, 215, 125, fill="gray")

    # Vẽ mặt trời
    canvas.create_oval(430, 50, 470, 90, fill="yellow")

# Tạo một cửa sổ giao diện
root = tk.Tk()
root.title("Vẽ khách sạn với cây, động vật, biển, núi và mặt trời")

# Tạo canvas để vẽ
canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()

# Vẽ khách sạn với các yếu tố khác
draw_hotel(canvas)

# Chạy vòng lặp chính của ứng dụng
root.mainloop()