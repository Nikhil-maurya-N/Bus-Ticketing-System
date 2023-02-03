# import tkinter 

# from tkinter import *

  

  

# def callback(input): 

      

#     if input.isdigit() or input=="": 

#         print(input) 

#         return True
#     else: 

#         print(input) 

#         return False

                          

# root = Tk() 

  

# e = Entry(root) 

# e.place(x = 50, y = 50) 
# e = Entry(root) 

# e.place(x = 50, y = 100) 

# reg = root.register(callback) 

  

# e.config(validate ="key",  

#          validatecommand =(reg, '%P')) 

  
# root.mainloop()

import tkinter 

from tkinter import *

  

  

def callback1(input): 

      

    if '@'in input and '.com'in input: 

        # print(input) 

        return True
    else: 

        print(input) 

        return False

                          

root = Tk() 

  

e = Entry(root) 

e.place(x = 50, y = 50) 
f= Entry(root) 

f.place(x = 50, y = 100) 

reg = root.register(callback1) 

  

e.config(validate ="focusout",  

         validatecommand =(reg, '%P')) 

  
root.mainloop()