import tkinter as tk
from tkinter import Entry, LabelFrame, Listbox, PhotoImage, Scrollbar
from tkinter import messagebox
from tkinter import ttk
from tkinter.constants import COMMAND, END, VERTICAL
from datetime import datetime
from reportlab.pdfgen import canvas 
from reportlab.pdfbase import pdfmetrics
import matplotlib.pyplot as plt

import mysql.connector as mysql

class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs, ):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}

        # --------------------------- menu
        menu = tk.Menu(container)

        betting = tk.Menu(menu, tearoff=0)
        menu.add_cascade(menu=betting, label="Opciones")
        betting.add_command(label="Inicio",command=lambda: self.show_frame(Startpage))
        betting.add_command(label="Registro",command=lambda: self.show_frame(PageRegistro))
        betting.add_command(label="Compra",command=lambda: self.show_frame(Compra))
        betting.add_command(label="Inventario",command=lambda: self.show_frame(PageInventario))

        betting2 = tk.Menu(menu, tearoff=0)
        menu.add_cascade(menu=betting2, label="Estadísticas")
        betting2.add_command(label="General",command=lambda: self.show_frame(E_General))
        betting2.add_command(label="Cliente",command=lambda: self.show_frame(E_cliente))
        betting2.add_command(label="Producto",command=lambda: self.show_frame(E_Producto))
        
        tk.Tk.config(self, menu=menu)

        for F in (Startpage, PageRegistro, PageInventario, Compra,E_General,E_cliente,E_Producto):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.config(bg="#16425B")

        self.show_frame(Startpage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Startpage(tk.Frame):  

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        ll = tk.Label(self, text="BIENVENIDO A FETCHEST",bg="#16425B",fg='white',font=('Helvetica', 18, 'bold')).place(x=200,y=35)
        
        div = tk.Label(self, text="_______________________________________________________",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 15, 'bold')).place(x=50,y=110)
        l2 = tk.Label(self, text="Fetchest busca automatizar el análisis de datos,\n\ncon la finalidad de tomar mejores decisiones para la empresa.",bg="#16425B",fg='white')
        l2.place(x=190,y=110)
        div = tk.Label(self, text="_______________________________________________________",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 15, 'bold')).place(x=50,y=350)
        
        e = tk.Label(self, text="OBJETIVOS",bg="#16425B",fg='white',font=('Helvetica', 12, 'bold')).place(x=312,y=190)
        sub6 = tk.Label(self, text="      Nuevo                Actual",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=320,y=220)
        sp_op = tk.Label(self, text="Productos:",bg="#16425B",fg='white').place(x=240,y=240)
        sp_oc = tk.Label(self, text="Clientes:",bg="#16425B",fg='white').place(x=240,y=270)
        sp_ov = tk.Label(self, text="Ventas:",bg="#16425B",fg='white').place(x=240,y=300)
        #---------------------------objetivo
        self.sp_opE = tk.Entry(self,bg="#d9dcd6",fg="#16425B", width=12)
        self.sp_opE.place(x=320,y=240)

        self.sp_ocE = tk.Entry(self,bg="#d9dcd6",fg="#16425B", width=12)
        self.sp_ocE.place(x=320,y=270)

        self.sp_ovE = tk.Entry(self,bg="#d9dcd6",fg="#16425B", width=12)
        self.sp_ovE.place(x=320,y=300)

        self.sp_opEa = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=9,height=1)
        self.sp_opEa.place(x=400,y=240)

        self.sp_ocEa = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=9,height=1)
        self.sp_ocEa.place(x=400,y=270)

        self.sp_ovEa = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=9,height=1)
        self.sp_ovEa.place(x=400,y=300)

        self.st_objetivosget()
        #------------------------------------aviso legal
        w = tk.Canvas(self, width=290, bg="#16425B",height=150).place(x=50,y=400)
        e = tk.Label(self, text="AVISO LEGAL",bg="#16425B",fg='white',font=('Helvetica', 12, 'bold')).place(x=140,y=415)
        sub1 = tk.Label(self, text=" Fetchest excluye cualquier responsabilidad\n por los daños y perjuicios de toda naturaleza que\n pudieran deberse a la mala utilización del Servicio. \nPor motivos de seguridad, Fetchest no recopila\n ni almacena información confidencial de su empresa",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=60,y=450)
        #-------------------------------------desarrolladores
        w1 = tk.Canvas(self, width=290, bg="#16425B",height=150).place(x=370,y=400)
        e1 = tk.Label(self, text="DESARROLLADORES",bg="#16425B",fg='white',font=('Helvetica', 12, 'bold')).place(x=435,y=415)
        sub2 = tk.Label(self, text=" -  Alejandro Lobo",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 10, 'italic')).place(x=390,y=450)
        sub2 = tk.Label(self, text=" -  Alberto Rodríguez",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 10, 'italic')).place(x=390,y=470)
        sub2 = tk.Label(self, text=" -  Luis Guerrero",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 10, 'italic')).place(x=520,y=450)
        sub2 = tk.Label(self, text=" -  Melissa Reyna",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 10, 'italic')).place(x=520,y=470)
        sub2 = tk.Label(self, text=" -  Gerardo Garavito",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 10, 'italic')).place(x=390,y=490)
        sub2 = tk.Label(self, text="Contacto: inventariooapp@gmail.com",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=420,y=520)

        # -------------------------- agregar
        act = tk.Button(self, text="Modificar",height = 1, width = 10,bg="#fedc56",command= self.st_objetivos)
        act.place(x=320,y=330)
    
    def st_objetivosget(self):
        self.sp_opEa.configure(state='normal')
        self.sp_opEa.delete('1.0',END)
        self.sp_ocEa.configure(state='normal')
        self.sp_ocEa.delete('1.0',END)
        self.sp_ovEa.configure(state='normal')
        self.sp_ovEa.delete('1.0',END)

        conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
        #---------------------------objetivos
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `fc_objetivos`")
        result = cursor.fetchone()
        self.sp_opEa.insert(END,result[0])
        self.sp_opEa.configure(state='disabled')
        self.sp_ocEa.insert(END,result[1])
        self.sp_ocEa.configure(state='disabled')
        self.sp_ovEa.insert(END,result[2])
        self.sp_ovEa.configure(state='disabled')

        conn.close()
        pass

    def st_objetivos(self):
        o_productos = self.sp_opE.get()
        o_clientes = self.sp_ocE.get()
        o_ventas = self.sp_ovE.get()

        if (o_productos == "" or o_clientes == "" or o_ventas == ""):
            messagebox.showinfo("Error", "Se requiere llenar todos los campos")
        else:
            conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
            cursor = conn.cursor()
            cursor.execute("update fc_objetivos set o_productos='" + o_productos + "', o_clientes='" + o_clientes +"', o_ventas='" + o_ventas +"'")
            cursor.execute("commit")
            self.sp_opE.delete(0,'end')
            self.sp_ocE.delete(0,'end')
            self.sp_ovE.delete(0,'end')
            
            self.st_objetivosget()
            messagebox.showinfo("Estatus", "Actualizado")
            conn.close() 
        pass

