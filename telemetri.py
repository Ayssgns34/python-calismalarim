import tkinter as tk
import random
def veri_guncelle():
    yeni_hiz=random.randint(0,15)
    yeni_batarya=random.randint(80,100)

    hiz_etiketi.config(text=f"Hız:{yeni_hiz} km/s")
    batarya_etiketi.config(text=f"Batarya:&{yeni_batarya}")
    pencere.after(1000,veri_guncelle)



pencere=tk.Tk()
pencere.title(" İKA Telemetri İstasyonu")
pencere.geometry("400x300")
pencere.configure(bg='black')

baslik=tk.Label(pencere,text="İKA CANLI VERİ AKIŞI", font=("Arial",14,"bold"),bg="black",fg="cyan")
baslik.pack(pady=10)

hiz_etiketi=tk.Label(pencere,text="Hız: O km/s", font=("Arial",12),bg="black",fg="white")
hiz_etiketi.pack(pady=5)

batarya_etiketi=tk.Label(pencere, text="Batarya:%100" , font=("Arial",12),bg="black",fg="green")
batarya_etiketi.pack(pady=5)

veri_guncelle()
pencere.mainloop()
