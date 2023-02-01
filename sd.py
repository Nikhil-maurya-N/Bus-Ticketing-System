from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title('background image')

# image1 = PhotoImage(file='image_name.gif')
# img1=Image.open("1.jpg")
# image1=ImageTk.PhotoImage(img1)

# get the image size
# w = image1.width()
# h = image1.height()

# make the root window the size of the image
def Register():
    print(var3.get())
    l=Label(f1,text=var3.get())
    l.place(x=110,y=310)
var3=StringVar()
# root.geometry("%dx%d" % (w, h))
f1 = Frame( root, height=600, width=580, relief=FLAT, border=5)
f1.place(x=400, y=50)
l3 = Label(f1, text="Gender", font=("Lato", 15), bg="light gray")
l3.place(x=110, y=180)
E3 = Radiobutton(f1, text="Male", value=1, variable= var3, bg="lightGray")
E3.place(x=220, y=180)
E3 = Radiobutton(f1, text="female", value=2, variable= var3, bg="lightGray")
E3.place(x=280, y=180)
E3 = Radiobutton(f1, text="Not to Specify", value=3,
                variable= var3, bg="lightGray")
E3.place(x=350, y=180)

b1 = Button(f1, text="Register", font=("Leto", 15), command=Register)
b1.place(x=260, y=480)

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
root.mainloop()