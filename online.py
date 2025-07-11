from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.geometry("500x650")
root.resizable(0,0)
root.title("Customer Registration System")
root.configure(bg="white")

def add():
    f=full_name.get()
    p=phone.get()
    e=email.get()
    a=address.get()
    if not f or not p or not e or not a:
        messagebox.showwarning('error','all fields are required')
        return
    conn=sqlite3.connect('Customer_registration.db')
    c = conn.cursor()
    c.execute('insert into registration (full_name,phone,email,address) \
              values("{}", "{}", "{}", "{}")'.format(f,p,e,a))
    
    conn.commit()
    conn.close()

def get_customer_details():
    conn = sqlite3.connect('customer_registration.db')
    c= conn.cursor()
    c.execute('SELECT * FROM registration ')
    records = c.fetchall()
    conn.close()
    printed_records=''
    for i in records:
        printed_records=printed_records+i[0]+ ' ' +str(i[2])+"\n"
        
    show_record.config(text=printed_records)
    
    
def delete_records():
    oid = delete_record.get()
    if not oid:
        messagebox.showerror("Error", "Please enter a ID")
        return
    
    conn = sqlite3.connect('Customer_registration.db')
    c = conn.cursor()
    c.execute('DELETE FROM registration WHERE oid=?',(oid,))
    conn.commit()
    conn.close()
    
    delete_record.delete(0,END)
    get_customer_details()


def edit_details():
    oid = delete_record.get()
    if not oid:
        messagebox.showerror("Error", "Please enter a ID")
        return
 
    conn = sqlite3.connect('customer_registration.db')
    c = conn.cursor()
    c.execute('SELECT * FROM registration WHERE oid=?', (oid,))
    record = c.fetchone()
    conn.close()

    
    root = Toplevel()
    root.configure(bg="white")
    root.title('Update records')
    root.geometry('500x500')
    
lbl_fullname=Label(root, text="Fullname",bg="white",font=("arial",12))
lbl_fullname.place(x=50,y=80)
full_name=Entry(root,width=35,font=("arial",11))
full_name.place(x=180,y=80)


lbl_phone=Label(root, text="Phone",bg="white",font=("arial",12))
lbl_phone.place(x=50,y=130)
phone=Entry(root,width=35,font=("arial",11))
phone.place(x=180,y=130)

lbl_email=Label(root, text="Email",bg="white",font=("arial",12))
lbl_email.place(x=50,y=180)
email=Entry(root,width=35,font=("arial",11))
email.place(x=180,y=180)

lbl_address=Label(root, text="Address",bg="white",font=("arial",12))
lbl_address.place(x=50,y=230)
address=Entry(root, width=35,font=("arial",11))
address.place(x=180,y=230)

btn_register=Button(root, text="Register",bg="green",fg="white",font=("arial",11,"bold"),command=add)
btn_register.place(x=200,y=280)

def update():
    conn = sqlite3.connect('customer_registration.db')
    c = conn.cursor()
    c.execute('''
              UPDATE registration SET full_name=?, phone=?, email=?, address=? WHERE oid=?
              ''', (full_name.get(), phone.get(), email.get(), address.get(), oid))
    conn.commit()
    conn.close()
    messagebox.showinfo('Sucess', 'Record update sucessfully')
    root.destroy()
    get_customer_details()
    
btn_save=Button(root,text="SAVE",bg="green",fg="white",font=("arial",11,"bold"),command=update)
btn_save.place(x=450,y=375)


conn=sqlite3.connect("Customer_registration.db")
c = conn.cursor()
c.execute('''
          CREATE TABLE if not exists registration(
              full_name VARCHAR(20),
              phone CHAR(10),
              email VARCHAR(30),
              address VARCHAR(30)
          )
''')
conn.commit()
conn.close()

llb_registration=Label(root,text="Customer Registration Form",
                       font=("arial",16,"bold"),
                       bg="white",fg="darkblue")
llb_registration.place(x=120,y=20)

lbl_fullname=Label(root,text="Fullname",bg="white",font=("arial",12))
lbl_fullname.place(x=50,y=80)
full_name=Entry(root,width=35,font=("arial",11))
full_name.place(x=180,y=80)


lbl_phone=Label(root,text="Phone",bg="white",font=("arial",12))
lbl_phone.place(x=50,y=130)
phone=Entry(root,width=35,font=("arial",11))
phone.place(x=180,y=130)

lbl_email=Label(root,text="Email",bg="white",font=("arial",12))
lbl_email.place(x=50,y=180)
email=Entry(root,width=35,font=("arial",11))
email.place(x=180,y=180)

lbl_address=Label(root,text="Address",bg="white",font=("arial",12))
lbl_address.place(x=50,y=230)
address=Entry(root,width=35,font=("arial",11))
address.place(x=180,y=230)


btn_register=Button(root,text="Register",bg="green",fg="white",font=("arial",11,"bold"),command=add)
btn_register.place(x=200,y=280)

btn_fetch=Button(root,text="show records",bg="blue",fg="white",font=("arial",11,"bold"),command=get_customer_details)
btn_fetch.place(x=190,y=330)


lbl_delete=Label(root,text="Enter Id Delete",bg="white",font=("arial",11))
lbl_delete.place(x=50,y=380)

delete_record=Entry(root,width=20,font=("arial",11))
delete_record.place(x=200,y=380)

btn_delete=Button(root,text="Delete",bg="red",fg="white",font=("arial",11,"bold"),command=delete_record)
btn_delete.place(x=380,y=375)

btn_edit=Button(root,text="Edit",bg="green",fg="white",font=("arial",11,"bold"),command=edit_details)
btn_edit.place(x=450,y=375)

show_record=Label(root,text="Show Records",bg="white",justify="right",anchor="nw",font=("Courier",11),relief=SOLID,width=35,height=15)
show_record.place(x=30,y=430)

root.mainloop()

 