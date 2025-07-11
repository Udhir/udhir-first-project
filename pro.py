from tkinter import *
root=Tk()
root.title('login')
#root.geometry('300x300')
root.maxsize(width=300,height=300)
root.minsize(width=300,height=300)
root.resizable(0,0)

top_box = root.Label(root, text="Top")
top_box.pack(side="top", fill="x")

bottom_box = root.Label(root, text="Bottom")
bottom_box.pack(side="bottom", fill="x")


left_box = root.Label(root, text="Left")
left_box.pack(side="left", fill="y")


right_box = root.Label(root, text="Right")
right_box.pack(side="right", fill="y")


center_box = root.Label(root, text="Center")
center_box.pack(expand=True)
mainloop()