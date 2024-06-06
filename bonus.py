import tkinter as tk
from random import randint as rn

def dectohex():
    fen = tk.Tk()
    fen.title("Conversion décimal-hexadécimal")
    fen.geometry("400x200")
    fen.configure(bg='gray')

    F1 = tk.Frame(fen, bg='gray')
    F1.pack()
    l1 = tk.Label(F1, text="Entrez un nombre décimal", bg='gray', fg='white')
    l1.grid(row=0, column=0)
    en1 = tk.Entry(F1, bg='white', fg='black', width=20)
    en1.grid(row=1, column=0)
    l2 = tk.Label(F1, text="Le nombre en hexadécimal est", bg='gray', fg='white')
    l2.grid(row=0, column=1)
    en2 = tk.Entry(F1, bg='white', fg='black', width=20)
    en2.grid(row=1, column=1)

    def zzconv():
        try:
            en2.delete(0, tk.END)
            en2.insert(0, (hex(int(en1.get()))).lstrip("0x"))
        except:
            en2.delete(0, tk.END)
            en2.insert(0, "Entrez un nombre valide")
    bt = tk.Button(fen, text="Convertir", bg='orange', fg='white', width=20, command=zzconv)
    bt.pack()
    fen.mainloop()

def ChoixCouleur():
    fen = tk.Tk()
    fen.title("Choix aléatoire de couleur")
    fen.geometry("400x200")
    fen.configure(bg='gray')

    L1 = tk.Label(fen, text="Couleur aléatoire", bg='gray', fg='white')
    L1.pack()
    E = tk.Entry(fen, bg='white', fg='black', width=20)
    E.pack()
    def setcol():
        E.delete(0, tk.END)
        c = str(hex(rn(0x100000, 0xffffff))).replace("0x", "#")
        E.insert(0,c)
        fen.configure(bg=c)
    B = tk.Button(fen, text="Générer", bg='orange', fg='white', width=20, command=setcol)
    B.pack()
    fen.mainloop()

# dectohex()
ChoixCouleur()