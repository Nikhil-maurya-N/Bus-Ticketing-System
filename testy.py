import tkinter

from tkinter import *

import tkinter.messagebox as tmsg
from tkinter import messagebox



# # # # def callback(input):


# # # #     if input.isdigit() or input=="":

# # # #         print(input)

# # # #         return True
# # # #     else:

# # # #         print(input)

# # # #         return False


# # root = Tk()


# # # # e = Entry(root)

# # # # e.place(x = 50, y = 50)
# # # # e = Entry(root)

# # # # e.place(x = 50, y = 100)

# # # # reg = root.register(callback)


# # # # e.config(validate ="key",

# # # #          validatecommand =(reg, '%P'))


# # # # root.mainloop()

# # # import tkinter

# # # from tkinter import *


# # # def callback1(input):


# # #     if '@'in input and '.com'in input:

# # #         # print(input)

# # #         return True
# # #     else:

# # #         print(input)

# # #         return False


# # # root = Tk()


# # # e = Entry(root)

# # # e.place(x = 50, y = 50)
# # # f= Entry(root)

# # # f.place(x = 50, y = 100)

# # # reg = root.register(callback1)


# # # e.config(validate ="focusout",

# # #          validatecommand =(reg, '%P'))


# # # def validatefloat(P):
# # #     X=P
# # #     i=X.find('.')
# # #     X=X[:i]+X[i+1:]
# # #     if X.isdigit():
# # #         print("yes")
# # #     else:
# # #         print("NO")

# # # validatefloat('1.22')
# # # ba='1.22'
# # # ba=float(ba)
# # # print(type(ba))
# # # print(ba)

# # # # c1 = Checkbutton(f2, text="Ha Hm insaan h", onvalue=1,offvalue=0,variable=checkvar,bg="light gray",command=checkboxcommand)
# # # c1.place(x=120, y=250)

# # # def checkboxcommand(self):
# # #         print(self.checkvar)
# # #         if self.checkvar==1:
# # #             print("yes")
# # #         else:
# # #             print('No')
# # var = 5
# # E3 = Radiobutton(text="Male", value=1, variable=var, bg="lightGray",)
# # E3.place(x=220, y=180)
# # E4 = Radiobutton(text="female", value=0,variable=var, bg="lightGray",)
# # E4.place(x=280, y=180)
# # E5 = Radiobutton(text="Not to Specify", value=-1,variable=var, bg="lightGray",)
# # E5.place(x=350, y=180)
# # E3.deselect()
# # E4.deselect()
# # E5.deselect()
# # root.mainloop()
# from tkinter import *

# # def sel():
# #    selection = "You selected the option " + str(var.get())
# #    label.config(text = selection)
# def Register():
#    print(var1.get())
#    print(var2.get())
#    print(var3.get())
#    print(var4.get())
#    print(var5.get())
#    print(var6.get())
#    if var1.get()=="" or var2.get()=="" or var3.get()=="" or var4.get()=="" or var5.get()=="" or var6.get() =="":
#         print("Yes")
#    else:
#       print("no")

# root = Tk()
# var = IntVar()
# # R1 = Radiobutton(root, text="male", variable=var, value=1
# #                   )
# # R1.place(x=220, y=180)

# # R2 = Radiobutton(root, text="female", variable=var, value=2
# #                  )
# # R2.place(x=280, y=180)

# # R3 = Radiobutton(root, text="Not to specify", variable=var, value=3
# #                   )
# # R3.place(x=350, y=180)


# # label = Label(root)
# # label.place(x=10,y=150)
# # c1 = Checkbutton(text="Ha Hm insaan h", bg="light gray",variable=var)
# # c1.place(x=120, y=250)
# # b2 = Button(text="Log in", font=("Leto", 13), command=sel)
# # b2.place(x=170, y=300)
# var1=StringVar()
# var2=IntVar()
# var3=StringVar()
# var4=StringVar()
# var5=StringVar()
# var6=StringVar()


# f1 = Frame(root, height=600, width=580, relief=FLAT, border=5)
# f1.place(x=400, y=50)
# # vcmd=(f1.register(callback))
# # vcmd1=(f1.register(callback1))

# # img1 = Image.open("1.jpg")
# # bg1 = ImageTk.PhotoImage(img1)

# # Show image using label
# # label1 = Label(f1, image=bg1)
# # label1.image = bg1
# # label1.place(x=0, y=0)

# l1 = Label(f1, text="New Passenger Registration",
#          font=("Lato", 25), bg=None)
# l1.place(x=80, y=20)

# cross = Button(f1, text="X", command=f1.destroy)
# cross.place(x=550, y=1)

# l2 = Label(f1, text="Name", font=("Lato", 15), bg="light gray")
# l2.place(x=110, y=120)
# E2 = Entry(f1, textvariable=var1, font=("Lato", 15))
# E2.place(x=220, y=120)

# l3 = Label(f1, text="Gender", font=("Lato", 15), bg="light gray")
# l3.place(x=110, y=180)

# E3 = Radiobutton(f1, text="Male", value=1, variable=var2, bg="lightGray")
# E3.place(x=220, y=180)
# E3 = Radiobutton(f1, text="female", value=2, variable=var2, bg="lightGray")
# E3.place(x=280, y=180)
# E3 = Radiobutton(f1, text="Not to Specify", value=3, variable=var2, bg="lightGray")
# E3.place(x=350, y=180)

# l4 = Label(f1, text="Mobile NO.", font=("Lato", 15), bg="light gray")
# l4.place(x=110, y=240)
# E4 = Entry(f1, textvariable=var3, validate="key",font=("Lato", 15))
# E4.place(x=220, y=240)

# l5 = Label(f1, text="EMAIL", font=("Lato", 15),bg="light gray")
# l5.place(x=110, y=300)
# E5 = Entry(f1, textvariable=var4 , validate ="focusout",font=("Lato", 15))
# E5.place(x=220, y=300)

# l6 = Label(f1, text="ADDHAR", font=("Lato", 15), bg="light gray")
# l6.place(x=110, y=360)
# E6 = Entry(f1,validate="key", textvariable=var5, font=("Lato", 15))
# E6.place(x=220, y=360)

# l6 = Label(f1, text="Passward", font=("Lato", 15), bg="light gray")
# l6.place(x=110, y=420)
# E6 = Entry(f1, textvariable=var6, font=("Lato", 15))
# E6.place(x=220, y=420)

# b1 = Button(f1, text="Register", font=("Leto", 15), command=Register)
# b1.place(x=260, y=480)

# root.mainloop()
# char='s'
      
# if char in " @#$%^&*(_-+?)":
#     print("YEs")
num=0
low=0
upp=0
special=0
print(num)
for char in "self.varA.get()":
   if char.isnumeric:
         print(char)
         num=1
   if char.islower():
         # print("l")
         
         low=1
   if char.isupper():
         # print("u")
         
         upp=1
   if char in " !@#$%^&*()_-+?":
         # print("s")
         
         special=1
print(num)
print(low)
print(upp)
print(special)
if num==0 or low==0 or upp==0 or special==0:
   flag=1
   tmsg.showerror("Invalid Addhar","there should be all the characters from the character set: {0-1}, {a-z}, {A-Z} and {! @#$%^&*()_-+}")
   # return True