import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os , sys
import tempfile

class Store:
    def __init__(self,window):
        self.win=window

        self.categories=["Kurti","Legis","Shirt","Jeans"]

        self.kurti=["Kurti1","Kurt2","Kurt3","Kurt4"]
        self.legis=["Legis1","Legis2","Legis3","Legis4"]
        self.shirt=["Shirt1","Shirt2","Shirt3","Shirt4"]
        self.jeans=["Jeans1","Jeans2","Jeans3","Jeans4"]

        #Create Variable
        self.cname=StringVar()
        self.cmob=StringVar()
        self.cbill=StringVar()

        self.price=IntVar()
        self.qty=IntVar()

        self.tlist=[]

        self.win.geometry("1550x800+0+0")
        space=" "
        self.win.title(space*200+"Bảng thanh toán")
        heading=Label(self.win,text="Welcome to Circle T",background="red",fg="white",font=("Goudy Stout",15))
        heading.pack(fill=X,ipady=10)
        # heading.place(x=0,y=0)



        main_frame=Frame(self.win,background="red")
        main_frame.pack(fill="both",expand=1)

        # ======================================================================
        logo = Image.open("Circle_K_logo_2016.svg.png")
        logo = logo.resize((900, 150), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)
        logo_label = Label(self.win, image=logo, bg="red")
        logo_label.image = logo
        # logo_label.pack(fill=X,ipady=10)
        logo_label.place(x=400, y=0)

        # ======================================================================


        customer_frame=LabelFrame(main_frame,pady=10,height=100,background="white",text="Thông tin Order",font=("Elephant",15))
        customer_frame.place(x=0,y=100,width=1550)

        form_frame=LabelFrame(main_frame,height=500,pady=100,padx=60,width=550,background="red",text="Thông tin sản phẩm",font=("Elephant",15))
        form_frame.place(x=0,y=250)

        table_frame=LabelFrame(main_frame,height=500,width=1000,background="white",text="Chi tiết Order",font=("Elephant",15))
        table_frame.place(x=550,y=200)

        button_frame=LabelFrame(main_frame,height=100,width=1550,background="orange",font=("Elephant",15))
        button_frame.place(x=0,y=700)

        #customer details
        Customer_Name_lbl=Label(customer_frame,text="Customer_ID",font=("times new roman",15))
        Customer_Name_lbl.place(x=10,y=0,width=200)
        Customer_Name_txt=Entry(customer_frame,font=("times new roman",15),textvariable=self.cname)
        Customer_Name_txt.place(x=250,y=0)

        Customer_Mob_lbl=Label(customer_frame,text="Employee_ID",font=("times new roman",15))
        Customer_Mob_lbl.place(x=500,y=0,width=200)
        Customer_Mob_txt=Entry(customer_frame,font=("times new roman",15),textvariable=self.cmob)
        Customer_Mob_txt.place(x=750,y=0)

        Customer_Billno_lbl=Label(customer_frame,text="Order_ID",font=("times new roman",15))
        Customer_Billno_lbl.place(x=1000,y=0,width=200)
        Customer_Billno_txt=Entry(customer_frame,font=("times new roman",15),textvariable=self.cbill)
        Customer_Billno_txt.place(x=1250,y=0)

        #Product Details
        Product_Cat=Label(form_frame,text="Loại hàng",font=("times new roman",15))
        Product_Cat.place(x=20,y=0,width=120)
        self.categories.insert(0,"Chọn loại hàng")
        self.Product_Cat_List=ttk.Combobox(form_frame,font=("times new roman",15),values=self.categories)
        self.Product_Cat_List.current(0)
        self.Product_Cat_List.place(x=170,y=0,width=200)

        self.Product_Cat_List.bind('<<ComboboxSelected>>',self.cat)

        Product_Sub=Label(form_frame,text="Sub Category",font=("times new roman",15))
        Product_Sub.place(x=20,y=50,width=120)
        self.Product_Sub_List=ttk.Combobox(form_frame,font=("times new roman",15))
        self.Product_Sub_List.place(x=170,y=50,width=200)

        Product_Rate_lbl=Label(form_frame,text="Price",font=("times new roman",15))
        Product_Rate_lbl.place(x=20,y=100,width=120)
        Product_Rate_txt=Entry(form_frame,font=("times new roman",15),textvariable=self.price)
        Product_Rate_txt.place(x=170,y=100,width=200)

        Product_Qty_lbl=Label(form_frame,text="Quantity",font=("times new roman",15))
        Product_Qty_lbl.place(x=20,y=150,width=120)
        Product_Qty_txt=Entry(form_frame,font=("times new roman",15),textvariable=self.qty)
        Product_Qty_txt.place(x=170,y=150,width=200)

        #Billing Area
        scrolly=Scrollbar(table_frame,orient=VERTICAL)
        self.billarea=Text(table_frame,yscrollcommand=scrolly.set,font=("times new roman",15))
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.billarea.yview)
        self.billarea.pack(fill=BOTH,expand=1)

        #Button
        self.Add_Item_Btn=Button(button_frame,text="Add Item",font=("times new roman",15),command=self.addItem)
        self.Add_Item_Btn.place(x=50,y=0,width=200)

        self.Calc_Bill_Btn=Button(button_frame,text="Calculate Bill",font=("times new roman",15),command=self.makeBill)
        self.Calc_Bill_Btn.place(x=300,y=0,width=200)

        self.Reset_Btn=Button(button_frame,text="Reset",font=("times new roman",15),command=self.reset)
        self.Reset_Btn.place(x=1050,y=0,width=200)

        self.Exit_Btn=Button(button_frame,text="Exit",font=("times new roman",15),command=self.quit)
        self.Exit_Btn.place(x=1300,y=0,width=200)

        self.heading()



    def cat(self,e=' '):
        if self.Product_Cat_List.get()=="Kurti":
            self.Product_Sub_List.config(values=self.kurti)
            self.Product_Sub_List.current(0)
        elif self.Product_Cat_List.get()=="Legis":
            self.Product_Sub_List.config(values=self.legis)
            self.Product_Sub_List.current(0)
        elif self.Product_Cat_List.get()=="Shirt":
            self.Product_Sub_List.config(values=self.shirt)
            self.Product_Sub_List.current(0)
        elif self.Product_Cat_List.get()=="Jeans":
            self.Product_Sub_List.config(values=self.jeans)
            self.Product_Sub_List.current(0)

    def addItem(self):
        if self.Product_Cat_List.get()=="Select Category":
            messagebox.showinfo("info","please select categories")
        elif self.price.get()==0:
            messagebox.showinfo("info","please enter price")
        elif self.qty.get()==0:
            messagebox.showinfo("info","please enter quantity")
        else:
            r=self.price.get()
            q=self.qty.get()
            t=r*q
            self.tlist.append(t)
            print(self.tlist)
            self.billarea.insert(END,f'\n {self.Product_Sub_List.get()}\t\t {r} \t {q} \t {t}')

    def makeBill(self):
        if len(self.cname.get())==0 and len(self.cmob.get())==0 and len(self.cbill.get())==0:
            messagebox.showinfo("info","please enter customer detail")
        elif self.Product_Cat_List.get()=="Select Category":
            messagebox.showinfo("info","please select categories")
        elif self.price.get()==0:
            messagebox.showinfo("info","please enter price")
        elif self.qty.get()==0:
            messagebox.showinfo("info","please enter quantity")
        else:
            space=" "
            total=sum(self.tlist)
            self.billarea.insert(3.16,self.cname.get())
            self.billarea.insert(4.16 ,self.cmob.get())
            self.billarea.insert(5.16,self.cbill.get())
            self.billarea.insert(END,"\n ++++++++++++++++++++++++++++++++++++++++++++++++")
            self.billarea.insert(END,f'\n Tổng tiền các sản phẩm:{space*20} {total}')
            self.billarea.insert(END,f'\n VAT(10%):{space*40} {total*0.1}')
            self.billarea.insert(END,f'\n Tổng tiền hoá đơn:{space*30} {total+(total*0.1)}')


    def reset(self):
        self.billarea.delete(1.0,END)
        self.heading()

    def quit(self):
        win.destroy()

    def heading(self):
        self.billarea.delete(1.0,END)
        self.billarea.insert(END,"\t\t\t\t Hoá đơn ")
        self.billarea.insert(END,"\n\t================================================================")
        self.billarea.insert(END,f'\n Custome Name:\t')
        self.billarea.insert(END,f'\n Employee ID:\t')
        self.billarea.insert(END,f'\n Order ID:\t')
        self.billarea.insert(END,f'\n Product Name \t\t Price \t Quantity \t Total')


if __name__=='__main__':
    win=tk.Tk()
    app=Store(win)
    win.mainloop()