class PageRegistro(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label = tk.Label(self, text="Autenticación")   despues autentificamos
        l0 = tk.Label(self, text="",bg="#16425B").pack(pady=1, padx=10)
        label = tk.Label(self, text="Registro de cliente",bg="#16425B",fg='white',font=('Helvetica', 18, 'bold'))
        label.pack(pady=10, padx=10)
        l1 = tk.Label(self, text="",bg="#16425B").pack(pady=1, padx=10)

        # self.var = tk.IntVar()
        # chk = tk.Checkbutton(self, text="Cliente Nuevo",fg="black", variable=self.var,
        #     command=self.show_status)
        # chk.select()
        # chk.pack()
        
        self.frame1_id =LabelFrame(self,text="Id",padx=10,pady=10,bg="#16425B",fg='white')       
        self.e_id= Entry(self.frame1_id,bg="#d9dcd6",fg="#16425B")
        
        self.frame1_nom =LabelFrame(self,text="Nombre",padx=10,pady=10,bg="#16425B",fg='white')
        self.e_name= Entry(self.frame1_nom,bg="#d9dcd6",fg="#16425B")
        self.frame1_nom.pack(padx=15,pady=12)
        self.e_name.pack()

        self.frame1_tel =LabelFrame(self,text="Telefono",padx=10,pady=10,bg="#16425B",fg='white')
        self.e_phone= Entry(self.frame1_tel,bg="#d9dcd6",fg="#16425B")
        self.frame1_tel.pack(padx=15,pady=12)
        self.e_phone.pack()
        
        # button1 = tk.Button(self, text="Autenticar",
        #                 command = myMessage)
        
        self.btn_r = tk.Button(self, text="Registrar",
                        command=lambda: [self.insert(),controller.show_frame(Compra)])
        self.btn_r.pack()
        # self.btn_inicio_sesion = tk.Button(self, text="Continuar",
        #                 command=lambda: [controller.show_frame(Compra)])
        # self.btn_inicio_sesion.pack_forget()
        pass

    # def show_status(self):
    #     # print("variable is", self.var.get())
    #     if self.var.get() == 0:
    #         # print("si")
    #         self.e_id.pack_forget()
    #         self.frame1_id.pack_forget()
    #         self.frame1_nom.pack_forget()
    #         self.e_name.pack_forget()
    #         self.frame1_tel.pack_forget()
    #         self.e_phone.pack_forget()
    #         self.btn_r.pack_forget()
    #         self.btn_inicio_sesion.pack_forget()

    #         self.e_id.pack()
    #         self.frame1_id.pack(padx=15,pady=12)
    #         # 
    #         self.frame1_nom.pack(padx=15,pady=12)
    #         self.e_name.pack()
    #         #
    #         self.frame1_tel.pack(padx=15,pady=12)
    #         self.e_phone.pack()
    #         #
    #         self.btn_inicio_sesion.pack()
    #     else:
    #         # print("no")
    #         self.e_id.pack_forget()
    #         self.frame1_id.pack_forget()
    #         self.btn_r.pack_forget()
    #         self.btn_inicio_sesion.pack_forget()
    #         # 
    #         self.frame1_nom.pack(padx=15,pady=12)
    #         self.e_name.pack()
    #         #
    #         self.frame1_tel.pack(padx=15,pady=12)
    #         self.e_phone.pack()
    #         #
    #         self.btn_r.pack()
        # mylabelv= tk.Label(self,text=self.var.get()).pack()

    def insert(self):
        
        # id = self.e_id.get()
        name = self.e_name.get()
        phone = self.e_phone.get()

        if (name == "" or phone == ""):
            messagebox.showinfo("Error", "Se requiere llenar todos los campos")
        else:
            conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
            cursor = conn.cursor()
            cursor.execute("insert into fc_client values('""','"+ name +"','"+ phone +"')")
            cursor.execute("commit")
            # self.e_id.delete(0,'end')
            self.e_name.delete(0,'end')
            self.e_phone.delete(0,'end')

            messagebox.showinfo("Estatus", "Registrado")
            conn.close()

class E_General(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        eg_l = tk.Label(self, text="Estadísticas Generales",bg="#16425B",fg='white',font=('Helvetica', 18, 'bold'))
        eg_l.place(x=225,y=35)

        div2 = tk.Label(self, text="_______________________________________________________",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 15, 'bold')).place(x=50,y=110)
        sub1 = tk.Label(self, text="Productos",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=228,y=80)
        sub2 = tk.Label(self, text="Clientes",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=333,y=80)
        sub3 = tk.Label(self, text="Ventas",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=436,y=80)
        div2 = tk.Label(self, text="_______________________________________________________",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 15, 'bold')).place(x=50,y=180)
        div2 = tk.Label(self, text="_______________________________________________________",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 15, 'bold')).place(x=50,y=250)
        sub10 = tk.Label(self, text="Tabla de productos ordenados por cantidad en stock",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=220,y=285)
        div4 = tk.Label(self, text="_______________________________________________________",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 15, 'bold')).place(x=50,y=510)
        eg_tp = tk.Label(self, text="Total:",bg="#16425B",fg='white').place(x=50,y=100)

        sub4 = tk.Label(self, text="Fecha",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=237,y=145)
        sub5 = tk.Label(self, text="Hora",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=339,y=145)
        eg_fuc = tk.Label(self, text="Última ventas:",bg="#16425B",fg='white').place(x=50,y=170)
        eg_p = tk.Label(self, text="Valor de venta promedio:",bg="#16425B",fg='white').place(x=426,y=170)

        eg_o = tk.Label(self, text="Rendimiento actual\n frente a objetivo:",bg="#16425B",fg='white').place(x=50,y=229)
        sub4 = tk.Label(self, text="Productos",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=230,y=215)
        sub5 = tk.Label(self, text="Clientes",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=330,y=215)
        sub5 = tk.Label(self, text="Ventas",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=436,y=215)
        
        #---------------------------total producto
        self.eg_e_tp = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=11, height=1)
        self.eg_e_tp.place(x=210,y=100)
        #---------------------------totalcliente
        self.eg_e_tcl = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=11, height=1)
        self.eg_e_tcl.place(x=310,y=100)
        #---------------------------total ventas
        self.eg_e_tco = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=11, height=1)
        self.eg_e_tco.place(x=410,y=100)
        #---------------------última compra
        self.eg_e_fuc = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=11, height=1)
        self.eg_e_fuc.place(x=210,y=170)

        self.eg_e_fuch = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=11, height=1)
        self.eg_e_fuch.place(x=310,y=170)
        # -----------------------------promedio de compra
        self.eg_e_p = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=10, height=1)
        self.eg_e_p.place(x=575,y=170)
        #---------------------objetivos
        self.eg_e_op = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=11, height=1)
        self.eg_e_op.place(x=210,y=240)

        self.eg_e_oc = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=11, height=1)
        self.eg_e_oc.place(x=310,y=240)

        self.eg_e_ov = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=11, height=1)
        self.eg_e_ov.place(x=410,y=240)
        
        self.act_egenerales()

        #-------------------------tabla producto x stock
        self.stockTreeview = ttk.Treeview(self,height=4,columns=("ID","Producto","Marca","Costo","Stock"))
        
        self.stockTreeview.heading("ID",text="ID")
        self.stockTreeview.heading("Producto",text="Producto")
        self.stockTreeview.heading("Marca",text="Marca")
        self.stockTreeview.heading("Costo",text="Costo")
        self.stockTreeview.heading("Stock",text="Stock")

        self.stockTreeview['show'] = 'headings'

        self.stockTreeview.column("ID",minwidth=4,  width = 4)
        self.stockTreeview.column("Producto",minwidth=140, width = 140)
        self.stockTreeview.column("Marca",minwidth=90, width = 90)
        self.stockTreeview.column("Costo",minwidth=35, width = 30)
        self.stockTreeview.column("Stock",minwidth=35, width = 30)

        self.stockTreeview.place(x=50,y=315,width=610, height=200) ##

        self.tabla_general_stock()


        # -------------------------- actualizar
        act = tk.Button(self, text="Actualizar",height = 1, width = 10,bg="#fedc56", 
                                            command=lambda: [self.tabla_general_stock(),self.act_egenerales()])
        act.place(x=578,y=100)

    def tabla_general_stock(self):
        conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT fc_producto.p_id, fc_producto.p_name, fc_producto.p_brand, fc_producto.p_cost, fc_producto.p_stock FROM fc_producto order by fc_producto.p_stock")
        result = cursor.fetchall()
        if len(result) != 0:
            self.stockTreeview.delete(*self.stockTreeview.get_children())
            for row in result:
                self.stockTreeview.insert('',END,values=row)
                conn.commit()
        conn.close()
        pass

    def act_egenerales(self):
        self.eg_e_tco.configure(state='normal')
        self.eg_e_tco.delete('1.0',END)
        self.eg_e_tcl.configure(state='normal')
        self.eg_e_tcl.delete('1.0',END)
        self.eg_e_tp.configure(state='normal')
        self.eg_e_tp.delete('1.0',END)
        self.eg_e_fuc.configure(state='normal')
        self.eg_e_fuc.delete('1.0',END)
        self.eg_e_fuch.configure(state='normal')
        self.eg_e_fuch.delete('1.0',END)
        self.eg_e_p.configure(state='normal')
        self.eg_e_p.delete('1.0',END)
        self.eg_e_op.configure(state='normal')
        self.eg_e_op.delete('1.0',END)
        self.eg_e_oc.configure(state='normal')
        self.eg_e_oc.delete('1.0',END)
        self.eg_e_ov.configure(state='normal')
        self.eg_e_ov.delete('1.0',END)

        conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
        #---------------------------total de ventas
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(fc_compra.c_id) FROM `fc_compra`")
        result = cursor.fetchone()
        self.eg_e_tco.insert(END,result)
        self.eg_e_tco.configure(state='disabled')
        #----------------------------total de clientes
        cursor2  = conn.cursor()
        cursor2.execute("SELECT COUNT(fc_client.id) FROM `fc_client`")
        result2 = cursor2.fetchone()
        self.eg_e_tcl.insert(END,result2)
        self.eg_e_tcl.configure(state='disabled')
        #-------------------------- total de productos
        cursor3  = conn.cursor()
        cursor3.execute("SELECT COUNT(fc_producto.p_id) FROM `fc_producto`")
        result3 = cursor3.fetchone()
        self.eg_e_tp.insert(END,result3)
        self.eg_e_tp.configure(state='disabled')
        # ---------------------------fecha ultima compra
        cursor4  = conn.cursor()
        cursor4.execute("SELECT c_fecha FROM fc_compra ORDER BY c_id DESC LIMIT 1")
        result4 = cursor4.fetchone()
        self.eg_e_fuc.insert(END,result4[0][0:10])
        self.eg_e_fuc.configure(state='disabled')
        
        self.eg_e_fuch.insert(END,result4[0][11:16])
        self.eg_e_fuch.configure(state='disabled')
        # --------promedio
        cursor5  = conn.cursor()
        cursor5.execute("SELECT AVG(fc_producto.p_cost) FROM fc_producto,fc_compra WHERE fc_producto.p_id = fc_compra.id_producto")
        result5 = cursor5.fetchone()
        self.eg_e_p.insert(END,round(result5[0],2))
        self.eg_e_p.configure(state='disabled')
        # --------promedio
        cursor5  = conn.cursor()
        cursor5.execute("SELECT AVG(fc_producto.p_cost) FROM fc_producto,fc_compra WHERE fc_producto.p_id = fc_compra.id_producto")
        result5 = cursor5.fetchone()
        self.eg_e_p.insert(END,round(result5[0],2))
        self.eg_e_p.configure(state='disabled')

        #---------------------------total de ventas
        cursor6 = conn.cursor()
        cursor6.execute("SELECT * FROM `fc_objetivos`")
        result6 = cursor.fetchone()
        ro1 = (result3[0]/result6[0])*100
        self.eg_e_op.insert(END,("%"+str(round(ro1,2))))
        self.eg_e_op.configure(state='disabled')

        ro2 = (result2[0]/result6[1])*100
        self.eg_e_oc.insert(END,("%"+str(round(ro2,2))))
        self.eg_e_oc.configure(state='disabled')

        ro3 = (result[0]/result6[2])*100
        self.eg_e_ov.insert(END,("%"+str(round(ro3,2))))
        self.eg_e_ov.configure(state='disabled')
        conn.close()

        pass

