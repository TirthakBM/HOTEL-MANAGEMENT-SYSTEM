from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagementSystem


def main():
    root=Tk()
    app=Login_window(root)
    root.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1600x700+0+0")

        self.bg=ImageTk.PhotoImage(file="login_background.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root,bg="black")
        frame.place(x=500,y=150,width=340,height=450)

        img1=Image.open("login_icon.ico")
        img1=img1.resize((90,90),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=630,y=170,width=90,height=90)

        get_start=Label(frame,text="GET STARTED",font=("arial",14,"bold"),fg="white",bg="black")
        get_start.place(x=108,y=120)

        ###### LABEL #########
        username_lbl=Label(frame,text="USERNAME :",font=("arial",11,"bold"),fg="white",bg="black")
        username_lbl.place(x=40,y=155)

        self.txtuser=ttk.Entry(frame,font=("arial",11,"bold"))
        self.txtuser.place(x=40,y=190,width=210)

        password_lbl=Label(frame,text="PASSWORD :",font=("arial",11,"bold"),fg="white",bg="black")
        password_lbl.place(x=40,y=235)

        self.txtpass=ttk.Entry(frame,font=("arial",11,"bold"),show = "*")
        self.txtpass.place(x=40,y=270,width=210)

        ########## ICON IMAGES ###############
        img2=Image.open("login_icon.ico")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=510,y=306,width=25,height=25)

        img3=Image.open("password_icon.ico")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=510,y=386,width=25,height=25)

        login_btn=Button(frame,text="LOGIN",command=self.login,font=("arial",11,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue",activeforeground="white",activebackground="blue")
        login_btn.place(x=110,y=320,width=120,height=35)

        register_btn=Button(frame,text="REGISTER",command=self.register_window,font=("arial",11,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        register_btn.place(x=2,y=370,width=120,height=20)

        forgot_password_btn=Button(frame,text="FORGOT PASSWORD",command=self.forgot_password_window,font=("arial",11,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgot_password_btn.place(x=20,y=415,width=160,height=20)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("ERROR","ALL FIELD REQUIRED!!")
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="root":
            messagebox.showinfo("WELCOME","WELCOME USER")
        else:
            conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(self.txtuser.get(),self.txtpass.get()))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("ERROR","INVALID USERNAME AND PASSWORD!!!")
            else:
                open_main=messagebox.askyesno("ADMIN","ACCESS GRANTED , READY TO START THE DAY?")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    
    ################## RESET PASSWORD ################
    def reset_password_data(self):
        if self.combo_security_q.get()=="SELECT":
            messagebox.showerror("ERROR","SELECT THE SECURITY QUESTION!!",parent=self.root2)
        elif self.txt_security_a.get()=="":
            messagebox.showerror("ERROR","PLAESE ENTER THE ANSWER!!",parent=self.root2)
        elif self.txt_new_password.get()=="":
            messagebox.showerror("ERROR","PLEASE ENTER THE PASSWORD!!",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and security_q=%s and security_a=%s")
            value=(self.txtuser.get(),self.combo_security_q.get(),self.txt_security_a.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("ERROR","PLEASE ENTER THE CORRECT ANSWER",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("INFO","YOUR PASSWORD HAS BEEN RESET, PLAESE LOGIN NEW PASSWORD",parent=self.root2)
                self.root2.destroy()

    ############## FORGOT PASSWORD ############
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("ERROR","PLEASE ENDER THE EMAIL ADDRESS TO RESET PASSWORD!!")
        else:
            conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("ERROR","PLEASE ENTER VALID USERNAME")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("FORGOT PASSWORD")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="FORGOT PASSWORD",font=("arial",12,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_q=Label(self.root2,text="SELECT SECURITY QUESTION:",font=("arial",15,"bold"),bg="white",fg="black")
                security_q.place(x=30,y=80)

                self.combo_security_q=ttk.Combobox(self.root2,font=("arial",15,"bold"),state="readonly")
                self.combo_security_q["values"]=("SELECT","YOUR BIRTH PLACE","YOUR CLG NAME","YOUR PET NAME")
                self.combo_security_q.place(x=50,y=110,width=250)
                self.combo_security_q.current(0)

                security_a=Label(self.root2,text="SECURITY ANSWER",font=("arial",15,"bold"),bg="white",fg="black")
                security_a.place(x=50,y=150)

                self.txt_security_a = ttk.Entry(self.root2,font=("arial",15,"bold"))
                self.txt_security_a.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="NEW PASSWORD",font=("arial",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_new_password = ttk.Entry(self.root2,font=("arial",15,"bold"),show = "*")
                self.txt_new_password.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="RESET",command=self.reset_password_data,font=("arial",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)





class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("REGISTER")
        self.root.geometry("1600x700+0+0")

        ############ VARIABLES ###############
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_q=StringVar()
        self.var_security_a=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        ###### BG IMAGE ##########
        self.bg=ImageTk.PhotoImage(file="register_background.jpg")

        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relheight=1,relwidth=1)

        ########## LEFT IMAGE #############
        self.bg1=ImageTk.PhotoImage(file="register_left_background.jpg")

        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,height=550,width=470)

        ####### MAIN FRAME ##########
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl =Label(frame,text="REGISTER HERE",font=("arial",15,"bold"),fg="green",bg="white")
        register_lbl.place(x=20,y=20)

        ########## LABELS AND ENTRIES ############

        ##### ROW 1 #############
        fname=Label(frame,text="FIRST NAME :",font=("arial",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("arial",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        fname=Label(frame,text="LAST NAME :",font=("arial",15,"bold"),bg="white")
        fname.place(x=370,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("arial",15,"bold"))
        fname_entry.place(x=370,y=130,width=250)

        ##### ROW 2 ###############

        contact = Label(frame,text="CONTACT NO.:",font=("arial",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact,font=("arial",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email = Label(frame,text="EMAIL:",font=("arial",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email,font=("arial",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        ########### ROW 3 #################

        security_q=Label(frame,text="SELECT SECURITY QUESTION:",font=("arial",15,"bold"),bg="white",fg="black")
        security_q.place(x=50,y=240)

        self.combo_security_q=ttk.Combobox(frame,textvariable=self.var_security_q,font=("arial",15,"bold"),state="readonly")
        self.combo_security_q["values"]=("SELECT","YOUR BIRTH PLACE","YOUR CLG NAME","YOUR PET NAME")
        self.combo_security_q.place(x=50,y=270,width=250)
        self.combo_security_q.current(0)

        security_a=Label(frame,text="SECURITY ANSWER",font=("arial",15,"bold"),bg="white",fg="black")
        security_a.place(x=370,y=240)

        self.txt_security_a = ttk.Entry(frame,textvariable=self.var_security_a,font=("arial",15,"bold"))
        self.txt_security_a.place(x=370,y=270,width=250)

        ########### ROW 4 ################
        pswd=Label(frame,text="PASSWORD",font=("arial",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass,font=("arial",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="CONFIRM PASSWORD",font=("arial",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass,font=("arial",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        ############ CHECK BUTTON ############

        self.var_check_btn=IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check_btn,text="I AGREE THE TEARMS AND CONDITIONS.",font=("arial",11,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=400)

        ########### BUTTON #############
        img = Image.open("register_button.png")
        img = img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1 = Button(frame,image=self.photoimage,command=self.rgister_data,borderwidth=0,cursor="hand2",fg="white",activeforeground="white",activebackground="white",bg="white",font=("arial",15,"bold"))
        b1.place(x=30,y=460)

        img1 = Image.open("login_button.png")
        img1 = img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2 = Button(frame,command=self.return_login,image=self.photoimage1,borderwidth=0,cursor="hand2",fg="white",activeforeground="white",activebackground="white",bg="white",font=("arial",15,"bold"))
        b2.place(x=330,y=460)


    ############# FUNCTION ####################

    def rgister_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_q.get()=="SELECT":
            messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("ERROR","PASSWORD AND CONFIRM PASSWORD MUST BE SAME!!!")
        elif self.var_check_btn.get()==0:
            messagebox.showerror("ERROR","PLEASE AGREE THE TERMS AND CONDITION!!!")
        else:
            conn = mysql.connector.connect(host="Localhost",username="root",password="root",database="hotel_management")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("ERROR","USER ALREADY EXIST, PLEASE TRY ANOTHERS EMAIL!!!")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(self.var_fname.get(),self.var_lname.get(),self.var_contact.get(),self.var_email.get(),self.var_security_q.get(),self.var_security_a.get(),self.var_pass.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("SUCCESS","REGISER SUCCESSFULLY!!!")

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()
