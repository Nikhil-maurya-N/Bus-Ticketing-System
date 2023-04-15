### Hi there  this project is in early developement.... stay tuned for updates :)
$$$
<!--
**Nikhil-maurya-N/Nikhil-maurya-N** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on E- bus ticketing system 
- 🌱 I’m currently learning python, Databases

E-Bus Ticketing System

--->Introduction:
The traditional bus ticketing system is often associated with
long queues and delays, making it a tedious and time-consuming
process for passengers. Moreover, with the recent COVID-19
pandemic, there has been a growing demand for contactless
transactions to minimize the risk of transmission. To address these
challenges, the e-bus ticketing system using QR code presents a
modern and efficient solution for bus operators and passengers.
We have assured the faster and safer transactions with
proper validation of the particular passenger’s ticket fees.
Although we have integrated the system in a single program but
when it will actually operable then we may make it to many
fractions and assign many roles such as:
1. Admin (backend manager)
2. Agent (for recharging passengers)
3. Operator (the bus conductor who uses this to collect the
fees)
4. Passenger (who has his QR-code containing information
name@addharnumber).
--->Objective
This project aims to develop a comprehensive e-bus ticketing
system that utilizes QR codes to facilitate a hassle-free and
contactless ticketing experience for passengers. With this system,
passengers can easily purchase and validate their tickets through a
mobile application, eliminating the need for physical tickets or cash
transactions. Bus operators can also manage their routes and ticket
sales through a back-end system, providing real-time data on ticket
sales and passenger traffic.
The use of QR codes in this system provides numerous
benefits, including faster ticket validation, reduced waiting time for
passengers, and improved accuracy in ticket validation.
Furthermore, with the growing popularity of smartphones and
mobile devices, the adoption of this system is expected to be high
among passengers.
Overall, the e-bus ticketing system using QR code presents a
modern and innovative solution to the challenges faced by
traditional bus ticketing systems. It is a step towards a more
efficient and convenient mode of transportation for both bus
operators and passengers.
The Working Algorithm
The Algorithm of the project e-bus ticketing system is that it is
mainly divided into following parts:
1. Database Creation (Named ‘passenger_details’)
2. Connection to database
3. New passenger (Registration of passenger)
4. Login
5. Scan for Entry
6. Scan for Exit
These are main modules used to complete this whole
project the main external modules which are used in its
source code to create it are as follows:
• FPDF
• qrcode
• tkinter
• messagebox
• tkinter.messagebox as tmsg
• PIL
• mysql.connector
• datetime
• os
• web browser
1. Database Creation:
We need to create a base database and a main table
named personal for storing personal information of the
passengers so that the further operations can occur.
We have two external supportive files for creation of
base database named:
• Database_creationFile.sql (SQL file)
• PythonScriptToCreateMainDB.py (python script file)
•
There are 8 entities in the personal table of the database. We
have to used many of the details in this table to perform
various operation like login scan in scan out etc. The E-R
diagram for that is at Next page please visit
Another sub Tables is needed in this database to store
various transaction records and calculation module this is
abbreviated as nameofpassengerAadharofpassenger by
merging the name of passenger and his Aadhar the name of
a table might look like:
Name-Abhav Yadav
Aadhar-123456789012
So, the table name will look like: ‘Abhavyadav123456789012’
Passenger
Name
Aadhar Gender
Mobile_no
Email
password state
Total_balance
E-R Diagram of personal
nameAadhar
board_time
TransitionId
amount_difference
statement
departure_time
total_balanc
e
E-R Diagram of sub-table
2. Connection to database:
For connection of database, we have a function named as
connect_To_DB and its belonging functions which uses mysql.connector
module mainly. It asks user his password if default password is incorrect
and saves it to a file named as ‘pass.txt’ in same directory where whole
source code is present. It uses following algorithm:
I. Try reading ‘pass.txt’
II. If ‘pass.txt’ exists then redline which is password saved before
III. Else increment flag
IV. Try connecting to database
V. If exception occurs it means password is wrong and asks user again
for password of database.
3. New passenger:
It is an admin or agent side operation which is responsible for
registration of new passenger by GUI based frame pop up technologies
used in this function is Tkinter and MySQL connector.
This New passenger is a menu and has six GUI based labels and
entries named as follows:
• Name
• Gender
• Mobile_no
• Email
• Aadhar
• Password
And in last there is a button named as Register which when
pressed validates the data and it the data entered is valid then it saves
it into the database named as passenger_details’ personal which we
have earlier created by python scripts provided in the package. There is
various validation function which resists users entering wrong data or
and inappropriate data that can crash or confuse the database system.
Such that:
• Callback
• Callback1
• Callback2
4. Login:
This module is very important for various operations the main
credentials use in this are Aadhar and password. We are using login
by two methods:
o By QR code
o By Aadhar and password
By Aadhar and password:
We have a login method in the module for this operation
and supporting methods which takes value as argument which
defines the various operations like:
• De-activation
• Recharge
• Get Records
• Get QR code
By QR code:
We call it indirect method which is used by passenger to
transit the fees of transportation by automation. We have
discussed it brief in next Heading please refer to that for details.
This takes name and Aadhar of user to get logged in for accessing
the database of user and performing transitional operations like
calculation and updating of records in sub table.
5. Scan for Entry:
Passenger use this feature when they have to board in to the bus
for this operation, we have function called entry_bus and supporting
methods such as savedata which and uses sub table of the that
particular passenger name like name + Aadhar ->
‘raddha123456789873’ in which the algorithm goes like:
i. Start
ii. QR scanned
iii. Extract data from that
iv. Pass data to savedata function
v. Perform some validation
vi. Auto increment TransitionId and save board time
vii. Update the state value to 1
viii. Exit
6. Scan for Exit:
Passenger use this feature when they have to leave the bus an
deduce his fees for departure and so when have to calculate the
amount and save the information in the database and also fetch
some data from database so hence there are is a function for
performing this operation named as exit_bus and supporting
functions for this to do some side calculation and operation to
execute the need. For this we have this Algorithm:
i. Start
ii. Scan QR code
iii. Extract data from it
iv. Send it to a supporting function named as calculate
v. Perform validations
vi. Trim the data into information we need
vii. Fetch data from database such as board time
viii. Calculate the total money by passing it to the moneycal
function
ix. The moneycal function calculates the cost by 1sec
travel=1/60 unit money and return it
x. Show the message and save the record to the database
xi. Exit
So hence, like this the modules of the whole project. We have
integrated all the modules in a single program because it is a
prototype module we need to disintegrate the modules once it
will be on the actual production use .We also have some side
modules which help it to work efficiently These helping modules
completes the modules operations so that they can be used by
users or backend admit to perform some specific operations some
of them are as follows:
i. Recharge
ii. Deactivation
iii. Get QR
iv. Get records
Hardware and Software requirements
For hardware requirements we Don’t need anything any so
specific but we are using QR as our core Idea so we need
following hardware:
Laptop including following things:
i. 4GB of ram and 2.5 GHz of processing power
ii. Webcam
iii. Basic I/O devices
For software we need some software and a basic and
general purpose software running environment we need following
software:
o Python (3.11.0)
o MySQL (8.0.32)
o MySQL server (8.0.32)
o
For development I used Microsoft’s visual studio Code as an
IDE for better interface debugging and testing.
The version of my V. S. code is 1.76. Which is very good and
stable for development of any GUI based application using
python Tkinter or any GUI Based technology.
Data flow diagram
Current Problems and area of improvement
Current Problems:
1. Long queues and delays in traditional bus ticketing systems
2. Physical ticketing can be lost, damaged or misplaced
3. Risk of cash transactions and physical contact during the
COVID-19 pandemic
4. Inefficient data management and ticket sales tracking by bus
operators
5. Lack of real-time data on passenger traffic and ticket sales
Areas of Improvement:
1. Faster and more convenient ticket purchasing process for
passengers
2. Contactless and safer ticketing experience for passengers
during the COVID-19 pandemic
3. Real-time data on passenger traffic and ticket sales for bus
operators to optimize their services
4. Accurate and efficient ticket validation process for bus
conductors
5. Efficient and centralized data management system for ticket
sales tracking by bus operators
Future or Scope of the project
The scope of the e-bus ticketing system using QR code project
involves the development of a comprehensive ticketing solution
that leverages QR codes to facilitate a seamless and contactless
ticketing experience for passengers. The project will cover the
following aspects:
1. Mobile Application Development:
A mobile application will be developed for passengers
to purchase and validate tickets. The application will allow
passengers to select their desired bus routes, view ticket
prices, and purchase tickets using various payment options.
2. QR Code Generation:
A unique QR code will be generated for each ticket
purchased through the mobile application. The QR code will
serve as the ticket and will be scanned by bus conductors to
validate the ticket.
3. Back-End System Development:
A back-end system will be developed for bus operators
to manage their routes, ticket sales, and passenger data. The
system will provide real-time data on ticket sales and
passenger traffic, allowing operators to optimize their
services based on demand.
4. QR Code Scanner Integration:
A QR code scanner will be integrated with the system to
validate tickets. The scanner will be installed on buses and
used by conductors to scan the QR codes on passengers'
tickets.
from the traditional ticketing system to the new e-bus
ticketing system using QR code.
The scope of this project is to deliver a fully functional and
integrated e-bus ticketing system that enhances the overall
efficiency of bus services, reduces waiting time for passengers,
and provides a safer and contactless ticketing experience.
Conclusion
In conclusion, the e-bus ticketing system using QR code presents
a modern and innovative solution to the challenges faced by
traditional bus ticketing systems. By leveraging the power of QR
codes and mobile applications, this system provides a fast, safe,
and efficient ticketing experience for passengers while also
streamlining ticket sales and passenger data management for bus
operators.
The development of this system represents a significant step
towards a more efficient and convenient mode of transportation
for both bus operators and passengers. It is expected to reduce
waiting times, improve the accuracy of ticket validation, and
provide a contactless and safer ticketing experience, especially
during the current COVID-19 pandemic.
Overall, this project provides a comprehensive and practical
solution to the challenges faced by traditional bus ticketing
systems. The e-bus ticketing system using QR code is an excellent
example of how technology can be leveraged to enhance the
efficiency and convenience of public transportation systems.

