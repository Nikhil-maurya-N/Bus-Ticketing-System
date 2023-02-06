import cv2
import qrcode
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk
import mysql.connector
import datetime


class problem:

    def __init__(self):
        self.flag=None
        
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
        mainmenu.add_command(label="Recharge", font=("BOLD", 15), command=self.login)
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


        self.getPassward("nikhil")
        
        
        self.root.mainloop()

       
    def getPassward(self,passk):
        try:
            self.mydb=mysql.connector.connect(host='localhost',user='root',password=passk)
            tmsg.showinfo("Logged In","Successfully logged in to your sql")

            self.pointer=self.mydb.cursor()
            self.pointer.execute("use passenger_details")
            # print("yes")
            # self.pointer.execute("show databases")
            # s=('passenger_details',)
            # if s not in self.pointer:
            #     self.pointer.execute("create database passenger_details")
            #     queryTocreateBaseTable='''create table personal(
            #                             name varchar(20),
            #                             Gender varchar(20),
            #                             Mobile_no varchar(10),
            #                             Email varchar(50),
            #                             Addhar varchar(15)not null,
            #                             passward varchar(15),
            #                             state boolean,
            #                             total_balance float,
            #                             primary key(addhar)
            #                             )'''
            #     self.pointer.execute(queryTocreateBaseTable)
            #     self.mydb.commit()
            #     tmsg.showinfo("database created","Successfull created 'personal' table in 'passenger_details'")
            # self.pointer.execute("use passenger_details")
        except mysql.connector.errors.ProgrammingError:
            # print("yes")
            tmsg.showerror("Unable to connect database","It seems like the passward : '{}' is not right to login to your database!".format(passk))
            self.passward=StringVar()

            self.frame = Frame(self.root, bg="light gray", height=200,
                    width=380, relief=GROOVE, border=10)
            self.frame.place(x=400, y=50)

            l_1 = Label(self.frame, text="Enter Your root passward",
                        font=("Lato", 17), bg="light gray")
            l_1.place(x=30, y=30)

            E_2 = Entry(self.frame, textvariable=self.passward, font=("Lato", 13))
            E_2.place(x=100, y=80)

            # cross=Button(self.frame,text="X",font=("Leto", 13), command=self.frame.destroy)
            # cross.place(x=335,y=1)

            b2 = Button(self.frame, text="Log in", font=("Leto", 13), command=self.passward_sender)
            b2.place(x=170, y=130)

    def passward_sender(self):
        self.frame.destroy()
        self.getPassward(self.passward.get())
        


