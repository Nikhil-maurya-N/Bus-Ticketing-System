# data="Nikhil kjas 303343108922"
# temp=str()
# for i in data:
#     if i.isalpha() or i==" ":
#         temp+=i
# addhar=data.replace(temp,"")
# print("|"+addhar+"|")
import datetime
import time

curr=datetime.datetime.now()
c=int(round(curr.timestamp()))
print(c)
time.sleep(10)
curr=datetime.datetime.now()
d=int(round(curr.timestamp()))
print(d)
print(d-c)


