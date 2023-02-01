# import qrcode
# user_qrcode=qrcode.make("https://github.com/Nikhil-maurya-N")
# user_qrcode.save("qrcode.png")
# user_qrcode.show()
import mysql.connector
print("Hello1")
mydb=mysql.connector.connect(host='localhost',user='root',password='nikhil',database='passenger_details')
pointer=mydb.cursor()
# print(QueryID)
print("Hello2")
sql="insert into personal(name, Gender, Mobile_no, Email, Addhar, passward ) values('ndsfsil','male','2343978','nikhil0ds','66767','fvfdssdkks')"
pointer.execute(sql)
mydb.commit()
sql="select * from personal"
pointer.execute(sql)
D=pointer.fetchall()
for i in D:
    print(i)


print("hello3")
