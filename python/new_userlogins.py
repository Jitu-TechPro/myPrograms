import os
import socket
from datetime import datetime
import sqlite3

# following section collects system's date, time, usename and systemname

def getUserName():
    # this will get logged in user name
    return os.getlogin()    

uname = getUserName()

def getSystemName():
    # this will get system name
    return socket.gethostname()

sname = getSystemName()        

def getSystemDate():
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")    
    return date

date = getSystemDate()

def getSystemTime():
    now = datetime.now()
    time = now.strftime("%H:%M")    
    return time

time = getSystemTime()

# This secion writes collected data to a text file

def writeDataToFile():
    with open("new_logins.txt", "a") as file:
        file.write(date)
        file.write("\t")
        file.write(time)
        file.write("\t")
        file.write(uname)
        file.write("\t")
        file.write(sname)
        file.write("\n")

writeDataToFile()

# This section reads the created text file

def readDataFromFile():
    with open("new_logins.txt", "r") as file:
        file_stuff = file.read()
        print(file_stuff)

readDataFromFile()

# This section writes the data to a Sqlite3 database

sqlite_conn = sqlite3.connect("C:\msys64\mingw64\lib\sqlite3.38.5\mingw.db")
cursor = sqlite_conn.cursor()

try:
    table = 'CREATE TABLE Logins (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, time TEXT, uname TEXT, sname TEXT);'
    cursor.execute(table)
except:
    cursor.execute('INSERT INTO Logins (date, time, uname, sname) VALUES (?, ?, ?, ?)', (date, time, uname, sname))

sqlite_conn.commit()
sqlite_conn.close() 
