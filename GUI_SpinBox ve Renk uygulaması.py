import tkinter as tk
from tkinter import *

def renk():
    r=sred.get()  #0x5    0xb
    g=sgreen.get()
    b=sblue.get()
    #hex 16'LIK kod dönüştürme
    rh=hex(int(r))
    gh =hex(int(g))
    bh =hex(int(b))
    color= "#" + rh.replace("0x","") + gh.replace("0x","") + bh.replace("0x","")
    print(color)
    pencere.configure(bg=color)   #6b3    6 kırmızı  b =11 =yeşil    3 mavi demek






pencere=tk.Tk()
pencere.geometry("300x300")



sred=Spinbox(font="Verdana 12",from_=0,to=15,width=5,command=renk)
sred.place(x=80,y=20)
lred=Label(text="Kırmızı")
lred.place(x=20,y=20)

sgreen=Spinbox(font="Verdana 12",from_=0,to=15,width=5,command=renk)
sgreen.place(x=80,y=50)
lgreen=Label(text="Yeşil")
lgreen.place(x=20,y=50)

sblue=Spinbox(font="Verdana 12",from_=0,to=15,width=5,command=renk)
sblue.place(x=80,y=80)
lblue=Label(text="Mavi")
lblue.place(x=20,y=80)






pencere.mainloop()