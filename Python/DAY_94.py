from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p') # format 24 Jam, 
#string = strftime('%I:%M:%S %p') # format 12 Jam, 
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital",35), background = "black", foreground = "red")
label.pack(anchor='center')
time()

mainloop()