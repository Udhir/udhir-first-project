import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Login")

# Top
top_box = tk.Label(root, text="Top")
top_box.pack(side="top", fill="x")

# Bottom
bottom_box = tk.Label(root, text="Bottom")
bottom_box.pack(side="bottom", fill="x")

# Left
left_box = tk.Label(root, text="Left")
left_box.pack(side="left", fill="y")

# Right
right_box = tk.Label(root, text="Right")
right_box.pack(side="right", fill="y")

# Center
center_box = tk.Label(root, text="Center")
center_box.pack(expand=True)

root.mainloop()
