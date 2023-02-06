# from tkinter import *
# from PIL import Image,ImageTk

# root = Tk()
# root.title('background image')

# image1 = PhotoImage(file='image_name.gif')
# img1=Image.open("1.jpg")
# image1=ImageTk.PhotoImage(img1)

# get the image size
# w = image1.width()
# h = image1.height()

# make the root window the size of the image
# def Register():
#     print(var3.get())
#     l=Label(f1,text=var3.get())
#     l.place(x=110,y=310)
# var3=StringVar()
# root.geometry("%dx%d" % (w, h))
# f1 = Frame( root, height=600, width=580, relief=FLAT, border=5)
# f1.place(x=400, y=50)
# l3 = Label(f1, text="Gender", font=("Lato", 15), bg="light gray")
# l3.place(x=110, y=180)
# E3 = Radiobutton(f1, text="Male", value=1, variable= var3, bg="lightGray")
# E3.place(x=220, y=180)
# E3 = Radiobutton(f1, text="fema3le", value=2, variable= var3, bg="lightGray")
# E3.place(x=280, y=180)
# E3 = Radiobutton(f1, text="Not to Specify", value=3,
#                 variable= var3, bg="lightGray")
# E3.place(x=350, y=180)

# b1 = Button(f1, text="Register", font=("Leto", 15), command=Register)
# b1.place(x=260, y=480)
# # root has no image argument, so use a label as a panel
# panel1 = Label(root, image=image1)
# panel1.pack(side='top', fill='both', expand='yes')

# # put a button/label on the image panel to test it
# label1 = Label(panel1, text='here i am')
# label1.pack(side=TOP)

# button2 = Button(panel1, text='button2')
# button2.pack(side='top')
# root.wm_attributes('-transparentcolor', root['fg'])

# start the event loop
# root.mainloop()
# import mysql.connector
# name="nikhil"

# # query="create table {}(board_time date, departure_time date,amount_difference float,total_balance float)".format(name)
# # pointer.execute(query)
# add='987567543'
# sqlQuery="select passward from personal where Addhar= '{}'".format(add)
# pointer.execute(sqlQuery)
# print(pointer.fetchone())
# # LoginCredential=self.pointer.execute(sqlQuery)

# mydb.commit()
import cv2
import qrcode
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk
import mysql.connector
import datetime

# def check_validity():
#     return 69
# root=Tk()
# b2 = Button(text="Log in", font=("Leto", 13), command=check_validity)
# b2.place(x=170, y=300)
# print(b2)
# root.mainloop()
# query="create table {}(board_time date set default getdate(), departure_time date set default getdate(),amount_difference float,statement text(100),total_balance float)".format("kddu")
# pointer.execute(query)
# query="update personal set  total_balance ='{}' where Addhar='{}'".format(23,'098765432112')
# query="update {} set departure_time={}, set amount_difference={}, set statement={},set total_balance={}".format("nikhil303343108922",datetime.datetime.now(),'78',"money deduced for Travel cost",'78')
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='ikhil')
    pointer=mydb.cursor()
except mysql.connector.errors.ProgrammingError:
    print("yes")
    
# print(query)
# u=list(pointer)
# print(u)
pointer.execute("show databases")
s=('passenger_details',)
if s in pointer:
    print("yes")
# print(type(pointer))
else:
    print("NO")
# for s in pointer:
#     print(s)
# mydb.commit()