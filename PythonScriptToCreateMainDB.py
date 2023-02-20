import mysql.connector
# from tkinter import messagebox
# import tkinter.messagebox as tmsg
passk=input("Enter your password for database server : ")
try:
    mydb = mysql.connector.connect(
        host='localhost', user='root', password=passk)
except:
    print("wrong password")
    exit()
# tmsg.showinfo("Logged In", "Successfully logged in to your sql")
pointer=mydb.cursor()
pointer.execute("show databases")
s = ('passenger_details',)
if s not in pointer:
    pointer.execute("create database passenger_details")
    pointer.execute("use passenger_details")
    queryTocreateBaseTable = '''create table personal(
                                    name varchar(20),
                                    Gender varchar(20),
                                    Mobile_no varchar(10),
                                    Email varchar(50),
                                    Addhar varchar(15)not null,
                                    passward varchar(15),
                                    state boolean default 0,
                                    total_balance float default 0,
                                    primary key(addhar)
                                    )'''
    pointer.execute(queryTocreateBaseTable)
    mydb.commit()
    print("Database creaeted successfully")
    # tmsg.showinfo("database created",
                # "Successfull created 'personal' table in 'passenger_details'")
else:
    print("Database already exists, No need to do that")

