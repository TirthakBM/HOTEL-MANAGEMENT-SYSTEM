from os import stat
from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1121x452+234+243")

        ################ VARIABLES #############
        self.var_contact = StringVar()
        self.var_check_in = StringVar()
        self.var_check_out = StringVar()
        self.var_room_type = StringVar()
        self.var_room_available = StringVar()
        self.var_meal = StringVar()
        self.var_no_of_days = StringVar()
        self.var_paid_tax = StringVar()
        self.var_actual_total = StringVar()
        self.var_total = StringVar()


        ################ Title ##################
        lbl_title = Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1121,height=35)

        ################## Logo ######################
        img2 = Image.open("logohotel.png")
        img2 = img2.resize((100,35),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=35)

        ################ LABEL FRAME ###################
        lblFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOMBOOKING DETAILS",font=("times new roman",12,"bold"),padx=2)
        lblFrameLeft.place(x=5,y=40,width=425,height=410)

        ############### LABELS & ENTRIES ##############

        ############## CUSTOMER CONTACT. #################
        lbl_cust_contact= Label(lblFrameLeft,text="CUSTOMER CONTACT :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        
        entry_contact = ttk.Entry(lblFrameLeft,textvariable= self.var_contact,width=20,font=("arial",11,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        ############# FEATCH DATA BUTTON ##########
        btn_featch_data = Button(lblFrameLeft,command=self.fetch_contact,text="FETCH DATA",font=("arial",8,"bold"),bg="black",fg="gold",width=10)
        btn_featch_data.place(x=333,y=4)

        ############# CHECK IN DATE ################
        lblcheck_in_date = Label(lblFrameLeft,text="CHECK IN DATE :",font=("arial",10,"bold"),padx=2,pady=6)
        lblcheck_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(lblFrameLeft,textvariable=self.var_check_in,width=29,font=("arial",11,"bold"))
        txtcheck_in_date.grid(row=1,column=1)

        ############ CHECK OUT DATE ##############
        lblcheck_out_date = Label(lblFrameLeft,text="CHECK OUT DATE :",font=("arial",10,"bold"),padx=2,pady=6)
        lblcheck_out_date.grid(row=2,column=0,sticky=W)

        txtcheck_out_date=ttk.Entry(lblFrameLeft,textvariable=self.var_check_out,width=29,font=("arial",11,"bold"))
        txtcheck_out_date.grid(row=2,column=1)

        ############ ROOM TYPE ###############
        lblroom_type=Label(lblFrameLeft,text="ROOM TYPE :",font=("arial",10,"bold"),padx=2,pady=6)
        lblroom_type.grid(row=3,column=0,sticky=W)

        conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("Select ROOM_TYPE from details")
        data_rows = my_cursor.fetchall()

        combo_room_type = ttk.Combobox(lblFrameLeft,textvariable=self.var_room_type,font=("arial",10,"bold"),width=31,stat="readonly")
        combo_room_type["value"]=data_rows
        combo_room_type.current(0)
        combo_room_type.grid(row=3,column=1)

        ############ AVAILABLE ROOM ##########
        lblroom_available = Label(lblFrameLeft,text="ROOM AVAILABLE :",font=("arial",10,"bold"),padx=2,pady=6)
        lblroom_available.grid(row=4,column=0,sticky=W)

        conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("Select ROOM_NO from details")
        rows = my_cursor.fetchall()

        combo_room_no = ttk.Combobox(lblFrameLeft,textvariable=self.var_room_available,font=("arial",10,"bold"),width=31,stat="readonly")
        combo_room_no["value"]=rows
        combo_room_no.current(0)
        combo_room_no.grid(row=4,column=1)

        ############ MEAL ###############
        lblroom_meal = Label(lblFrameLeft,text="MEAL :",font=("arial",10,"bold"),padx=2,pady=6)
        lblroom_meal.grid(row=5,column=0,sticky=W)

        #txtroom_meal=ttk.Entry(lblFrameLeft,textvariable=self.var_meal,width=29,font=("arial",11,"bold"))
        #txtroom_meal.grid(row=5,column=1)

        combo_gender=ttk.Combobox(lblFrameLeft,textvariable=self.var_meal,font=("arial",10,"bold"),width=31,state="readonly")
        combo_gender["value"]=("Breakfast","Lunch","Dinner")
        combo_gender.current(0)
        combo_gender.grid(row=5,column=1)

        ########### NUMBER OF DAYS ################
        lblno_of_days = Label(lblFrameLeft,text="NO. OF DAYS :",font=("arial",10,"bold"),padx=2,pady=6)
        lblno_of_days.grid(row=6,column=0,sticky=W)

        txtno_of_days=ttk.Entry(lblFrameLeft,textvariable=self.var_no_of_days,width=29,font=("arial",11,"bold"),state="readonly")
        txtno_of_days.grid(row=6,column=1)

        ########## PAID TAX ###############
        lblno_of_days = Label(lblFrameLeft,text="PAID TAX :",font=("arial",10,"bold"),padx=2,pady=6)
        lblno_of_days.grid(row=7,column=0,sticky=W)

        txtno_of_days=ttk.Entry(lblFrameLeft,textvariable=self.var_paid_tax,width=29,font=("arial",11,"bold"),state="readonly")
        txtno_of_days.grid(row=7,column=1)

        ########### SUB TOTAL ################
        lblno_of_days = Label(lblFrameLeft,text="SUB TOTAL :",font=("arial",10,"bold"),padx=2,pady=6)
        lblno_of_days.grid(row=8,column=0,sticky=W)

        txtno_of_days=ttk.Entry(lblFrameLeft,textvariable=self.var_actual_total,width=29,font=("arial",11,"bold"),state="readonly")
        txtno_of_days.grid(row=8,column=1)

        ########## TOTAL COST ################
        lbLid_number = Label(lblFrameLeft,text="TOTAL COST :",font=("arial",10,"bold"),padx=2,pady=6)
        lbLid_number.grid(row=9,column=0,sticky=W)

        txtid_number = ttk.Entry(lblFrameLeft,textvariable=self.var_total,width=29,font=("arial",11,"bold"),state="readonly")
        txtid_number.grid(row=9,column=1)

        ############# BILL BUTTON ##########
        btn_bill_button = Button(lblFrameLeft,text="BILL",command=self.total,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btn_bill_button.grid(row=10,column=0,padx=5,sticky=W)

        ############## BUTTONS ##############
        btn_frame = Label(lblFrameLeft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=350,width=412,height=32)

        btn_add = Button(btn_frame,text="ADD",command=self.add_data,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btn_add.grid(row=0,column=0,padx=5)

        btn_update = Button(btn_frame,text="UPDATE",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btn_update.grid(row=0,column=1,padx=5)

        btn_delete = Button(btn_frame,text="DELETE",command=self.dat_Delete,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btn_delete.grid(row=0,column=2,padx=5)

        btn_reset = Button(btn_frame,text="RESET",command=self.reset,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btn_reset.grid(row=0,column=3,padx=5)

        ############## RIGHT SIDE IMAGE ################
        img3 = Image.open("room1.jpg")
        img3 = img3.resize((365,211),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1 = Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=750,y=38,width=365,height=211)
        ############## TABLE FRAME SEARCH ###############        
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="SEARCH AND VIEW DETAILS",font=("times new roman",12,"bold"),padx=2)
        table_frame.place(x=435,y=248,width=680,height=201)

        lblsearchby = Label(table_frame,text="SEARCH BY :",font=("arial",10,"bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=4)

        self.search_var = StringVar()

        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",10,"bold"),width=12,state="readonly")
        combo_search["value"]=("CONTACT","ROOM")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=4)

        self.txt_search = StringVar()
        entry_search = ttk.Entry(table_frame,textvariable=self.txt_search,width=29,font=("arial",11,"bold"))
        entry_search.grid(row=0,column=2,padx=4)

        btn_search = Button(table_frame,text="SEARCH",command=self.search_data,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btn_search.grid(row=0,column=3,padx=5)

        btn_showall = Button(table_frame,text="SHOW ALL!!",command=self.fetch_data,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btn_showall.grid(row=0,column=4,padx=5)

        ################ SHOW DATA TABLE ##############
        details_table = Label(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=34,width=674,height=148)

        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,columns=("CONTACT","CHECK_IN","CHECK_OUT","ROOM_TYPE","ROOM_AVAILABLE","MEAL","NO_OF_DAYS"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("CONTACT",text="CONTACT")
        self.room_table.heading("CHECK_IN",text="CHECK IN")
        self.room_table.heading("CHECK_OUT",text="CHECK OUT")
        self.room_table.heading("ROOM_TYPE",text="ROOM TYPE")
        self.room_table.heading("ROOM_AVAILABLE",text="ROOM AVAILABLE")
        self.room_table.heading("MEAL",text="MEAL")
        self.room_table.heading("NO_OF_DAYS",text="NO. OF DAYS")

        self.room_table["show"]="headings"

        self.room_table.column("CONTACT",width=100)
        self.room_table.column("CHECK_IN",width=100)
        self.room_table.column("CHECK_OUT",width=100)
        self.room_table.column("ROOM_TYPE",width=100)
        self.room_table.column("ROOM_AVAILABLE",width=100)
        self.room_table.column("MEAL",width=100)
        self.room_table.column("NO_OF_DAYS",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get()=="" or self.var_check_in.get()=="":
            messagebox.showerror("Error","ALL FIELDS ARE REQUIRED!!!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),self.var_check_in.get(),self.var_check_out.get(),self.var_room_type.get(),self.var_room_available.get(),self.var_meal.get(),
        self.var_no_of_days.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room booked!!!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from room")
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0]),
        self.var_check_in.set(row[1]),
        self.var_check_out.set(row[2]),
        self.var_room_type.set(row[3]),
        self.var_room_available.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_no_of_days.set(row[6])
        
        

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set CHECK_IN=%s,CHECK_OUT=%s,ROOM_TYPE=%s,ROOM_AVAILABLE=%s,MEAL=%s,NO_OF_DAYS=%s where CONTACT=%s",(self.var_check_in.get(),self.var_check_out.get(),self.var_room_type.get(),self.var_room_available.get(),self.var_meal.get(),self.var_no_of_days.get(),self.var_contact.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated sucessfully",parent=self.root)

    def dat_Delete(self):
        dat_Delete = messagebox.askyesno("Hotel Management System,","Do you want to remove this customers room",parent=self.root)
        if dat_Delete>0:
            conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
            my_cursor = conn.cursor()
            query = "delete from room where CONTACT=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not dat_Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set(""),
        self.var_check_in.set(""),
        self.var_check_out.set(""),
        self.var_room_type.set(""),
        self.var_room_available.set(""),
        self.var_meal.set(""),
        self.var_no_of_days.set("")
        self.var_paid_tax.set("")
        self.var_actual_total.set("")
        self.var_total.set("")

    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
            my_cursor = conn.cursor()
            query=("select NAME from customer where MOBILE=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

        if row==None:
            messagebox.showerror("Error","Number not found",parent=self.root)
        else:
            conn.commit()
            conn.close()

            showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
            showdataframe.place(x=445,y=55,width=300,height=180)

            ######## NAME ##############
            lblname=Label(showdataframe,text="NAME:",font=("arial",10,"bold"))
            lblname.place(x=0,y=0)

            lbl_data_name = Label(showdataframe,text=row,font=("arial",10,"bold"))
            lbl_data_name.place(x=110,y=0)

            ########### GENDER ###########
            conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
            my_cursor = conn.cursor()
            query=("select GENDER from customer where MOBILE=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

            lblgender=Label(showdataframe,text="GENDER:",font=("arial",10,"bold"))
            lblgender.place(x=0,y=30)

            lbl_data_gender = Label(showdataframe,text=row,font=("arial",10,"bold"))
            lbl_data_gender.place(x=110,y=30)

            ############ EMAIL ################
            conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
            my_cursor = conn.cursor()
            query=("select EMAIL from customer where MOBILE=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

            lblgender=Label(showdataframe,text="EMAIL:",font=("arial",10,"bold"))
            lblgender.place(x=0,y=60)

            lbl_data_gender = Label(showdataframe,text=row,font=("arial",10,"bold"))
            lbl_data_gender.place(x=110,y=60)
            
            ######## NATIONALITY ################
            conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
            my_cursor = conn.cursor()
            query=("select NATIONALITY from customer where MOBILE=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

            lblgender=Label(showdataframe,text="NATIONALITY:",font=("arial",10,"bold"))
            lblgender.place(x=0,y=90)

            lbl_data_gender = Label(showdataframe,text=row,font=("arial",10,"bold"))
            lbl_data_gender.place(x=110,y=90)

            ######### ADDRESS ##############
            conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
            my_cursor = conn.cursor()
            query=("select ADDRESS from customer where MOBILE=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

            lblgender=Label(showdataframe,text="ADDRESS:",font=("arial",10,"bold"))
            lblgender.place(x=0,y=120)

            lbl_data_gender = Label(showdataframe,text=row,font=("arial",10,"bold"))
            lbl_data_gender.place(x=110,y=120)

    
    ############## SEARCH ####################
    def search_data(self):
        conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows_featch = my_cursor.fetchall()
        if len(rows_featch)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows_featch:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def total(self):
        indate = self.var_check_in.get()
        outdate = self.var_check_out.get()
        indate=datetime.strptime(indate,"%d/%m/%Y")
        outdate=datetime.strptime(outdate,"%d/%m/%Y")
        self.var_no_of_days.set(abs(outdate-indate).days)

        if (self.var_meal.get()=="BreakFast" and self.var_room_type.get()=="LUXURY"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "RS."+str("%.2f"%((q5)*0.1))
            ST = "RS."+str("%.2f"%((q5)))
            TT = "RS."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_room_type.get()=="SINGLE"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "RS."+str("%.2f"%((q5)*0.1))
            ST = "RS."+str("%.2f"%((q5)))
            TT = "RS."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="BreakFast" and self.var_room_type.get()=="DUPLEX"):
            q1 = float(500)
            q2 = float(1000)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "RS."+str("%.2f"%((q5)*0.1))
            ST = "RS."+str("%.2f"%((q5)))
            TT = "RS."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_room_type.get()=="LUXURY"):
            q1 = float(1000)
            q2 = float(1500)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "RS."+str("%.2f"%((q5)*0.1))
            ST = "RS."+str("%.2f"%((q5)))
            TT = "RS."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_room_type.get()=="LUXURY"):
            q1 = float(1100)
            q2 = float(1600)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "RS."+str("%.2f"%((q5)*0.1))
            ST = "RS."+str("%.2f"%((q5)))
            TT = "RS."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Breakfast" and self.var_room_type.get()=="SINGLE"):
            q1 = float(250)
            q2 = float(600)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "RS."+str("%.2f"%((q5)*0.1))
            ST = "RS."+str("%.2f"%((q5)))
            TT = "RS."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_room_type.get()=="SINGLE"):
            q1 = float(300)
            q2 = float(800)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "RS."+str("%.2f"%((q5)*0.1))
            ST = "RS."+str("%.2f"%((q5)))
            TT = "RS."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_room_type.get()=="DUPLEX"):
            q1 = float(550)
            q2 = float(1000)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "RS."+str("%.2f"%((q5)*0.1))
            ST = "RS."+str("%.2f"%((q5)))
            TT = "RS."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_room_type.get()=="DUPLEX"):
            q1 = float(500)
            q2 = float(1100)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "RS."+str("%.2f"%((q5)*0.1))
            ST = "RS."+str("%.2f"%((q5)))
            TT = "RS."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="BreakFast" and self.var_room_type.get()=="DOUBLE"):
            q1 = float(400)
            q2 = float(900)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "RS."+str("%.2f"%((q5)*0.1))
            ST = "RS."+str("%.2f"%((q5)))
            TT = "RS."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_room_type.get()=="DOUBLE"):
            q1 = float(500)
            q2 = float(900)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "RS."+str("%.2f"%((q5)*0.1))
            ST = "RS."+str("%.2f"%((q5)))
            TT = "RS."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_room_type.get()=="DOUBLE"):
            q1 = float(500)
            q2 = float(1000)
            q3 = float(self.var_no_of_days.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "RS."+str("%.2f"%((q5)*0.1))
            ST = "RS."+str("%.2f"%((q5)))
            TT = "RS."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paid_tax.set(Tax)
            self.var_actual_total.set(ST)
            self.var_total.set(TT)

        







if __name__ == "__main__":
    root=Tk()
    Obj=Roombooking(root)
    root.mainloop()