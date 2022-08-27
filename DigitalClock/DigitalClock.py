from tkinter import *
from time import strftime, sleep
from datetime import *
import time

root = Tk()
label = Label(root, fg = "cyan",bg = "black",font = ("Times New Roman", 40))

def show_time():
    string = strftime(f"%H:%M:%S %p ")
    label.config(text=string)
    label.after(100, show_time)
    label.pack()

show_time()
root.mainloop()

