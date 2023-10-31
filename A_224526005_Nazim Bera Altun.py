import tkinter as hsp
from tkinter import ttk

def sayi_tikla(sayi):
    ekran_entry.insert(hsp.END, sayi)

def hesapla():
    try:
        sonuc = eval(ekran_entry.get())
        ekran_entry.delete(0, hsp.END)
        ekran_entry.insert(hsp.END, sonuc)
    except:
        ekran_entry.delete(0, hsp.END)
        ekran_entry.insert(hsp.END, "Hata")

def temizle():
    ekran_entry.delete(0, hsp.END)

pencere = hsp.Tk()
pencere.title("Hesap Makinesi")

ekran_entry = ttk.Entry(pencere, font=('Segoe UI', 20))
ekran_entry.grid(row=0, column=0, columnspan=4)

butonlar = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

sira, kolon = 1, 0

for buton in butonlar:
    ttk.Button(pencere, text=buton, command=lambda b=buton: sayi_tikla(b)).grid(row=sira, column=kolon)
    kolon += 1
    if kolon > 3:
        kolon = 0
        sira += 1

ttk.Button(pencere, text="=", command=hesapla).grid(row=5, column=0, columnspan=4)
ttk.Button(pencere, text="C", command=temizle).grid(row=6, column=0, columnspan=4)

pencere.mainloop()
