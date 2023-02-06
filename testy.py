# import tkinter

# from tkinter import *


# # # def callback(input):


# # #     if input.isdigit() or input=="":

# # #         print(input)

# # #         return True
# # #     else:

# # #         print(input)

# # #         return False


# root = Tk()


# # # e = Entry(root)

# # # e.place(x = 50, y = 50)
# # # e = Entry(root)

# # # e.place(x = 50, y = 100)

# # # reg = root.register(callback)


# # # e.config(validate ="key",

# # #          validatecommand =(reg, '%P'))


# # # root.mainloop()

# # import tkinter

# # from tkinter import *


# # def callback1(input):


# #     if '@'in input and '.com'in input:

# #         # print(input)

# #         return True
# #     else:

# #         print(input)

# #         return False


# # root = Tk()


# # e = Entry(root)

# # e.place(x = 50, y = 50)
# # f= Entry(root)

# # f.place(x = 50, y = 100)

# # reg = root.register(callback1)


# # e.config(validate ="focusout",

# #          validatecommand =(reg, '%P'))


# # def validatefloat(P):
# #     X=P
# #     i=X.find('.')
# #     X=X[:i]+X[i+1:]
# #     if X.isdigit():
# #         print("yes")
# #     else:
# #         print("NO")

# # validatefloat('1.22')
# # ba='1.22'
# # ba=float(ba)
# # print(type(ba))
# # print(ba)

# # # c1 = Checkbutton(self.f2, text="Ha Hm insaan h", onvalue=1,offvalue=0,variable=self.checkvar,bg="light gray",command=self.checkboxcommand)
# # c1.place(x=120, y=250)

# # def checkboxcommand(self):
# #         print(self.checkvar)
# #         if self.checkvar==1:
# #             print("yes")
# #         else:
# #             print('No')
# var = 5
# E3 = Radiobutton(text="Male", value=1, variable=var, bg="lightGray",)
# E3.place(x=220, y=180)
# E4 = Radiobutton(text="female", value=0,variable=var, bg="lightGray",)
# E4.place(x=280, y=180)
# E5 = Radiobutton(text="Not to Specify", value=-1,variable=var, bg="lightGray",)
# E5.place(x=350, y=180)
# E3.deselect()
# E4.deselect()
# E5.deselect()
# root.mainloop()
from tkinter import *

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="male", variable=var, value=1
                  )
R1.place(x=220, y=180)

R2 = Radiobutton(root, text="female", variable=var, value=2
                 )
R2.place(x=280, y=180)

R3 = Radiobutton(root, text="Not to specify", variable=var, value=3
                  )
R3.place(x=350, y=180)

label = Label(root)
label.place(x=10,y=150)
root.mainloop()
