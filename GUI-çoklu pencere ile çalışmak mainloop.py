#mainloop'u anlamak
#Çoklu pencere ile çalışmak

import tkinter as tk

pencere1=tk.Tk()
pencere1.title("First ")
pencere1.configure(bg="red")

pencere1.mainloop()

pencere2=tk.Tk()
pencere2.title("second")
pencere2.configure(bg="yellow")
pencere2.mainloop()
#eğer ki pencere 2 nin pencere 1 ile aynı anda açılmasını istiyorsan pencere 2 nin kodlarını 1 in kodlari ile  1 in mainloopu arasına yaz
