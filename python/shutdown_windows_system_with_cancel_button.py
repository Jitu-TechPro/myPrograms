# Title - Program to shutdown the system at specific time 
# If somebody is using the system at that time he can cancel the shutdown 
# Or the system will get shutdown in specified timeout
#************************************************************************
# Author - Subhash Bhalerao
# Version - 1.0
#************************************************************************
import os
#loading Tkinter library
import tkinter as tk

def cancel_shutdown():
	master.destroy()

#Tkinter object
master = tk.Tk()

#Set geometry of Tkinter frame
master.geometry("750x250")

# background set to grey
#master.configure(bg="light gray")

#Set Labels and Texts for user reference
warning = tk.Label(text="Warning", fg="Red", font=("Helvetica", 18))
warning.pack()

msg_txt_1 = tk.Label(text="The system is going to shutdown in 5 minutes, save your work", font=("Helvetica", 14))
msg_txt_1.pack()

msg_txt_2 = tk.Label(text="If you are still using the system, click on Cancel button now", font=("Helvetica", 14))
msg_txt_2.pack()

empty_lines = tk.Label(text="")
empty_lines.pack()

button = tk.Button(text="Cancel Shutdown", command=cancel_shutdown, fg="Red", font=("Helvetica", 18) )
button.pack()

#Automatically close the window after 5 seconds
master.after(300000,lambda:os.system("shutdown /s /t 00"))

tk.mainloop()

