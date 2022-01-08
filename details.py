from os import stat
from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Detailsroom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1121x452+234+243")

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
        lblFrameLeft=LabelFrame(self.root,bd=2,relief=RIDGE,text="NEW ROOM ADD",font=("times new roman",12,"bold"),padx=2)
        lblFrameLeft.place(x=5,y=40,width=460,height=350)

        ############## FLOOR #################
        lbl_floor= Label(lblFrameLeft,text="FLOOR ",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        
        self.var_floor=StringVar()
        entry_floor = ttk.Entry(lblFrameLeft,textvariable=self.var_floor,width=20,font=("arial",11,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

        ############## ROOM NUMBER #################
        lbl_room_no= Label(lblFrameLeft,text="ROOM NO. ",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_room_no.grid(row=1,column=0,sticky=W)
        
        self.var_room_no=StringVar()
        entry_room_no = ttk.Entry(lblFrameLeft,textvariable=self.var_room_no,width=20,font=("arial",11,"bold"))
        entry_room_no.grid(row=1,column=1,sticky=W)

        ############## ROOM TYPE #################
        lbl_room_TYPE= Label(lblFrameLeft,text="ROOM TYPE. ",font=("arial",10,"bold"),padx=2,pady=6)
        lbl_room_TYPE.grid(row=2,column=0,sticky=W)
        
        self.var_room_type=StringVar()
        #entry_room_TYPE = ttk.Entry(lblFrameLeft,textvariable=self.var_room_type,width=20,font=("arial",11,"bold"))
        #entry_room_TYPE.grid(row=2,column=1,sticky=W)

        combo_gender=ttk.Combobox(lblFrameLeft,textvariable=self.var_room_type,font=("arial",10,"bold"),width=31,state="readonly")
        combo_gender["value"]=("LUXURY","DUPLEX","SINGLE","DOUBLE")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)

        ############## BUTTONS ##############
        btn_frame = Label(lblFrameLeft,bd=2,relief=RIDGE)
        btn_frame.place(x=15,y=200,width=412,height=32)

        btn_add = Button(btn_frame,text="ADD",command=self.add_data,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btn_add.grid(row=0,column=0,padx=5)

        btn_update = Button(btn_frame,text="UPDATE",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btn_update.grid(row=0,column=1,padx=5)

        btn_delete = Button(btn_frame,text="DELETE",command=self.dat_Delete,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btn_delete.grid(row=0,column=2,padx=5)

        btn_reset = Button(btn_frame,text="RESET",command=self.reset,font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btn_reset.grid(row=0,column=3,padx=5)

        ############## TABLE FRAME SEARCH ###############        
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="SHOW ROOM DETAILS",font=("times new roman",12,"bold"),padx=2)
        table_frame.place(x=500,y=40,width=600,height=350)

        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(table_frame,columns=("FLOOR","ROOM_NO","ROOM_TYPE"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("FLOOR",text="FLOOR")
        self.room_table.heading("ROOM_NO",text="ROOM NO.")
        self.room_table.heading("ROOM_TYPE",text="ROOM TYPE")

        self.room_table["show"]="headings"

        self.room_table.column("FLOOR",width=100)
        self.room_table.column("ROOM_NO",width=100)
        self.room_table.column("ROOM_TYPE",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get()=="" or self.var_room_type.get()=="":
            messagebox.showerror("Error","ALL FIELDS ARE REQUIRED!!!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(self.var_floor.get(),self.var_room_no.get(),self.var_room_type.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room added succeccfully!!!",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from details")
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

        self.var_floor.set(row[0]),
        self.var_room_no.set(row[1]),
        self.var_room_type.set(row[2])

    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter floor number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
            my_cursor = conn.cursor()
            my_cursor.execute("update details set FLOOR=%s,ROOM_TYPE=%s where ROOM_NO=%s",(self.var_floor.get(),self.var_room_type.get(),self.var_room_no.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","NEW Room details has been updated sucessfully",parent=self.root)

    def dat_Delete(self):
        dat_Delete = messagebox.askyesno("Hotel Management System,","Do you want to remove this room detail",parent=self.root)
        if dat_Delete>0:
            conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
            my_cursor = conn.cursor()
            query = "delete from details where ROOM_NO=%s"
            value = (self.var_room_no.get(),)
            my_cursor.execute(query,value)
        else:
            if not dat_Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_floor.set(""),
        self.var_room_no.set(""),
        self.var_room_type.set("")





if __name__ == "__main__":
    root=Tk()
    Obj=Detailsroom(root)
    root.mainloop()