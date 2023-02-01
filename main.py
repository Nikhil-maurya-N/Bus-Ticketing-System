import cv2
import qrcode
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk
import mysql.connector


class problem:

    def __init__(self):

        self.root = Tk()
        self.root.title("Bus Ticketing system By Nikhil Maurya")
        self.root.geometry("1366x768")

        img = Image.open("4.jpg")
        bg = ImageTk.PhotoImage(img)

        # Show image using label
        label1 = Label(self.root, image=bg,)
        label1.place(x=0, y=0)

    # menus
        mainmenu = Menu(self.root)
        mainmenu.add_command(label="New Passenger...", font=("BOLD", 15), command=self.New_passenger)
        mainmenu.add_command(label="Recharge", font=("BOLD", 15), command=self.Recharge)
        mainmenu.add_command(label="About", font=("BOLD", 15), command=self.About)
        mainmenu.add_command(label="Contact Us", font=("BOLD", 15), command=self.Contact)
        mainmenu.add_command(label="De-Activation", font=("BOLD", 15), command=None)
        mainmenu.add_command(label="Exit", font=("BOLD", 15), command=self.Exit)
        self.root.config(menu=mainmenu)


        # Button for entry and exit
        Entry_Button = Button(text="Scan For Entry", font=(
            "brandon Grotesque", 20), command=self.entry_bus)
        Entry_Button.place(x=300, y=200)

        Exit_Button = Button(text="Scan For Exit", font=(
            "brandon Grotesque", 20), command=self.exit_bus)
        Exit_Button.place(x=800, y=200)


        self.root.mainloop()
       

