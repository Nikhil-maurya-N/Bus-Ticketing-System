# # import tkinter 

# # from tkinter import *

  

  

# # def callback(input): 

      

# #     if input.isdigit() or input=="": 

# #         print(input) 

# #         return True
# #     else: 

# #         print(input) 

# #         return False

                          

# # root = Tk() 

  

# # e = Entry(root) 

# # e.place(x = 50, y = 50) 
# # e = Entry(root) 

# # e.place(x = 50, y = 100) 

# # reg = root.register(callback) 

  

# # e.config(validate ="key",  

# #          validatecommand =(reg, '%P')) 

  
# # root.mainloop()

# import tkinter 

# from tkinter import *

  

  

# def callback1(input): 

      

#     if '@'in input and '.com'in input: 

#         # print(input) 

#         return True
#     else: 

#         print(input) 

#         return False

                          

# root = Tk() 

  

# e = Entry(root) 

# e.place(x = 50, y = 50) 
# f= Entry(root) 

# f.place(x = 50, y = 100) 

# reg = root.register(callback1) 

  

# e.config(validate ="focusout",  

#          validatecommand =(reg, '%P')) 

  
# root.mainloop()


# def validatefloat(P):
#     X=P
#     i=X.find('.')
#     X=X[:i]+X[i+1:]
#     if X.isdigit():
#         print("yes")
#     else:
#         print("NO")
              
# validatefloat('1.22')            
ba='1.22'
ba=float(ba)
print(type(ba))
print(ba)

c1 = Checkbutton(self.f2, text="Ha Hm insaan h", onvalue=1,offvalue=0,variable=self.checkvar,bg="light gray",command=self.checkboxcommand)
c1.place(x=120, y=250)

def checkboxcommand(self):
        print(self.checkvar)
        if self.checkvar==1:
            print("yes")
        else:
            print('No')