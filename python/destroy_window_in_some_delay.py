#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of tkinter frame
win = Tk()

#Set the geometry of tkinter frame
win.geometry("750x270")

#Initialize a Label widget
Label(win, text= "This window will get closed after 3 seconds...",
font=('Helvetica 20 bold')).pack(pady=20)

#Automatically close the window after 3 seconds
win.after(3000,lambda:win.destroy())

win.mainloop()
