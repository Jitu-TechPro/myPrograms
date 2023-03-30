import os
import socket
from datetime import datetime
import sqlite3
import mysql.connector

# this will get logged in user name
uname=os.getlogin()
#print(uname)

# this will get system name
sname=socket.gethostname()
#print(sname)

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

#login_details= (dt_string, uname, sname)

#print(login_details)

f1=open("logins.txt", "a")
f1.write(dt_string)
f1.write("\t")
f1.write(uname)
f1.write("\t")
f1.write(sname)
f1.write("\n")
f1.close()

conn = sqlite3.connect('userLogins.db')

cursor = conn.cursor()

#table = """CREATE TABLE LOGINS(SN INTEGER PRIMARY KEY AUTOINCREMENT, DATE VARCHAR(255), UNAME VARCHAR(255), SNAME VARCHAR(255));"""

#cursor.execute(table)

cursor.execute('INSERT INTO LOGINS (DATE, UNAME, SNAME) VALUES (?, ?, ?)', (dt_string, uname, sname))

conn.commit()

conn.close()

mydb = mysql.connector.connect(
    host='localhost',
    user='dbuser',
    password='DbUser@2023',
    database='userlogins'
)

mycursor = mydb.cursor()

#table = "CREATE TABLE LOGINS(id INT AUTO_INCREMENT PRIMARY KEY, DATE VARCHAR(255), UNAME VARCHAR(255), SNAME VARCHAR(255))"

#mycursor.execute(table)

sql = 'INSERT INTO LOGINS (DATE, UNAME, SNAME) VALUES (%s, %s, %s)'
val = (dt_string, uname, sname)

mycursor.execute(sql, val)

mydb.commit()
