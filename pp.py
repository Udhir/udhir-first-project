from tkinter import *
root = Tk()
root.geometry("400x250")
Username = Label(root,text = "Username").grid(row = 0, column = 0)
e1 = Entry(root).grid(row = 0, column = 1)
password = Label(root,text = "Password").grid(row = 1, column = 0)
e2 = Entry(root).grid(row = 1,column = 1)
login = Button(root, text = "login").grid(row = 4, column = 1)
root.mainloop()







