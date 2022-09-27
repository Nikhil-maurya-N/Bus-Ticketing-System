from email.mime import image
from tkinter import font
from PIL import Image,ImageDraw,ImageFont

draw=Image.open("1.jpg")
font1=ImageFont.truetype("chiller",100)
points=100,80
string="Nikhil"
color ="red"
draw.text(points,string,color,font1)
image.show()