# functions
    def Register(self):
        self.user_qrcode = qrcode.make(
            str(self.var5.get())+"@"+str(self.var1.get()))
        self.user_qrcode.save(str(self.var1.get())+"qrcode.png")
        msg = tmsg.showinfo(
            "Image Creation", f"{self.var1.get()}, you Have succesfull registered to E- Bus Here is your scanner ")
        img2 = Image. open(str(self.var1.get())+"qrcode.png")
        img2. show()
        self.submitTODB()


    def submitTODB(self):
        print("Hello1")
        mydb=mysql.connector.connect(host='localhost',user='root',password='nikhil',database='passenger_details')
        pointer=mydb.cursor()
        # print(QueryID)
        print("Hello2")
        gender=str()
        if self.var2.get()==1:
            gender="male"
        elif self.var2.get()==1:
            gender="fmale"
        else:
            gender="Not to specify"
        sql="insert into personal (name, Gender, Mobile_no, Email, Addhar, passward ) values('{}','{}','{}','{}','{}','{}')".format(self.var1.get(),self.var2.get(),self.var3.get(),self.var4.get(),self.var5.get(),self.var6.get())
        pointer.execute(sql)
        mydb.commit()
        # query="create table '{}'"
        # D=pointer.fetchone()
        print("hello3")


    def New_passenger(self):

        self.var1=StringVar()
        self.var2=StringVar()
        self.var3=StringVar()
        self.var4=StringVar()
        self.var5=StringVar()
        self.var6=StringVar()


        self.f1 = Frame(self.root, height=600, width=580, relief=FLAT, border=5)
        self.f1.place(x=400, y=50)

        img1 = Image.open("1.jpg")
        bg1 = ImageTk.PhotoImage(img1)

        # Show image using label
        label1 = Label(self.f1, image=bg1)
        label1.image = bg1
        label1.place(x=0, y=0)

        l1 = Label(self.f1, text="New Passenger Registration",
                font=("Lato", 25), bg=None)
        l1.place(x=80, y=20)

        cross = Button(self.f1, text="X", command=self.f1.destroy)
        cross.place(x=550, y=1)

        l2 = Label(self.f1, text="Name", font=("Lato", 15), bg="light gray")
        l2.place(x=110, y=120)
        E2 = Entry(self.f1, textvariable=self.var1, font=("Lato", 15))
        E2.place(x=220, y=120)

        l3 = Label(self.f1, text="Gender", font=("Lato", 15), bg="light gray")
        l3.place(x=110, y=180)
        E3 = Radiobutton(self.f1, text="Male", value=0, variable=self.var2, bg="lightGray")
        E3.place(x=220, y=180)
        E3 = Radiobutton(self.f1, text="female", value=1, variable=self.var2, bg="lightGray")
        E3.place(x=280, y=180)
        E3 = Radiobutton(self.f1, text="Not to Specify", value=2,
                        variable=self.var2, bg="lightGray")
        E3.place(x=350, y=180)

        l4 = Label(self.f1, text="Mobile NO.", font=("Lato", 15), bg="light gray")
        l4.place(x=110, y=240)
        E4 = Entry(self.f1, textvariable=self.var3, font=("Lato", 15))
        E4.place(x=220, y=240)

        l5 = Label(self.f1, text="EMAIL", font=("Lato", 15), bg="light gray")
        l5.place(x=110, y=300)
        E5 = Entry(self.f1, textvariable=self.var4, font=("Lato", 15))
        E5.place(x=220, y=300)

        l6 = Label(self.f1, text="ADDHAR", font=("Lato", 15), bg="light gray")
        l6.place(x=110, y=360)
        E6 = Entry(self.f1, textvariable=self.var5, font=("Lato", 15))
        E6.place(x=220, y=360)

        l6 = Label(self.f1, text="Passward", font=("Lato", 15), bg="light gray")
        l6.place(x=110, y=420)
        E6 = Entry(self.f1, textvariable=self.var6, font=("Lato", 15))
        E6.place(x=220, y=420)

        b1 = Button(self.f1, text="Register", font=("Leto", 15), command=self.Register)
        b1.place(x=260, y=480)


    def About():
        msg = tmsg.showinfo("About", ''' This is an prototype for solving an real tym problem as discussed in Project portfolio that is we are going to sort problem of E-bus ticketing as we are in hurry so we had overcome the problem of paper ticketing we issue an QR code in whhich the  details of pasenger are encoded and entire process of ticketing done within few seconds ''')


    def Contact():
        msg = tmsg.Bshowinfo("Contact Details", '''Contact us at : \n

        Gmail : nikhil020105@gmail.com
        github : https://github.com/Nikhil-maurya-N
        Linkedin : https://www.linkedin.com/in/nikhil-maurya-13535320b
        Instagram : https://instagram.com/a_n_on_y_m_o_us_?igshid=YmMyMTA2M2Y=
        ''')


    def login(self):
        # pass

        self.var7 = StringVar()
        self.var8 = StringVar()

        self.f2 = Frame(self.root, bg="light gray", height=400,
                width=380, relief=GROOVE, border=10)
        self.f2.place(x=400, y=50)

        l_1 = Label(self.f2, text="Passenger Recharge Interface ",
                    font=("Lato", 17), bg="light gray")
        l_1.place(x=30, y=30)

        l_2 = Label(self.f2, text="Addhar No", font=("Lato", 13), bg="light gray")
        l_2.place(x=50, y=100)
        E_2 = Entry(self.f2, textvariable=self.var7, font=("Lato", 13))
        E_2.place(x=140, y=100)

        l_3 = Label(self.f2, text="Passward", font=("Lato", 13), bg="light gray")
        l_3.place(x=50, y=150)
        E_4 = Entry(self.f2, textvariable=self.var8, font=("Lato", 13,))
        E_4.place(x=140, y=150)

        # l_4 = Label(self.f2, text="hidenberg", font=("Lato", 13), bg="light gray")
        # l_4.place(x=50, y=200)
        # E_5 = Entry(self.f2, textvariable=self.var1, font=("Lato", 13,))
        # E_5.place(x=140, y=200)

        c1 = Checkbutton(self.f2, text="Ha Hm insaan h", bg="light gray")
        c1.place(x=120, y=250)

        b2 = Button(self.f2, text="Log in", font=("Leto", 13), command=self.check_validity)
        b2.place(x=170, y=300)
        self.flag=True
        return self.flag

    def check_validity(self):
        pass

    def Recharge(self):
        if self.login():
            pass
        else:
            msg = tmsg.showerror(
                "Login error", "Invalid credentials!\nPlz try again with valid username and password")


    def entry_bus(self):
        cap = cv2.VideoCapture(0)
        # initialize the cv2 QRCode detector
        detector = cv2.QRCodeDetector()
        while True:
            _, img = cap.read()
            # detect and decode
            data, bbox, _ = detector.detectAndDecode(img)
            # check if there is a QRCode in the image
            if data:
                a = data
                break
            # display the result
            cv2.imshow("QRCODEscanner", img)
            if cv2.waitKey(1) == ord("q"):
                break

        # b=webbrowser.open(str(a))
        self.savedata(data)
        cap.release()
        cv2.destroyAllWindows()


    def exit_bus(self):
        cap = cv2.VideoCapture(0)
        # initialize the cv2 QRCode detector
        detector = cv2.QRCodeDetector()
        while True:
            _, img = cap.read()
            # detect and decode
            data, bbox, _ = detector.detectAndDecode(img)
            # check if there is a QRCode in the image
            if data:
                a = data
                break
            # display the result
            cv2.imshow("QRCODEscanner", img)
            if cv2.waitKey(1) == ord("q"):
                break

        # b=webbrowser.open(str(a))
        self.calculate(data)
        cap.release()
        cv2.destroyAllWindows()


    def savedata(self):
        pass


    def calculate(self):
        pass


    def Exit():
        exit()

mainwindow= problem()
    
