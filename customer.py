from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1121x452+234+243")

        ############### VARIABLES ###############
        self.var_ref = StringVar()
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_cust_mother = StringVar()
        self.var_cust_gender = StringVar()
        self.var_cust_post = StringVar()
        self.var_cust_mobile = StringVar()
        self.var_cust_email = StringVar()
        self.var_cust_nationality = StringVar()
        self.var_cust_id_proff = StringVar()
        self.var_cust_id_number = StringVar()
        self.var_cust_address = StringVar()


        ################ Title ##################
        lbl_title = Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1121,height=35)

        ################## Logo ######################
        img2 = Image.open("logohotel.png")
        img2 = img2.resize((100,35),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=35)

        ################ LABEL FRAME ###################
        lblFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DETAILS",font=("times new roman",12,"bold"),padx=2)
        lblFrameLeft.place(x=5,y=40,width=425,height=410)

        ############### LABELS & ENTRIES ##############

        ############## REFRENCE NO. #################
        lbl_cust_ref = Label(lblFrameLeft,text="CUSTOMER REF :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        
        entry_ref = ttk.Entry(lblFrameLeft,textvariable=self.var_ref,width=29,font=("arial",11,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        ############## CUSTOMER NAME ##############
        lbl_cust_name = Label(lblFrameLeft,text="CUSTOMER NAME :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)
        
        entry_name = ttk.Entry(lblFrameLeft,textvariable=self.var_cust_name,width=29,font=("arial",11,"bold"))
        entry_name.grid(row=1,column=1)

        ############# MOTHERS NAME ###############
        lbl_cust_mname = Label(lblFrameLeft,text="MOTHER NAME :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_mname.grid(row=2,column=0,sticky=W)
        
        entry_mname = ttk.Entry(lblFrameLeft,textvariable=self.var_cust_mother,width=29,font=("arial",11,"bold"))
        entry_mname.grid(row=2,column=1)

        ############ GENDER BOX ###############
        lbl_gender = Label(lblFrameLeft,font=("arial",10,"bold"),text="GENDER :",padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)
        
        combo_gender=ttk.Combobox(lblFrameLeft,textvariable=self.var_cust_gender,font=("arial",10,"bold"),width=31,state="readonly")
        combo_gender["value"]=("MALE","FEMALE","OTHERS")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        ########### POST CODE ###############
        lbl_cust_post = Label(lblFrameLeft,text="POST CODE :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_post.grid(row=4,column=0,sticky=W)
        
        entry_post = ttk.Entry(lblFrameLeft,textvariable=self.var_cust_post,width=29,font=("arial",11,"bold"))
        entry_post.grid(row=4,column=1)

        ########## MOBILE NUMBER ##############
        lbl_cust_mob = Label(lblFrameLeft,text="MOBILE :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_mob.grid(row=5,column=0,sticky=W)
        
        entry_mob = ttk.Entry(lblFrameLeft,textvariable=self.var_cust_mobile,width=29,font=("arial",11,"bold"))
        entry_mob.grid(row=5,column=1)

        ########## EMAIL ##################
        lbl_cust_email = Label(lblFrameLeft,text="EMAIL :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_email.grid(row=6,column=0,sticky=W)
        
        entry_email = ttk.Entry(lblFrameLeft,textvariable=self.var_cust_email,width=29,font=("arial",11,"bold"))
        entry_email.grid(row=6,column=1)

        ########### NATIONALITY ##############
        lblNationality = Label(lblFrameLeft,font=("arial",10,"bold"),text="NATIONALITY :",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)
        
        combo_nationality=ttk.Combobox(lblFrameLeft,textvariable=self.var_cust_nationality,font=("arial",10,"bold"),width=31,state="readonly")
        combo_nationality["value"]=("AMERICAN","BRITISH","INDIAN")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)

        ############ IDPROFF TYPE #############
        lblIdproff = Label(lblFrameLeft,font=("arial",10,"bold"),text="ID PROFF TYPE :",padx=2,pady=6)
        lblIdproff.grid(row=8,column=0,sticky=W)
        
        combo_idproff=ttk.Combobox(lblFrameLeft,textvariable=self.var_cust_id_proff,font=("arial",10,"bold"),width=31,state="readonly")
        combo_idproff["value"]=("AADHAR CARD","PASSPORT","DRIVING LICIENCE","PAN CARD")
        combo_idproff.current(0)
        combo_idproff.grid(row=8,column=1)

        ############ ID NUMBER #################
        lbl_cust_idno = Label(lblFrameLeft,text="ID NUMBER :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_idno.grid(row=9,column=0,sticky=W)
        
        entry_idno = ttk.Entry(lblFrameLeft,textvariable=self.var_cust_id_number,width=29,font=("arial",11,"bold"))
        entry_idno.grid(row=9,column=1)

        ########### ADDRESS #################
        lbl_cust_addr = Label(lblFrameLeft,text="ADDRESS :",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_cust_addr.grid(row=10,column=0,sticky=W)
        
        entry_addr = ttk.Entry(lblFrameLeft,textvariable=self.var_cust_address,width=29,font=("arial",11,"bold"))
        entry_addr.grid(row=10,column=1)

        ############## BUTTONS ##############
        btn_frame = Label(lblFrameLeft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=352,width=412,height=32)

        btn_add = Button(btn_frame,text="ADD",command=self.add_data,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btn_add.grid(row=0,column=0,padx=5)

        btn_update = Button(btn_frame,text="UPDATE",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btn_update.grid(row=0,column=1,padx=5)

        btn_delete = Button(btn_frame,text="DELETE",command=self.dat_Delete,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btn_delete.grid(row=0,column=2,padx=5)

        btn_reset = Button(btn_frame,text="RESET",command=self.data_reset,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btn_reset.grid(row=0,column=3,padx=5)

        ############## TABLE FRAME SEARCH ###############        
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="SEARCH AND VIEW DETAILS",font=("times new roman",12,"bold"),padx=2)
        table_frame.place(x=435,y=40,width=680,height=410)

        lblsearchby = Label(table_frame,text="SEARCH BY :",font=("arial",10,"bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=4)

        self.search_var = StringVar()

        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",10,"bold"),width=12,state="readonly")
        combo_search["value"]=("MOBILE","REF_NO")
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
        details_table.place(x=0,y=34,width=674,height=350)

        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_details_table=ttk.Treeview(details_table,columns=("REF_NO","NAME","MOTHER","GENDER","POST","MOBILE","EMAIL","NATIONALITY","ID_PROFF","ID_NO","ADDRESS"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.Cust_details_table.xview)
        Scroll_y.config(command=self.Cust_details_table.yview)

        self.Cust_details_table.heading("REF_NO",text="REFER NO.")
        self.Cust_details_table.heading("NAME",text="NAME")
        self.Cust_details_table.heading("MOTHER",text="MOTHER")
        self.Cust_details_table.heading("GENDER",text="GENDER")
        self.Cust_details_table.heading("POST",text="POST")
        self.Cust_details_table.heading("MOBILE",text="MOBILE")
        self.Cust_details_table.heading("EMAIL",text="EMAIL")
        self.Cust_details_table.heading("NATIONALITY",text="NATIONALITY")
        self.Cust_details_table.heading("ID_PROFF",text="ID PROFF.")
        self.Cust_details_table.heading("ID_NO",text="ID NO.")
        self.Cust_details_table.heading("ADDRESS",text="ADDRESS")

        self.Cust_details_table["show"]="headings"

        self.Cust_details_table.column("REF_NO",width=100)
        self.Cust_details_table.column("NAME",width=100)
        self.Cust_details_table.column("MOTHER",width=100)
        self.Cust_details_table.column("GENDER",width=100)
        self.Cust_details_table.column("POST",width=100)
        self.Cust_details_table.column("MOBILE",width=100)
        self.Cust_details_table.column("EMAIL",width=100)
        self.Cust_details_table.column("NATIONALITY",width=100)
        self.Cust_details_table.column("ID_PROFF",width=100)
        self.Cust_details_table.column("ID_NO",width=100)
        self.Cust_details_table.column("ADDRESS",width=100)

        self.Cust_details_table.pack(fill=BOTH,expand=1)
        self.Cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_cust_mobile.get()=="" or self.var_cust_mother.get()=="":
            messagebox.showerror("Error","ALL FIELDS ARE REQUIRED!!!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),self.var_cust_name.get(),self.var_cust_mother.get(),self.var_cust_gender.get(),self.var_cust_post.get(),self.var_cust_mobile.get(),self.var_cust_email.get(),self.var_cust_nationality.get(),self.var_cust_id_proff.get(),self.var_cust_id_number.get(),self.var_cust_address.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from customer")
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for i in rows:
                self.Cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.Cust_details_table.focus()
        content = self.Cust_details_table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_cust_mother.set(row[2]),
        self.var_cust_gender.set(row[3]),
        self.var_cust_post.set(row[4]),
        self.var_cust_mobile.set(row[5]),
        self.var_cust_email.set(row[6]),
        self.var_cust_nationality.set(row[7]),
        self.var_cust_id_proff.set(row[8]),
        self.var_cust_id_number.set(row[9]),
        self.var_cust_address.set(row[10])

    def update(self):
        if self.var_cust_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set NAME=%s,MOTHER=%s,GENDER=%s,POST=%s,MOBILE=%s,EMAIL=%s,NATIONALITY=%s,ID_PROFF=%s,ID_NO=%s,ADDRESS=%s where REF_NO=%s",(self.var_cust_name.get(),self.var_cust_mother.get(),self.var_cust_gender.get(),self.var_cust_post.get(),self.var_cust_mobile.get(),self.var_cust_email.get(),self.var_cust_nationality.get(),self.var_cust_id_proff.get(),self.var_cust_id_number.get(),self.var_cust_address.get(),self.var_ref.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated sucessfully",parent=self.root)

    def dat_Delete(self):
        dat_Delete = messagebox.askyesno("Hotel Management System,","Do you want to delete this customer",parent=self.root)
        if dat_Delete>0:
            conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
            my_cursor = conn.cursor()
            query = "delete from customer where REF_NO=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not dat_Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def data_reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_cust_mother.set(""),
        #self.var_cust_gender.set(""),
        self.var_cust_post.set(""),
        self.var_cust_mobile.set(""),
        self.var_cust_email.set(""),
        #self.var_cust_nationality.set(""),
        #self.var_cust_id_proff.set(""),
        self.var_cust_id_number.set(""),
        self.var_cust_address.set("")

        x = random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search_data(self):
        conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows_featch = my_cursor.fetchall()
        if len(rows_featch)!=0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for i in rows_featch:
                self.Cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()    
            

        

if __name__ == "__main__":
    root=Tk()
    Obj=Cust_Win(root)
    root.mainloop()