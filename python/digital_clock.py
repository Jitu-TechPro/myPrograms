from datetime import datetime
from tkinter import Tk, Label

window = Tk()
window.title("Digital Clock")
window.geometry("600x300")
window.configure(bg="gray")

label = Label(window, font=("Ariel Black",78,"bold"), bg="gray", fg="white")
label.pack(pady=100) 

def clock():
    time  = datetime.now().strftime("%H:%M:%S")
    label.configure(text=time)
    label.after(500,clock)

clock()
window.mainloop()