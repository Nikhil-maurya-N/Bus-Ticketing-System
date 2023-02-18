# Python program to create
# a pdf file


from fpdf import FPDF
import webbrowser
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password="nikhil",)
pointer=mydb.cursor()

pointer.execute("use passenger_details")
query="Select * from nikhil330343108922"
pointer.execute(query)
balance=pointer.fetchall()
# balance=balance
hle=balance

name=pointer.column_names
# print(name)
# balance=list(name)+list(balance)
# balance=tuple(balance)
# print(balance)
# save FPDF() class into a
# variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

space=[20,25,25,20,40,10]
pdf.set_font("Arial",style='b',size=10)
row=" "
for k,i in enumerate(name):
    row+="{:<{}}".format(str(i).capitalize(),space[k])
# print(row)
pdf.cell(187, 10, txt =row,
            ln = 1, align = 'C')
# # set style and size of font
# # that you want in the pdf

# create a cell
pdf.set_font("Arial", size = 10)
for i,num in enumerate(hle):
    row=""
    for k,j in enumerate(num):
        row+="{:<{}}".format(str(j),space[k])
        
    pdf.cell(180, 10, txt =row,
            ln = i+2, align = 'C')

# add another cell
# pdf.cell(200, 10, txt = "A Computer Science portal for geeks.      hlooo",
# 		ln = 2, align = 'C')

# save the pdf with name .pdf
# pdf.
pdf.output("GFG.pdf")
webbrowser.open_new_tab("GFG.pdf")
