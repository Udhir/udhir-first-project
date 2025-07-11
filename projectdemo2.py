from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.geometry('500x650')
root.resizable(0,0)
root.title("Customer Registration System")
root.configure(bg="white")

conn = sqlite3.connect('customer_registration.db')
c = conn.cursor()
c.execute

          
llb_registration=Label(root, text="Customer Registration Form",\
                         font=("Arial",16, "bold"), bg="white", fg="darkblue")
llb_registration.place(x=120, y=20)

lbl_fullname=Label(root, text="Full Name", bg="white", font=("Arial",12))
lbl_fullname.place(x=50, y=80)
full_name = Entry(root, width=35, font=("Arial",11))
full_name.place(x=180, y=80)

lbl_phone=Label(root, text="Phone", bg="white", font=("Arial",12))
lbl_phone.place(x=50, y=130)
phone = Entry(root, width=35, font=("Arial",11))
phone.place(x=180, y=130)

lbl_email=Label(root, text="Email", bg="white", font=("Arial",12))
lbl_email.place(x=50, y=180)
email = Entry(root, width=35, font=("Arial",11))
email.place(x=180, y=180)

lbl_address=Label(root, text="Address", bg="white", font=("Arial",12))
lbl_address.place(x=50, y=230)
address = Entry(root, width=35, font=("Arial",11))
address.place(x=180, y=230)

btn_register = Button(root, text="Register", bg="green", \
                      fg="white", font=("Arial",11, "bold")
btn_register.place(x=200, y=280)

btn_fetch = Button(root, text="Show Records", bg='blue', \
                   fg="white", font=("Arial",11, "bold")
btn_fetch.place(x=190, y=330)

lbl_delete=Label(root, text="Enter Id Delete", bg="white", font=("Arial",12))
lbl_delete.place(x=50, y=380)
delete_record = Entry(root, width=20, font=("Arial",11))
delete_record.place(x=200, y=380)

btn_delete = Button(root,text="Delete",bg="red", fg="white", font=("Arial",11, "bold"))
btn_delete.place(x=380, y=375)

show_records = Label(root, text="",  bg="white", justify="LEFT",\
                      anchor="nw, font=("Courier(",10), relief=SOLID,\
                                                width=55, height=15
                                                
                                            