class E_cliente(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ep_2 = tk.Label(self, text="Estadísticas por Cliente",bg="#16425B",fg='white',font=('Helvetica', 18, 'bold'))
        ep_2.place(x=210,y=35)

        div2 = tk.Label(self, text="_______________________________________________________",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 15, 'bold')).place(x=50,y=110)
        sub6 = tk.Label(self, text="ID",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=213,y=145)
        sub7 = tk.Label(self, text="Nombre",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=365,y=145)
        sub8 = tk.Label(self, text="Cant.",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=542,y=145)
        sub9 = tk.Label(self, text="Última compra",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=575,y=145)
        div3 = tk.Label(self, text="_______________________________________________________",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 15, 'bold')).place(x=50,y=210)
        sub10 = tk.Label(self, text="Tabla ordenada por ventas",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=120,y=245)
        sub10 = tk.Label(self, text="Tabla ordenada por ingresos",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=447,y=245)
        div4 = tk.Label(self, text="_______________________________________________________",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 15, 'bold')).place(x=50,y=510)
        #--------------------------labels 
        ec_tc = tk.Label(self, text="Total de clientes:",bg="#16425B",fg='white').place(x=50,y=100)
        ec_mac = tk.Label(self, text="Mayor consumidor:",bg="#16425B",fg='white').place(x=50,y=170)
        ec_mec = tk.Label(self, text="Menor consumidor:",bg="#16425B",fg='white').place(x=50,y=200)        
        #-------------------- total cliente
        self.ec_e_tc = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=5, height=1)
        self.ec_e_tc.place(x=206,y=100)

        #---------------------------------mayor consumidor
        self.ec_e_idmac = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=3, height=1)
        self.ec_e_idmac.place(x=206,y=170)
        
        self.ec_e_mac = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=38, height=1)
        self.ec_e_mac.place(x=236,y=170)

        self.ec_e_cmac = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=3, height=1)
        self.ec_e_cmac.place(x=546,y=170)

        self.ec_e_fmac = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=10, height=1)
        self.ec_e_fmac.place(x=576,y=170)
        #----------------------------------menor consumidor
        self.ec_e_idmec = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=3, height=1)
        self.ec_e_idmec.place(x=206,y=200)

        self.ec_e_mec = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=38, height=1)
        self.ec_e_mec.place(x=236,y=200)

        self.ec_e_cmec = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=3, height=1)
        self.ec_e_cmec.place(x=546,y=200)

        self.ec_e_fmec = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=10, height=1)
        self.ec_e_fmec.place(x=576,y=200)

        #---------------------------------función
        self.act_ecliente()

        #---------------------------tabla cliente x cantidad
        self.client_e_tabla = ttk.Treeview(self,height=4,columns=("ID","Nombre","Cantidad"))
        
        self.client_e_tabla.heading("ID",text="ID")
        self.client_e_tabla.heading("Nombre",text="Nombre")
        self.client_e_tabla.heading("Cantidad",text="Cantidad")

        self.client_e_tabla['show'] = 'headings'

        self.client_e_tabla.column("ID",minwidth=4,  width = 4)
        self.client_e_tabla.column("Nombre",minwidth=140, width = 140)
        self.client_e_tabla.column("Cantidad",minwidth=30, width = 30)

        self.client_e_tabla.place(x=50,y=270,width=280, height=250) ##

        self.showTablaCE()

        #---------------------------tabla cliente x promedio de compra
        self.client_e_tabla2 = ttk.Treeview(self,height=4,columns=("ID","Nombre","Cantidad"))
        
        self.client_e_tabla2.heading("ID",text="ID")
        self.client_e_tabla2.heading("Nombre",text="Nombre")
        self.client_e_tabla2.heading("Cantidad",text="Cantidad")

        self.client_e_tabla2['show'] = 'headings'

        self.client_e_tabla2.column("ID",minwidth=4,  width = 4)
        self.client_e_tabla2.column("Nombre",minwidth=140, width = 140)
        self.client_e_tabla2.column("Cantidad",minwidth=30, width = 30)

        self.client_e_tabla2.place(x=378,y=270,width=280, height=250) ##

        self.showTablaCE2()
        #---------------------------------boton
        act3 = tk.Button(self, text="Actualizar",height = 1, width = 10,bg="#fedc56", 
                                command=lambda: [self.showTablaCE(),self.act_ecliente()])
        act3.place(x=578,y=100)

    def showTablaCE(self):
        conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
        cursor = conn.cursor()
        cursor.execute("SELECT fc_compra.id_cliente, (SELECT fc_client.name FROM fc_client WHERE fc_compra.id_cliente = fc_client.id), COUNT(fc_compra.id_producto) FROM `fc_compra` GROUP BY fc_compra.id_cliente ORDER BY COUNT(fc_compra.id_cliente) DESC")
        result = cursor.fetchall()
        if len(result) != 0:
            self.client_e_tabla.delete(*self.client_e_tabla.get_children())
            for row in result:
                self.client_e_tabla.insert('',END,values=row)
                conn.commit()
        conn.close()
        pass

    def showTablaCE2(self):
        conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
        cursor = conn.cursor()
        cursor.execute("SELECT fc_compra.id_cliente, (SELECT fc_client.name FROM fc_client WHERE fc_compra.id_cliente = fc_client.id), SUM(fc_producto.p_cost) FROM fc_producto,fc_compra WHERE fc_producto.p_id = fc_compra.id_producto GROUP BY fc_compra.id_cliente ORDER BY SUM(fc_producto.p_cost) DESC")
        result = cursor.fetchall()
        if len(result) != 0:
            self.client_e_tabla2.delete(*self.client_e_tabla2.get_children())
            for row in result:
                self.client_e_tabla2.insert('',END,values=row)
                conn.commit()
        conn.close()
        pass

    def act_ecliente(self):
        self.ec_e_tc.configure(state='normal')
        self.ec_e_tc.delete('1.0',END)
        self.ec_e_idmac.configure(state='normal')
        self.ec_e_idmac.delete('1.0',END)
        self.ec_e_mac.configure(state='normal')
        self.ec_e_mac.delete('1.0',END)
        self.ec_e_fmac.configure(state='normal')
        self.ec_e_fmac.delete('1.0',END)
        self.ec_e_cmac.configure(state='normal')
        self.ec_e_cmac.delete('1.0',END)

        self.ec_e_idmec.configure(state='normal')
        self.ec_e_idmec.delete('1.0',END)
        self.ec_e_mec.configure(state='normal')
        self.ec_e_mec.delete('1.0',END)
        self.ec_e_fmec.configure(state='normal')
        self.ec_e_fmec.delete('1.0',END)
        self.ec_e_cmec.configure(state='normal')
        self.ec_e_cmec.delete('1.0',END)

        conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")

        # -----------------------------total clientes
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(fc_client.id) FROM `fc_client`")
        result = cursor.fetchall()
        self.ec_e_tc.insert(END,result)
        self.ec_e_tc.configure(state='disabled')
        # ----------------------------- mayor consumidor
        cursor1 = conn.cursor()
        cursor1.execute("SELECT fc_compra.id_cliente FROM `fc_compra` GROUP BY fc_compra.id_cliente ORDER BY COUNT(fc_compra.id_cliente) DESC LIMIT 1")
        result1 = cursor.fetchall()
        self.ec_e_idmac.insert(END,result1)
        self.ec_e_idmac.configure(state='disabled')

        cursor2 = conn.cursor()
        cursor2.execute("SELECT DISTINCT fc_client.name FROM fc_client,fc_compra WHERE fc_client.id = (SELECT fc_compra.id_cliente FROM `fc_compra` GROUP BY fc_compra.id_cliente ORDER BY COUNT(fc_compra.id_cliente) DESC LIMIT 1)")
        result2 = cursor.fetchone()
        self.ec_e_mac.insert(END,result2[0])
        self.ec_e_mac.configure(state='disabled')

        cursor2_1 = conn.cursor()
        cursor2_1.execute("SELECT fc_compra.c_fecha FROM `fc_compra` WHERE fc_compra.id_cliente = (SELECT fc_compra.id_cliente FROM `fc_compra` GROUP BY fc_compra.id_cliente ORDER BY COUNT(fc_compra.id_cliente) DESC LIMIT 1) ORDER BY fc_compra.c_id DESC LIMIT 1")
        result2_1 = cursor.fetchone()
        self.ec_e_fmac.insert(END,result2_1[0][0:10])
        self.ec_e_fmac.configure(state='disabled')

        cursor2_1_1 = conn.cursor()
        cursor2_1_1.execute("SELECT COUNT(fc_client.name) FROM fc_client,fc_compra WHERE fc_client.id = (SELECT fc_compra.id_cliente FROM `fc_compra` GROUP BY fc_compra.id_cliente ORDER BY COUNT(fc_compra.id_cliente) DESC LIMIT 1) AND fc_compra.id_cliente = fc_client.id")
        result2_1_1 = cursor.fetchall()
        self.ec_e_cmac.insert(END,result2_1_1)
        self.ec_e_cmac.configure(state='disabled')

        # ----------------------------- menor consumidor
        cursor3 = conn.cursor()
        cursor3.execute("SELECT fc_compra.id_cliente FROM `fc_compra` GROUP BY fc_compra.id_cliente ORDER BY COUNT(fc_compra.id_cliente) LIMIT 1")
        result3 = cursor.fetchall()
        self.ec_e_idmec.insert(END,result3)
        self.ec_e_idmec.configure(state='disabled')

        cursor4 = conn.cursor()
        cursor4.execute("SELECT DISTINCT fc_client.name FROM fc_client,fc_compra WHERE fc_client.id = (SELECT fc_compra.id_cliente FROM `fc_compra` GROUP BY fc_compra.id_cliente ORDER BY COUNT(fc_compra.id_cliente) LIMIT 1)")
        result4 = cursor.fetchone()
        self.ec_e_mec.insert(END,result4[0])
        self.ec_e_mec.configure(state='disabled')

        cursor4_1 = conn.cursor()
        cursor4_1.execute("SELECT fc_compra.c_fecha FROM `fc_compra` WHERE fc_compra.id_cliente = (SELECT fc_compra.id_cliente FROM `fc_compra` GROUP BY fc_compra.id_cliente ORDER BY COUNT(fc_compra.id_cliente) LIMIT 1) ORDER BY fc_compra.c_id DESC LIMIT 1")
        result4_1 = cursor.fetchone()
        self.ec_e_fmec.insert(END,result4_1[0][0:10])
        self.ec_e_fmec.configure(state='disabled')

        cursor5_1 = conn.cursor()
        cursor5_1.execute("SELECT COUNT(fc_client.name) FROM fc_client,fc_compra WHERE fc_client.id = (SELECT fc_compra.id_cliente FROM `fc_compra` GROUP BY fc_compra.id_cliente ORDER BY COUNT(fc_compra.id_cliente) LIMIT 1) AND fc_compra.id_cliente = fc_client.id")
        result5_1 = cursor.fetchall()
        self.ec_e_cmec.insert(END,result5_1)
        self.ec_e_cmec.configure(state='disabled')

        conn.close()
        pass

