import tkinter as tk
from tkinter import*

def degistir(val):
    etiket.configure(font="Verdana "+val)

pencere=tk.Tk()

deger=StringVar()
slider=Scale(from_=2,to=20,orient=HORIZONTAL,command=degistir)
slider.place(x=10,y=10)


etiket=Label(text="Etiket")
etiket.place(x=20,y=100)

pencere.mainloop()