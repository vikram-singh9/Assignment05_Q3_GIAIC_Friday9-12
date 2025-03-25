import tkinter as tk

# Window banane ke liye
root = tk.Tk()
root.title("Eraser on Canvas")

# Canvas ka size aur cell ka size set karna
canvas_width = 500
canvas_height = 500
cell_size = 20  # Har cell 20x20 pixels ka hoga

# Canvas banaya
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Grid banane ke liye list jo cells ke colors store karegi
grid = {}
for x in range(0, canvas_width, cell_size):
    for y in range(0, canvas_height, cell_size):
        # Har cell ko blue se bharo aur canvas pe draw karo
        cell_id = canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill="blue")
        grid[(x, y)] = cell_id  # Position aur ID store karo

# Eraser ka size aur shuruati position
eraser_size = 40  # Eraser 40x40 ka hoga
eraser = canvas.create_rectangle(0, 0, eraser_size, eraser_size, fill="red", outline="black")

# Eraser ko move karne ka function
def move_eraser(event):
    # Mouse ke coordinates se eraser ko move karo
    x, y = event.x, event.y
    canvas.coords(eraser, x, y, x + eraser_size, y + eraser_size)
    
    # Check karo ki eraser kin cells ko touch kar raha hai
    for (cell_x, cell_y), cell_id in grid.items():
        # Agar eraser cell ke saath overlap karta hai
        if (x < cell_x + cell_size and x + eraser_size > cell_x and
            y < cell_y + cell_size and y + eraser_size > cell_y):
            canvas.itemconfig(cell_id, fill="white")  # Cell ko white kar do

# Mouse drag ko eraser se connect karo
canvas.bind("<B1-Motion>", move_eraser)

# Program ko chalao
root.mainloop()