class E_Producto(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ep_2 = tk.Label(self, text="Estadísticas Por Producto",bg="#16425B",fg='white',font=('Helvetica', 18, 'bold'))
        ep_2.place(x=207,y=35)

        div2 = tk.Label(self, text="_______________________________________________________",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 15, 'bold')).place(x=50,y=110)
        sub2 = tk.Label(self, text="ID",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=217,y=145)
        sub3 = tk.Label(self, text="Costo",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=262,y=145)
        sub4 = tk.Label(self, text="ID",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=550,y=145)
        sub5 = tk.Label(self, text="Costo",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=595,y=145)
        div3 = tk.Label(self, text="_______________________________________________________",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 15, 'bold')).place(x=50,y=210)
        sub6 = tk.Label(self, text="ID",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=217,y=245)
        sub7 = tk.Label(self, text="Producto",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=350,y=245)
        sub8 = tk.Label(self, text="Cant.",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=538,y=245)
        sub9 = tk.Label(self, text="Costo",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=606,y=245)
        div4 = tk.Label(self, text="_______________________________________________________",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 15, 'bold')).place(x=50,y=310)
        sub10 = tk.Label(self, text="Tabla de productos ordenados por número de ventas",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 8, 'italic')).place(x=220,y=345)
        div4 = tk.Label(self, text="_______________________________________________________",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 15, 'bold')).place(x=50,y=510)
        ep_tp = tk.Label(self, text="Ventas de producto por tiempo:",bg="#16425B",fg='white').place(x=50,y=555)

        ep_tp = tk.Label(self, text="Total de productos:",bg="#16425B",fg='white').place(x=50,y=100)
        ep_pmb = tk.Label(self, text="Menor valor:",bg="#16425B",fg='white').place(x=50,y=170)
        ep_pmc = tk.Label(self, text="Mayor valor:",bg="#16425B",fg='white').place(x=50,y=200)
        
        ep_pvb = tk.Label(self, text="Menor valor (Vendido):",bg="#16425B",fg='white').place(x=384,y=170)
        ep_pvc = tk.Label(self, text="Mayor valor (Vendido):",bg="#16425B",fg='white').place(x=384,y=200)

        ep_pmev = tk.Label(self, text="Más vendido:",bg="#16425B",fg='white').place(x=50,y=270)
        ep_pmav = tk.Label(self, text="Menos vendido:",bg="#16425B",fg='white').place(x=50,y=300)
        
        #-------------------- total producto
        self.ep_e_tp = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=14, height=1)
        self.ep_e_tp.place(x=210,y=100)

        #---------------------------------menor valor
        self.ep_e_idpmb = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=3, height=1)
        self.ep_e_idpmb.place(x=210,y=170)

        self.ep_e_pmb = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=10, height=1)
        self.ep_e_pmb.place(x=240,y=170)
        #----------------------------------mayor valor
        self.ep_e_pmc = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=10, height=1)
        self.ep_e_pmc.place(x=240,y=200)

        self.ep_e_idpmc = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=3, height=1)
        self.ep_e_idpmc.place(x=210,y=200)
        #------------------------------    menor valor vendido
        self.ep_e_pvc = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=10, height=1)
        self.ep_e_pvc.place(x=574,y=170)

        self.ep_e_idpvc = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=3, height=1)
        self.ep_e_idpvc.place(x=544,y=170)
        #------------------------------  mayor valor vendido
        self.ep_e_pvb = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=10, height=1)
        self.ep_e_pvb.place(x=574,y=200)

        self.ep_e_idpvb = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=3, height=1)
        self.ep_e_idpvb.place(x=544,y=200)
        #---------------------------------producto más vendio
        self.ep_e_idpmav = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=3, height=1)
        self.ep_e_idpmav.place(x=210,y=270)

        self.ep_e_pmav = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=34, height=1)
        self.ep_e_pmav.place(x=240,y=270)

        self.ep_e_capmav = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=8, height=1)
        self.ep_e_capmav.place(x=519,y=270)

        self.ep_e_copmav = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=8, height=1)
        self.ep_e_copmav.place(x=590,y=270)
        #---------------------------------producto menos vendio
        self.ep_e_idpmev = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=3, height=1)
        self.ep_e_idpmev.place(x=210,y=300)

        self.ep_e_pmev = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=34, height=1)
        self.ep_e_pmev.place(x=240,y=300)

        self.ep_e_capmev = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=8, height=1)
        self.ep_e_capmev.place(x=519,y=300)

        self.ep_e_copmev = tk.Text(self,bg="#d9dcd6",fg="#16425B", width=8, height=1)
        self.ep_e_copmev.place(x=590,y=300)

        self.act_eproducto()

        #---------------------------tabla producto
        self.product_e_tabla = ttk.Treeview(self,height=4,columns=("ID","Producto","Marca","Costo","Vendidos"))
        
        self.product_e_tabla.heading("ID",text="ID")
        self.product_e_tabla.heading("Producto",text="Producto")
        self.product_e_tabla.heading("Marca",text="Marca")
        self.product_e_tabla.heading("Costo",text="Costo")
        self.product_e_tabla.heading("Vendidos",text="Vendidos")

        self.product_e_tabla['show'] = 'headings'

        self.product_e_tabla.column("ID",minwidth=18,  width = 18)
        self.product_e_tabla.column("Producto",minwidth=70, width = 70)
        self.product_e_tabla.column("Marca",minwidth=70, width = 70)
        self.product_e_tabla.column("Costo",minwidth=35, width = 30)
        self.product_e_tabla.column("Vendidos",minwidth=35, width = 30)

        self.product_e_tabla.place(x=50,y=375,width=610, height=148) ##

        self.showTablaPE()

        #---------------------------actualizar
        act3 = tk.Button(self, text="Actualizar",height = 1, width = 10,bg="#fedc56", 
                                        command=lambda: [self.showTablaPE(),self.act_eproducto()])
        act3.place(x=578,y=100)

        #---------------------------gráfoca
        act4 = tk.Button(self, text="Ver gráfica",height = 1, width = 10,bg="#fedc56", command = self.showGraphVT)
        act4.place(x=250,y=550)
    
    def showTablaPE(self):
        conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT fc_producto.p_id, fc_producto.p_name, fc_producto.p_brand, fc_producto.p_cost, (SELECT COUNT(*) FROM fc_compra WHERE fc_compra.id_producto = fc_producto.p_id) FROM fc_producto ORDER BY (SELECT COUNT(*) FROM fc_compra WHERE fc_compra.id_producto = fc_producto.p_id) DESC")
        result = cursor.fetchall()
        if len(result) != 0:
            self.product_e_tabla.delete(*self.product_e_tabla.get_children())
            for row in result:
                self.product_e_tabla.insert('',END,values=row)
                conn.commit()
        conn.close()
    
    def showGraphVT(self):
        conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
        cursor = conn.cursor()
        cursor.execute("SELECT fc_compra.c_fecha_m,COUNT(fc_compra.c_fecha_m) FROM fc_compra GROUP by fc_compra.c_fecha_m")
        result = cursor.fetchall()

        figure = plt.figure(num='Gráfica')
        
        plt.title('Ventas de producto por tiempo')
        plt.ylabel('Ventas')
        plt.xlabel('Meses')

        xf=[]
        yv=[]
        lb=[]
        for v in range(len(result)):
            xf.append(result[v][0])
            yv.append(result[v][1])
            lb.append(str(result[v][0]))

        axes = plt.bar(xf,yv, tick_label=lb)
        plt.show()
        conn.close()
        pass


    def act_eproducto(self):
        self.ep_e_tp.configure(state='normal')
        self.ep_e_tp.delete('1.0',END)
        self.ep_e_pmc.configure(state='normal')
        self.ep_e_pmc.delete('1.0',END)
        self.ep_e_pmb.configure(state='normal')
        self.ep_e_pmb.delete('1.0',END)
        self.ep_e_pvc.configure(state='normal')
        self.ep_e_pvc.delete('1.0',END)
        self.ep_e_pvb.configure(state='normal')
        self.ep_e_pvb.delete('1.0',END)
        self.ep_e_idpmc.configure(state='normal')
        self.ep_e_idpmc.delete('1.0',END)
        self.ep_e_idpmb.configure(state='normal')
        self.ep_e_idpmb.delete('1.0',END)
        self.ep_e_idpvc.configure(state='normal')
        self.ep_e_idpvc.delete('1.0',END)
        self.ep_e_idpvb.configure(state='normal')
        self.ep_e_idpvb.delete('1.0',END)

        self.ep_e_idpmav.configure(state='normal')
        self.ep_e_idpmav.delete('1.0',END)
        self.ep_e_pmav.configure(state='normal')
        self.ep_e_pmav.delete('1.0',END)
        self.ep_e_capmav.configure(state='normal')
        self.ep_e_capmav.delete('1.0',END)
        self.ep_e_copmav.configure(state='normal')
        self.ep_e_copmav.delete('1.0',END)

        self.ep_e_idpmev.configure(state='normal')
        self.ep_e_idpmev.delete('1.0',END)
        self.ep_e_pmev.configure(state='normal')
        self.ep_e_pmev.delete('1.0',END)
        self.ep_e_capmev.configure(state='normal')
        self.ep_e_capmev.delete('1.0',END)
        self.ep_e_copmev.configure(state='normal')
        self.ep_e_copmev.delete('1.0',END)
        
        conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
        # --------------------total producto
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(fc_producto.p_id) FROM `fc_producto`")
        result = cursor.fetchall()
        self.ep_e_tp.insert(END,result)
        self.ep_e_tp.configure(state='disabled')
        #---------------------producto más caro
        cursor1 = conn.cursor()
        cursor1.execute("SELECT MAX(fc_producto.p_cost) FROM fc_producto")
        result1 = cursor1.fetchone()
        self.ep_e_pmc.insert(END,"$ "+str(result1[0]))
        self.ep_e_pmc.configure(state='disabled')

        cursor1_1 = conn.cursor()
        cursor1_1.execute("SELECT p_id FROM fc_producto WHERE p_cost = (SELECT MAX(p_cost) FROM fc_producto)")
        result1_1 = cursor1.fetchall()
        self.ep_e_idpmc.insert(END,result1_1)
        self.ep_e_idpmc.configure(state='disabled')
        #--------------------producto más barato
        cursor2 = conn.cursor()
        cursor2.execute("SELECT MIN(fc_producto.p_cost) FROM fc_producto")
        result2 = cursor.fetchone()
        self.ep_e_pmb.insert(END,"$ "+str(result2[0]))
        self.ep_e_pmb.configure(state='disabled')
        
        cursor2_1 = conn.cursor()
        cursor2_1.execute("SELECT p_id FROM fc_producto WHERE p_cost = (SELECT MIN(p_cost) FROM fc_producto)")
        result2_1 = cursor.fetchall()
        self.ep_e_idpmb.insert(END,result2_1)
        self.ep_e_idpmb.configure(state='disabled')
        # ------------------------producto vendido más caro
        cursor3 = conn.cursor()
        cursor3.execute("SELECT MAX(fc_producto.p_cost) FROM fc_producto,fc_compra WHERE fc_producto.p_id = fc_compra.id_producto")
        result3 = cursor.fetchone()
        self.ep_e_pvc.insert(END,"$ "+str(result3[0]))
        self.ep_e_pvc.configure(state='disabled')

        cursor3_1 = conn.cursor()
        cursor3_1.execute("SELECT DISTINCT fc_producto.p_id FROM fc_producto,fc_compra WHERE fc_producto.p_cost = (SELECT MAX(fc_producto.p_cost) FROM fc_producto,fc_compra WHERE fc_producto.p_id = fc_compra.id_producto)")
        result3_1 = cursor.fetchall()
        self.ep_e_idpvc.insert(END,result3_1)
        self.ep_e_idpvc.configure(state='disabled')
        # -----------------------producto vendido más barato
        cursor4 = conn.cursor()
        cursor4.execute("SELECT MIN(fc_producto.p_cost) FROM fc_producto,fc_compra WHERE fc_producto.p_id = fc_compra.id_producto")
        result4 = cursor.fetchone()
        self.ep_e_pvb.insert(END,"$ "+str(result4[0]))
        self.ep_e_pvb.configure(state='disabled')

        cursor4_1 = conn.cursor()
        cursor4_1.execute("SELECT DISTINCT fc_producto.p_id FROM fc_producto,fc_compra WHERE fc_producto.p_cost = (SELECT MIN(fc_producto.p_cost) FROM fc_producto,fc_compra WHERE fc_producto.p_id = fc_compra.id_producto)")
        result4_1 = cursor.fetchall()
        self.ep_e_idpvb.insert(END,result4_1)
        self.ep_e_idpvb.configure(state='disabled')

        #-----------------------producto más vendido
        cursor5 = conn.cursor()
        cursor5.execute("SELECT fc_compra.id_producto FROM `fc_compra` GROUP BY fc_compra.id_producto ORDER BY COUNT(fc_compra.id_producto) DESC LIMIT 1")
        result5 = cursor.fetchall()
        self.ep_e_idpmav.insert(END,result5)
        self.ep_e_idpmav.configure(state='disabled')

        cursor5_1 = conn.cursor()
        cursor5_1.execute("SELECT DISTINCT fc_producto.p_name FROM fc_producto,fc_compra WHERE fc_producto.p_id = (SELECT fc_compra.id_producto FROM `fc_compra` GROUP BY fc_compra.id_producto ORDER BY COUNT(fc_compra.id_producto) DESC LIMIT 1)")
        result5_1 = cursor.fetchone()
        self.ep_e_pmav.insert(END,result5_1[0])
        self.ep_e_pmav.configure(state='disabled')

        cursor6 = conn.cursor()
        cursor6.execute("SELECT COUNT(fc_compra.c_id) FROM fc_compra,fc_producto WHERE fc_compra.id_producto = fc_producto.p_id AND fc_compra.id_producto = (SELECT fc_compra.id_producto FROM `fc_compra` GROUP BY fc_compra.id_producto ORDER BY COUNT(fc_compra.id_producto) DESC LIMIT 1)")
        result6 = cursor.fetchall()
        self.ep_e_capmav.insert(END,result6)
        self.ep_e_capmav.configure(state='disabled')

        cursor6_1 = conn.cursor()
        cursor6_1.execute("SELECT DISTINCT fc_producto.p_cost FROM fc_producto,fc_compra WHERE fc_producto.p_id = (SELECT fc_compra.id_producto FROM `fc_compra` GROUP BY fc_compra.id_producto ORDER BY COUNT(fc_compra.id_producto) DESC LIMIT 1)")
        result6_1 = cursor.fetchall()
        self.ep_e_copmav.insert(END,result6_1)
        self.ep_e_copmav.configure(state='disabled')

        #-----------------------producto menos vendido
        cursor7 = conn.cursor()
        cursor7.execute("SELECT fc_compra.id_producto FROM `fc_compra` GROUP BY fc_compra.id_producto ORDER BY COUNT(fc_compra.id_producto)  LIMIT 1")
        result7 = cursor.fetchall()
        self.ep_e_idpmev.insert(END,result7)
        self.ep_e_idpmev.configure(state='disabled')

        cursor7_1 = conn.cursor()
        cursor7_1.execute("SELECT DISTINCT fc_producto.p_name FROM fc_producto,fc_compra WHERE fc_producto.p_id = (SELECT fc_compra.id_producto FROM `fc_compra` GROUP BY fc_compra.id_producto ORDER BY COUNT(fc_compra.id_producto) LIMIT 1)")
        result7_1 = cursor.fetchone()
        self.ep_e_pmev.insert(END,result7_1[0])
        self.ep_e_pmev.configure(state='disabled')

        cursor8 = conn.cursor()
        cursor8.execute("SELECT COUNT(fc_compra.c_id) FROM fc_compra,fc_producto WHERE fc_compra.id_producto = fc_producto.p_id AND fc_compra.id_producto = (SELECT fc_compra.id_producto FROM `fc_compra` GROUP BY fc_compra.id_producto ORDER BY COUNT(fc_compra.id_producto)  LIMIT 1)")
        result8 = cursor.fetchall()
        self.ep_e_capmev.insert(END,result8)
        self.ep_e_capmev.configure(state='disabled')

        cursor8_1 = conn.cursor()
        cursor8_1.execute("SELECT DISTINCT fc_producto.p_cost FROM fc_producto,fc_compra WHERE fc_producto.p_id = (SELECT fc_compra.id_producto FROM `fc_compra` GROUP BY fc_compra.id_producto ORDER BY COUNT(fc_compra.id_producto) LIMIT 1)")
        result8_1 = cursor.fetchall()
        self.ep_e_copmev.insert(END,result8_1)
        self.ep_e_copmev.configure(state='disabled')

        conn.close()
        pass

