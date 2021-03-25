import tkinter as tk
from tkinter import *
from tkinter import messagebox

import mysql.connector as mysql

root = tk.Tk()
root.title("Fetchest")

def insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if (id == "" or name == "" or phone == ""):
        messagebox.showinfo("Error", "Se requiere llenar todos los campos")
    else:
        conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
        cursor = conn.cursor()
        cursor.execute("insert into fc_client values('"+ id +"','"+ name +"','"+ phone +"')")
        cursor.execute("commit")
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')

        messagebox.showinfo("Estatus", "Registrado")
        conn.close()
# frame1_tel =LabelFrame(root,text="Telefono")

lTitle = Label(root, font=('bold'),text='REGISTRO DE CLIENTE',bg = "#16425B",fg='white')
lTitle.place(x=255,y=80)

lId = Label(root, text='ID',bg = "#16425B",fg='white')
lId.place(x=260,y=140)
e_id = Entry()
e_id.place(x=320,y=140)
lName = Label(root, text='Nombre',bg = "#16425B",fg='white')
lName.place(x=260,y=180)
e_name = Entry()
e_name.place(x=320,y=180)
lTel = Label(root, text='Telefono',bg = "#16425B",fg='white')
lTel.place(x=260,y=220)
e_phone = Entry()
e_phone.place(x=320,y=220)



insert = Button(root, text="Registrar",command=insert)
insert.place(x=350,y=280)



# mylabel1 = tk.Label(root, text="hello2").grid(row=1,column=2)

root.geometry("750x500+0+0")
root.resizable(False,False)
root.config(bg = "#16425B")


root.mainloop()
