import tkinter as tk
from tkinter import *

def create_window():
    t2=Toplevel(bg="blue")

window=tk.Tk()


t1=Toplevel(bg="RED")


b=Button(text="create a window",command=create_window)
b.place(x=10,y=10)

window.mainloop()