# functions
    def Register(self):
        string=str(self.var1.get()+self.var5.get())
        string=string.replace(" ","")
        self.user_qrcode = qrcode.make(string)
        self.user_qrcode.save(string+"qrcode.png")
        msg = tmsg.showinfo(
            "Image Creation", f"{self.var1.get()}, you Have succesfull registered to E- Bus Here is your scanner ")
        img2 = Image. open(string+"qrcode.png")
        img2. show()
        self.submitTODB(string)
        self.f1.destroy()


    def submitTODB(self,string):
        # print("Hello1")
        
        # print(QueryID)
        # print("Hello2")
        gender=str()
        # print(type(self.var2.get()))
        variable=int(self.var2.get())
        if variable==1:
            gender="male"
        elif variable==2:
            gender="female"
        else:
            gender="Not to specify"
        sql="insert into personal (name, Gender, Mobile_no, Email, Addhar, passward ) values('{}','{}','{}','{}','{}','{}')".format(self.var1.get(),gender,self.var3.get(),self.var4.get(),self.var5.get(),self.var6.get())
        self.pointer.execute(sql)
        # mydb.commit()
        query="create table {}(TransitionId int not null auto_increment,board_time datetime, departure_time datetime ,amount_difference float,statement text(100),total_balance float,primary key (TransitionId))".format(string)
        # print(query)
        self.pointer.execute(query)
        self.mydb.commit()
        # D=pointer.fetchone()

        # print("hello3")


    def New_passenger(self):

        self.var1=StringVar()
        self.var2=IntVar()
        self.var3=StringVar()
        self.var4=StringVar()
        self.var5=StringVar()
        self.var6=StringVar()


        self.f1 = Frame(self.root, height=600, width=580, relief=FLAT, border=5)
        self.f1.place(x=400, y=50)
        vcmd=(self.f1.register(self.callback))
        vcmd1=(self.f1.register(self.callback1))

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

        E3 = Radiobutton(self.f1, text="Male", value=1, variable=self.var2, bg="lightGray")
        E3.place(x=220, y=180)
        E3 = Radiobutton(self.f1, text="female", value=2, variable=self.var2, bg="lightGray")
        E3.place(x=280, y=180)
        E3 = Radiobutton(self.f1, text="Not to Specify", value=3, variable=self.var2, bg="lightGray")
        E3.place(x=350, y=180)

        l4 = Label(self.f1, text="Mobile NO.", font=("Lato", 15), bg="light gray")
        l4.place(x=110, y=240)
        E4 = Entry(self.f1, textvariable=self.var3, validate="key",validatecommand=(vcmd,"%P"),font=("Lato", 15))
        E4.place(x=220, y=240)

        l5 = Label(self.f1, text="EMAIL", font=("Lato", 15),bg="light gray")
        l5.place(x=110, y=300)
        E5 = Entry(self.f1, textvariable=self.var4 , validate ="focusout", validatecommand =(vcmd1, '%P'),font=("Lato", 15))
        E5.place(x=220, y=300)

        l6 = Label(self.f1, text="ADDHAR", font=("Lato", 15), bg="light gray")
        l6.place(x=110, y=360)
        E6 = Entry(self.f1,validate="key",validatecommand=(vcmd,"%P"), textvariable=self.var5, font=("Lato", 15))
        E6.place(x=220, y=360)

        l6 = Label(self.f1, text="Passward", font=("Lato", 15), bg="light gray")
        l6.place(x=110, y=420)
        E6 = Entry(self.f1, textvariable=self.var6, font=("Lato", 15))
        E6.place(x=220, y=420)

        b1 = Button(self.f1, text="Register", font=("Leto", 15), command=self.Register)
        b1.place(x=260, y=480)


    def About(self):
        msg = tmsg.showinfo("About", ''' This is an prototype for solving an real tym problem as discussed in Project portfolio that is we are going to sort problem of E-bus ticketing as we are in hurry so we had overcome the problem of paper ticketing we issue an QR code in whhich the  details of pasenger are encoded and entire process of ticketing done within few seconds ''')


    def Contact(self):
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
        self.checkvar=IntVar()

        self.f2 = Frame(self.root, bg="light gray", height=400,
                width=380, relief=GROOVE, border=10)
        self.f2.place(x=400, y=50)
        vcmd=(self.f2.register(self.callback))

        l_1 = Label(self.f2, text="Passenger Recharge Interface ",
                    font=("Lato", 17), bg="light gray")
        l_1.place(x=30, y=30)

        l_2 = Label(self.f2, text="Addhar No", font=("Lato", 13), bg="light gray")
        l_2.place(x=50, y=100)

        E_2 = Entry(self.f2, textvariable=self.var7, validate ='key' ,validatecommand=(vcmd,'%P'), font=("Lato", 13))
        E_2.place(x=140, y=100)

        l_3 = Label(self.f2, text="Passward", font=("Lato", 13), bg="light gray")
        l_3.place(x=50, y=150)
        E_4 = Entry(self.f2, textvariable=self.var8, font=("Lato", 13,))
        E_4.place(x=140, y=150)

        

        c1 = Checkbutton(self.f2, text="Ha Hm insaan h", bg="light gray")
        c1.place(x=120, y=250)

        b2 = Button(self.f2, text="Log in", font=("Leto", 13), command=self.check_validity)
        b2.place(x=170, y=300)
        cross=Button(self.f2,text="X",font=("Leto", 13), command=self.f2.destroy)
        cross.place(x=335,y=1)
        # print("hello1")
        # print(self.flag)
        # return self.flag
        # self.f2.destroy()
        # return self.flag
    
    def callback1(self,input): 
        if ('@'in input and '.com'in input) or input=="": 
            return True
        else: 
            tmsg.showerror("INvalid input","Must have an '@' and  '.com' present in a valid email")
            return False
        
    def callback(self,P):
        # print("yes")
        if P.isdigit() or P=="":
            return True
        else:
            tmsg.showerror("Invalid input!","Please Enter only numeric values \ni.e.(0-9)")
            return False
        
    def callback2(self,P):
        # print("yes")
        if self.validatefloat(P) or P=="":
            return True
        else:
            tmsg.showerror("Invalid input!","Please Enter only numeric values  and single '.'\ni.e.(0-9)")
            return False
    def validatefloat(self,P):
        X=P
        i=X.find('.')
        X=X[:i]+X[i+1:]
        if X.isdigit():
            return True
        else:
            return False

    def check_validity(self):
        # print(self.c1.state())
        if self.checkvar==1:
            tmsg.showwarning("Humanity check ","Are Are! Insaan ni ho ka be tick kro :)")
            return
        sqlQuery="select passward from personal where Addhar='{}'".format(self.var7.get())
        self.pointer.execute(sqlQuery)
        LoginCredential=self.pointer.fetchone()



        # print(LoginCredential[0])
        try:
            if self.var8.get()==str(LoginCredential[0]):
                # print("Yes")
                self.f2.destroy()
                # pass
                # print("logged in")
                msg = tmsg.showinfo(
                    "logged In", "Successfully Logged In")
                self.Recharge()
            else:
                msg = tmsg.showerror(
                    "Login error", "Invalid credentials!\nPlz try again  password")

                # return self.flag
        except :
            msg = tmsg.showerror(
                "Login error", "Invalid credentials!\nPlz try again  with valid Addhar!")
            # return self.flag
        # return
        # pass

    def Recharge(self):
        query="Select total_balance from personal where Addhar={}".format(self.var7.get())
        self.pointer.execute(query)
        balance=self.pointer.fetchone()
        balance=str(balance[0])
        # print(balance)

        self.var9=StringVar()

        self.f3 = Frame(self.root, height=400,bg="light gray" ,width=580, relief=GROOVE, border=5)
        self.f3.place(x=400, y=50)


        cross = Button(self.f3, text="X", command=self.f3.destroy)
        cross.place(x=550, y=1)

        l1 = Label(self.f3, text="Recharge pannel",bg="light gray",
                font=("Lato", 25))
        l1.place(x=90, y=20)
        # var9=
        l2 = Label(self.f3, text=f"You have current balance in your account: {balance}", font=("Lato", 15), bg="light gray")
        l2.place(x=120, y=120)
        
        
        l3 = Label(self.f3, text="Enter Amount To add :", font=("Lato", 15), bg="light gray")
        l3.place(x=120, y=170)
        E3 = Entry(self.f3, textvariable=self.var9, font=("Lato", 15))
        E3.place(x=120, y=220)
        
        b2 = Button(self.f3, text="deposit", font=("Leto", 13),relief=RIDGE, command=lambda  : self.increase_money(balance))
        b2.place(x=220, y=320)

    def increase_money(self,balance):
        balance=float(balance)
        # print(balance)
        if  not self.callback2(self.var9.get()):
            return
        total=float(self.var9.get())+balance
        # print(total)
        query="update personal set total_balance ='{}' where Addhar={}".format(total,self.var7.get())
        # print(query)
        self.pointer.execute(query)
        self.mydb.commit()        
        query="select name from personal where Addhar={}".format(self.var7.get())
        # print(query)
        self.pointer.execute(query)
        name=self.pointer.fetchone()
        name=name[0]
        name=name.replace(" ","")
        tableName=name+self.var7.get()
        query="insert into {}(board_time,amount_difference,statement,total_balance) values( '{}','{}','{}','{}') ".format(tableName,datetime.datetime.now(),self.var9.get(),"Recharged via client portal",total)
        # print(query)
        self.pointer.execute(query)
        self.mydb.commit()
        self.f3.destroy()
        tmsg.showinfo("Transaction successfull","You have successfully recharged with the amount : "+str(self.var9.get()))
        # print(self.var9.get())
        # pass    

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
        cap.release()
        cv2.destroyAllWindows()
        self.savedata(data)


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
        cap.release()
        cv2.destroyAllWindows()
        self.calculate(data)


    def savedata(self,data):
        # data="Nikhil kjas 303343108922"
        temp=str()
        for i in data:
            if i.isalpha() or i==" ":
                temp+=i
        addhar=data.replace(temp,"")
        query="select state from personal where Addhar={}".format(addhar)
        self.pointer.execute(query)
        state=self.pointer.fetchone()[0]
        # print(query)
        # print(state)
        if state==1:
            tmsg.showwarning("invalid entry","It seems like you have already have an departure pending please firstly depart from bus")
            return
        query="insert into {}(board_time) value('{}')".format(data,datetime.datetime.now())
        self.pointer.execute(query)
        
        query="update personal set state=1 where Addhar={}".format(addhar)
        self.pointer.execute(query)
        self.mydb.commit()
        # print("Yes")
        # pass


    def calculate(self,data):
        temp=str()
        for i in data:
            if i.isalpha() or i==" ":
                temp+=i
        addhar=data.replace(temp,"")
        query="select state from personal where Addhar={}".format(addhar)
        self.pointer.execute(query)
        state=self.pointer.fetchone()[0]
        if state==0:
            tmsg.showerror("Invalid departure ","It seems like you did not boarded before please board first then do departure!")
            return
        query="select max(transitionID) from {}".format(data)
        self.pointer.execute(query)
        transId=self.pointer.fetchone()[0]
        depTime=datetime.datetime.now()
        query="select board_time from {} where TransitionId={}".format(data,transId)
        # print(query)
        self.pointer.execute(query)

        boardTime=self.pointer.fetchone()[0]

        timeINMin,moneydifference=self.moneyCal(boardTime,depTime)
        tmsg.showinfo("Departured successfull","Dear custumer you traveled {} which costs you : {}".format(timeINMin,moneydifference))
        
        query="select total_balance from personal where Addhar={}".format(addhar)
        self.pointer.execute(query)
        totalBalance=self.pointer.fetchone()[0]
        totalBalance-=moneydifference
        # print(totalBalance)
        query="update {} set departure_time='{}', amount_difference={}, statement='{}',total_balance={} where TransitionId={}".format(data,depTime,moneydifference,"money deduced for Travel cost",totalBalance,transId)
        # print(query)
        self.pointer.execute(query)
        query="update personal set total_balance ={}, state=0 where Addhar={}".format(totalBalance,addhar)
        # print(query)
        self.pointer.execute(query)

        self.mydb.commit()
        # self.mydb.commit()
        # pass

    def moneyCal(self,boardTime,depTime):
        boardTime=int(round(boardTime.timestamp()))
        depTime=int(round(depTime.timestamp()))
        totalTime=depTime-boardTime
        timeINMin= str(datetime.timedelta(seconds=totalTime))
        return timeINMin,totalTime* 1.0/60.0
    def Exit():
        exit()

mainwindow= problem()