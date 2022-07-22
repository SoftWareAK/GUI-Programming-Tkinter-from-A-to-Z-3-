#Python ile görsel programlama
#GUI-Kullanıcı arayüzü tasarımı

import tkinter as tk

pencere = tk.Tk()
pencere.geometry("500x500+55+55")
pencere.title( " byKurt")
pencere.configure(bg="blue")

etiket=tk.Label(text="GaraAmadoğulları",font="Veranda 22 bold")
etiket.pack()

#pack() kompenentleri paketliyor
#grid() arayüzü parçalara bölüyor
#place() x,y kordinatları ile yerleşiyor


pencere.mainloop()