class PageInventario(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ll = tk.Label(self, text="INVENTARIO",bg="#16425B",fg='white',font=('Helvetica', 18, 'bold'))
        ll.place(x=285,y=35)
    
        l_id = tk.Label(self, text="ID",bg="#16425B",fg='white').place(x=250,y=110)
        l_nm = tk.Label(self, text="Nombre",bg="#16425B",fg='white').place(x=250,y=140)
        l_mc = tk.Label(self, text="Marca",bg="#16425B",fg='white').place(x=250,y=170)
        l_cp = tk.Label(self, text="Costo",bg="#16425B",fg='white').place(x=250,y=200)     #costo producto
        l_s = tk.Label(self, text="Stock",bg="#16425B",fg='white').place(x=250,y=230)

        self.idd = Entry(self,bg="#d9dcd6",fg="#16425B")
        self.idd.place(x=340,y=110)
        self.namee = Entry(self,bg="#d9dcd6",fg="#16425B")
        self.namee.place(x=340,y=140)
        self.brandd = Entry(self,bg="#d9dcd6",fg="#16425B")
        self.brandd.place(x=340,y=170)
        self.costt= Entry(self,bg="#d9dcd6",fg="#16425B")
        self.costt.place(x=340,y=200)
        self.stockk= Entry(self,bg="#d9dcd6",fg="#16425B")
        self.stockk.place(x=340,y=230)

        # titulo = tk.Label(self, text="ID   Nombre    Marca    Costo     Contador",bg="#16425B",fg='white').place(x=350, y=80)
        # self.list = Listbox(self,selectbackground='#fedc56',selectforeground='black')
        # self.list.place(width=280, height=140,x=350,y=105)
        # self.showList()
        #lo nuevo mientras
        
        self.productTreeview = ttk.Treeview(self,height=4,columns=("ID","Producto","Marca","Costo","Stock"))
        
        self.productTreeview.heading("ID",text="ID")
        self.productTreeview.heading("Producto",text="Producto")
        self.productTreeview.heading("Marca",text="Marca")
        self.productTreeview.heading("Costo",text="Costo")
        self.productTreeview.heading("Stock",text="Stock")

        self.productTreeview['show'] = 'headings'

        self.productTreeview.column("ID",minwidth=4,  width = 4)
        self.productTreeview.column("Producto",minwidth=140, width = 140)
        self.productTreeview.column("Marca",minwidth=90, width = 90)
        self.productTreeview.column("Costo",minwidth=35, width = 30)
        self.productTreeview.column("Stock",minwidth=35, width = 30)

        self.productTreeview.place(x=60,y=320,width=600, height=230) ##

        self.showTreeView()

        #opciones
        self.btnAdd = tk.Button(self, text="Agregar",height = 1, width = 10,command=self.Add).place(x=140,y=272)
        self.btnGet = tk.Button(self, text="Mostrar",height = 1, width = 10,command=self.Get).place(x=230,y=272)
        self.btnUp = tk.Button(self, text="Modificar",height = 1, width = 10,command=self.Update).place(x=320,y=272)
        self.btnDel = tk.Button(self, text="Eliminar",height = 1, width = 10,bg='#bc544b', fg='#ffffff',command=self.Delete).place(x=410,y=272)
        self.btnRefresh = tk.Button(self,text="Actualizar",height = 1, width = 10,bg="#fedc56",command=self.showTreeView).place(x=500,y=272)
    
    def showTreeView(self):
        conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT fc_producto.p_id, fc_producto.p_name, fc_producto.p_brand, fc_producto.p_cost, fc_producto.p_stock FROM fc_producto")
        result = cursor.fetchall()
        if len(result) != 0:
            self.productTreeview.delete(*self.productTreeview.get_children())
            for row in result:
                self.productTreeview.insert('',END,values=row)
                conn.commit()
        conn.close()

    # def showList(self):
    #     conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
    #     cursor = conn.cursor()
    #     cursor.execute("select * from fc_producto")
    #     rows = cursor.fetchall()
    #     self.list.delete(0,'end')
    #     for row in rows:
    #         insertData = '   '+str(row[0])+'    '+row[1]+'        '+row[2]+'        '+str(row[3])+'        '+str(row[4])
    #         self.list.insert(self.list.size()+1, insertData)
    #     conn.close() 

    def Add(self):
        p_name = self.namee.get()
        p_brand = self.brandd.get()
        p_cost = self.costt.get()
        p_stock = self.stockk.get()

        if (p_name == "" or p_brand == "" or p_cost == "" or p_stock == ""):
            messagebox.showinfo("Error", "Se requiere llenar todos los campos")
        else:
            conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
            cursor = conn.cursor()
            cursor.execute("insert into fc_producto values('""','"+ p_name +"','"+ p_brand +"','"+ p_cost +"','"+ p_stock +"')")
            cursor.execute("commit")
            self.namee.delete(0,'end')
            self.brandd.delete(0,'end')
            self.costt.delete(0,'end')
            self.stockk.delete(0,'end')

            # self.showList()
            self.showTreeView()
            messagebox.showinfo("Estatus", "Agregado")
            conn.close()   
    
    def Delete(self):
        if(self.idd.get() == ""):
            messagebox.showinfo("Estatus", "Se requiere ingresar Id para eliminar un producto")
        else:
            conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
            cursor = conn.cursor()
            cursor.execute("delete from fc_producto where p_id ='"+ self.idd.get() +"'")
            cursor.execute("commit")
            
            self.idd.delete(0,'end')
            self.namee.delete(0,'end')
            self.brandd.delete(0,'end')
            self.costt.delete(0,'end')
            self.stockk.delete(0,'end')
            
            # self.showList()
            self.showTreeView()
            messagebox.showinfo("Estatus", "Eliminado")
            conn.close()
    
    def Update(self):
        p_id = self.idd.get()
        p_name = self.namee.get()
        p_brand = self.brandd.get()
        p_cost = self.costt.get()
        p_stock = self.stockk.get()

        if (p_name == "" or p_brand == "" or p_cost == ""or p_stock == ""):
            messagebox.showinfo("Error", "Se requiere llenar todos los campos")
        else:
            conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
            cursor = conn.cursor()
            cursor.execute("update fc_producto set p_name='" + p_name + "', p_brand='" + p_brand +"', p_cost='" + p_cost +"', p_stock='" + p_stock +"' where p_id ='"+ p_id +"'")
            cursor.execute("commit")
            self.namee.delete(0,'end')
            self.brandd.delete(0,'end')
            self.costt.delete(0,'end')
            self.stockk.delete(0,'end')
            
            # self.showList()
            self.showTreeView()
            messagebox.showinfo("Estatus", "Actualizado")
            conn.close()   
    
    def Get(self):
        if(self.idd.get() == ""):
            messagebox.showinfo("Estatus", "Se requiere ingresar Id para mostrar un producto")
        else:
            conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
            cursor = conn.cursor()
            cursor.execute("select * from fc_producto where p_id ='"+ self.idd.get() +"'")
            rows = cursor.fetchall()

            for row in rows:
                self.namee.insert(0, row[1])
                self.brandd.insert(0, row[2])
                self.costt.insert(0, row[3])
                self.stockk.insert(0, row[4])
                
            conn.close()

class Compra(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Compra",bg="#16425B",fg='white',font=('Helvetica', 18, 'bold'))
        label.place(x=310,y=35)

        div1 = tk.Label(self, text="_______________________________________________________",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 15, 'bold')).place(x=50,y=90)
        sub1 = tk.Label(self, text="Cliente",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 9, 'italic')).place(x=590,y=105)

        #bussqueda
        l_nm_busqueda = tk.Label(self, text="Buscar \npor nombre",bg="#16425B",fg='white').place(x=50,y=150)

        self.c_idd_busqueda = Entry(self,bg="#d9dcd6",fg="#16425B",width= 10)
        self.c_idd_busqueda.place(x=140,y=150)

        self.btnBusqueda = tk.Button(self, text="Buscar",height = 1, width = 6,command=self.filtrar).place(x=210,y=150)

        # treview
        self.bus_client_treeview = ttk.Treeview(self,height=4,columns=("ID","Nombre","Tel"))
        
        self.bus_client_treeview.heading("ID",text="ID")
        self.bus_client_treeview.heading("Nombre",text="Nombre")
        self.bus_client_treeview.heading("Tel",text="Tel")

        self.bus_client_treeview['show'] = 'headings'

        self.bus_client_treeview.column("ID",minwidth=4,  width = 4)
        self.bus_client_treeview.column("Nombre",minwidth=180, width = 180)
        self.bus_client_treeview.column("Tel",minwidth=80, width = 80)

        self.bus_client_treeview.place(x=300,y=147,width=360, height=170) ##

        l_id = tk.Label(self, text="ID",bg="#16425B",fg='white').place(x=50,y=200)
        l_nm = tk.Label(self, text="Nombre",bg="#16425B",fg='white').place(x=50,y=230)
        l_t = tk.Label(self, text="Teléfono",bg="#16425B",fg='white').place(x=50,y=260)

        self.c_idd = Entry(self,bg="#d9dcd6",fg="#16425B")
        self.c_idd.place(x=140,y=200)
        self.c_namee = Entry(self,bg="#d9dcd6",fg="#16425B")
        self.c_namee.place(x=140,y=230)
        self.c_tel = Entry(self,bg="#d9dcd6",fg="#16425B")
        self.c_tel.place(x=140,y=260)

        self.btnVer = tk.Button(self, text="Verificar",height = 1, width = 16,command=self.GetUser).place(x=140,y=292)

        div = tk.Label(self, text="_______________________________________________________",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 15, 'bold')).place(x=50,y=330)
        sub2 = tk.Label(self, text="Producto",bg="#16425B",fg='#d9dcd6',font=('Helvetica', 9, 'italic')).place(x=590,y=345)

        #compra / busqueda producto

        l_id = tk.Label(self, text="ID",bg="#16425B",fg='white').place(x=50,y=390)
        l_nm = tk.Label(self, text="Nombre",bg="#16425B",fg='white').place(x=50,y=420)
        l_t = tk.Label(self, text="Marca",bg="#16425B",fg='white').place(x=50,y=450)
        l_t = tk.Label(self, text="Costo",bg="#16425B",fg='white').place(x=50,y=480)

        self.pb_idd = Entry(self,bg="#d9dcd6",fg="#16425B")
        self.pb_idd.place(x=140,y=390)
        self.pb_namee = Entry(self,bg="#d9dcd6",fg="#16425B")
        self.pb_namee.place(x=140,y=420)
        self.pb_brandd = Entry(self,bg="#d9dcd6",fg="#16425B")
        self.pb_brandd.place(x=140,y=450)
        self.pb_cost = Entry(self,bg="#d9dcd6",fg="#16425B")
        self.pb_cost.place(x=140,y=480)

        self.btnMos = tk.Button(self, text="Mostrar",height = 1, width = 7,command=self.GetProduct).place(x=50,y=520)
        self.btnCom = tk.Button(self, text="Comprar",height = 1, width = 7,command=self.Compra).place(x=128,y=520)
        self.btnFin = tk.Button(self, text="Finalizar",height = 1, width = 7,command=lambda: 
                        [self.c_idd_busqueda.delete(0,END),self.c_idd.delete(0,END),self.c_namee.delete(0,END),
                        self.c_tel.delete(0,END),self.pb_idd.delete(0,END),self.pb_namee.delete(0,END),self.pb_brandd.delete(0,END),
                        self.pb_cost.delete(0,END),self.bus_client_treeview.delete(*self.bus_client_treeview.get_children()),
                        self.compra_treview.delete(*self.compra_treview.get_children()),controller.show_frame(Startpage)]).place(x=206,y=520)

        # treview
        self.compra_treview = ttk.Treeview(self,height=4,columns=("ID","Producto","Marca","Costo","F/H"))
        
        self.compra_treview.heading("ID",text="ID")
        self.compra_treview.heading("Producto",text="Producto")
        self.compra_treview.heading("Marca",text="Marca")
        self.compra_treview.heading("Costo",text="Costo")
        self.compra_treview.heading("F/H",text="F/H")

        self.compra_treview['show'] = 'headings'

        self.compra_treview.column("ID",minwidth=4,  width = 4)
        self.compra_treview.column("Producto",minwidth=78, width = 78)
        self.compra_treview.column("Marca",minwidth=36, width = 36)
        self.compra_treview.column("Costo",minwidth=27, width = 27)
        self.compra_treview.column("F/H",minwidth=70, width = 70)

        self.compra_treview.place(x=300,y=390,width=360, height=155) ##

    def filtrar (self):
        conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
        cursor = conn.cursor()
        cursor.execute("select * from fc_client where name like '%"+ self.c_idd_busqueda.get() +"%'")
        result = cursor.fetchall()
        if len(result) != 0:
            self.bus_client_treeview.delete(*self.bus_client_treeview.get_children())
            for row in result:
                self.bus_client_treeview.insert('',END,values=row)
                conn.commit()
        conn.close()

    def treeview_compra_usuario (self):
        conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
        cursor = conn.cursor()
        cursor.execute("SELECT fc_producto.p_id, fc_producto.p_name, fc_producto.p_brand, fc_producto.p_cost, fc_compra.c_fecha FROM fc_producto,fc_compra WHERE fc_producto.p_id = fc_compra.id_producto AND fc_compra.id_cliente = '"+ self.c_idd.get() +"'")
        result = cursor.fetchall()
        if len(result) != 0:
            self.compra_treview.delete(*self.compra_treview.get_children())
            for row in result:
                self.compra_treview.insert('',END,values=row)
                conn.commit()
        conn.close()

    def GetUser(self):
        self.c_namee.delete(0,END)
        self.c_tel.delete(0,END)
        if(self.c_idd.get() == ""):
            messagebox.showinfo("Estatus", "Se requiere ingresar Id para mostrar el cliente")
        else:
            conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
            cursor = conn.cursor()
            cursor.execute("select * from fc_client where id ='"+ self.c_idd.get() +"'")
            rows = cursor.fetchall()

            for row in rows:
                self.c_namee.insert(0, row[1])
                self.c_tel.insert(0, row[2])

            self.treeview_compra_usuario()   
            conn.close()
            
    def GetProduct(self):
        self.pb_namee.delete(0,END)
        self.pb_brandd.delete(0,END)
        self.pb_cost.delete(0,END)

        if(self.pb_idd.get() == ""):
            messagebox.showinfo("Estatus", "Se requiere ingresar Id para mostrar el producto")
        else:
            conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
            cursor = conn.cursor()
            cursor.execute("select * from fc_producto where p_id ='"+ self.pb_idd.get() +"'")
            rows = cursor.fetchall()

            for row in rows:
                self.pb_namee.insert(0, row[1])
                self.pb_brandd.insert(0, row[2])
                self.pb_cost.insert(0, row[3])

            conn.close()

    def Compra(self):
        id_cliente = self.c_idd.get()
        id_producto = self.pb_idd.get()
        
        self.now = datetime.now()
        self.dt_string = self.now.strftime("%d/%m/%Y %H:%M")
        self.dt_string_m = self.now.strftime("%m")
        
        if (id_cliente == "" or id_producto == ""):
            messagebox.showinfo("Error", "Se requiere ingresar los IDs de cliente y producto")
        else:
            
            conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
            cursor = conn.cursor()
            #AGREGAR LO DE LA FEHCA EN BD
            p_id=self.pb_idd.get()
            cursor.execute("select fc_producto.p_stock from fc_producto where fc_producto.p_id ='"+ p_id +"'")
            result = cursor.fetchone()
            if result[0] == 0:
                messagebox.showinfo("Stock - Estatus", "Este producto no esta en existencia")
            else:
                #------------------------- actualzar stock
                cursor = conn.cursor()
                stock_up = (result[0])-1
                cursor.execute("update fc_producto set p_stock='" + str(stock_up) +"' where p_id ='"+ p_id +"'")
                cursor.execute("commit")
                #------------------------- generar compra
                cursor = conn.cursor()
                cursor.execute("insert into fc_compra values('""','"+ id_cliente +"','"+ id_producto +"','"+ self.dt_string +"','"+ self.dt_string_m +"')")
                cursor.execute("commit")
                self.factura()
                self.pb_idd.delete(0,END)
                self.pb_namee.delete(0,END)
                self.pb_brandd.delete(0,END)
                self.pb_cost.delete(0,END)

                self.treeview_compra_usuario()
                messagebox.showinfo("Estatus", "¡Compra exitosa!")
                # self.factura()
            conn.close()  

    def factura(self):
        id_producto = self.pb_idd.get()
        pb_idf = self.pb_idd.get()
        pb_nameef = self.pb_namee.get()
        pb_costf = self.pb_cost.get()

        conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
        cursor = conn.cursor()
        cursor.execute("SELECT fc_compra.c_id FROM fc_compra ORDER by fc_compra.c_id desc LIMIT 1")
        id_cf = cursor.fetchone()

        conn = mysql.connect(host="localhost",port="3306",user="root",password="",database="fetchestDB")
        cursor = conn.cursor()
        cursor.execute("SELECT fc_compra.c_fecha FROM fc_compra ORDER by fc_compra.c_id desc LIMIT 1")
        id_ff = cursor.fetchone()
        id_ff = id_ff[0]
        #----------------------
        fileName = 'Factura'+str(id_cf[0])+'.pdf'
        documentTitle = 'FACTURA' + str(id_cf[0])
        title = 'FACTURA' + str(id_cf[0])
        productoslb = 'Id       Producto                                Importe'
        productoslb_co = 'Precio Unitario'
        prod_co = pb_costf; prod_id =pb_idf; prod_n =pb_nameef; prod_c =prod_co; prod_c2 =prod_co
        id_compra = ['Número de Factura',str(id_cf[0])]
        date = ['Fecha',id_ff[0:8]]

        # ------------- Create document 
        pdf = canvas.Canvas(fileName, pagesize=(700,450))
        pdf.setFontSize(150)
        pdf.setTitle(documentTitle)

        pdf.setFont("Courier", 12)
        pdf.drawString(450,140,"Subtotal = " + " $  " + prod_co)
        prod_coF = float(prod_co)
        pdf.drawString(485,105,"IVA = " + " $ " + (str(prod_coF*.16)))
        pdf.drawString(470,70,"Total = " + " $ " + (str(prod_coF+(prod_coF*.16))))

        pdf.setFont("Courier-Bold", 25)
        pdf.drawString(64,400,"FETCHEST")
        pdf.drawCentredString(550, 360, title)

        pdf.setFont("Courier-Bold", 11)
        pdf.drawCentredString(440,320, productoslb)
        pdf.drawCentredString(465,320, productoslb_co)

        pdf.setFont("Courier", 11)
        pdf.drawCentredString(262,300, prod_id)
        pdf.drawCentredString(331,300, prod_n)
        pdf.drawCentredString(460,300, prod_c)
        pdf.drawCentredString(599,300, prod_c2)
        # ------------------- Draw lines
        pdf.line(185, 390, 60, 390); pdf.line(250, 340, 650, 340)
        pdf.line(200, 340, 50, 340); pdf.line(200, 240, 50, 240)
        pdf.line(250, 160, 650, 160); pdf.line(430, 125, 650, 125)
        pdf.line(430, 90, 650, 90); pdf.line(430, 55, 650, 55)
        #--------------------------------------
        text = pdf.beginText(50, 315);text.setFont("Courier", 13)
        for line in id_compra:
            text.textLine(line)
        pdf.drawText(text)

        text2 = pdf.beginText(50, 215);text2.setFont("Courier", 13)
        for line in date:
            text2.textLine(line)
        pdf.drawText(text2)

        pdf.save()
        pass

app = MyApp()
app.geometry("720x600")
app.title("   Fetchest")
# app.iconbitmap('logo1.ico')
app.configure(bg='red')
app.resizable(False,False)
app.mainloop()