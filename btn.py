from tkinter import *
root = Tk()
root.geometry('500x500')
ent=Entry(show='*')
ent.place(x=20,y=40)
def password_show_hide():
    if r.get()==1:
        ent.configure(show='')
    else:
        ent.configure(show='*')
r=IntVar()
btn1=Checkbutton(text='show password',variable=r,command=password_show_hide)
btn1.place(x=50,y=80)
mainloop()