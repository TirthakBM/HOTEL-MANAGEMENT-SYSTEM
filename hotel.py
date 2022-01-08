from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from customer import Cust_Win, Cust_Win
from room import Roombooking
from details import Detailsroom
from info import Info_details

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1600x700+0+0")

        ################## First image ##############
        img1 = Image.open("hotel1.jpg")
        img1 = img1.resize((1600,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg = Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1600,height=140)


        ################## Logo ######################
        img2 = Image.open("logohotel.png")
        img2 = img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)


        ################ Title ##################
        lbl_title = Label(self.root,text="Hotel Management System",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1600,height=65)

        ################ MAIN FRAME ###############
        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=205,width=1600,height=620)

        ############### LABEL ################
        lbl_menu = Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230) 

        ############### BUTTON FRAME #############
        btn_frame = Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=40,width=229,height=190)

        cust_btn = Button(btn_frame,text="CUSTOMER",command=self.Cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0)

        room_btn = Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0)
        
        details_btn = Button(btn_frame,text="DETAILS",command=self.Details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0)

        reports_btn = Button(btn_frame,text="INFO",command=self.INFO_DETAIL,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        reports_btn.grid(row=3,column=0) 

        logout_btn = Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0) 

        
        ################ RIGHT SIDE IMAGE #####################
        img3 = Image.open("slide3.jpg")
        img3 = img3.resize((1370,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1370,height=541)

        ################ DOWN IMAGES ####################
        img4 = Image.open("food.jpeg")
        img4 = img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=220,width=228,height=150)

        img5 = Image.open("inside.jpg")
        img5 = img5.resize((230,190),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=350,width=228,height=190)



    def Cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def Details_room(self):
        self.new_window = Toplevel(self.root)
        self.app=Detailsroom(self.new_window)

    def logout(self):
        self.root.destroy()

    def INFO_DETAIL(self):
        self.new_window = Toplevel(self.root)
        self.app=Info_details(self.new_window)




        

if __name__ == "__main__":
    root = Tk()
    Obj = HotelManagementSystem(root)
    root.mainloop()