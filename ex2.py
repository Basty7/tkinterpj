import tkinter as tk
from random import randint as rn

fen = tk.Tk()
fen.title("Lignes et cercles aléatoires")
fen.geometry("500x500")
fen.background = "white"

can = tk.Canvas(fen, bg=fen.background, height=500, width=500)

def choixCouleur():
        return str(hex(rn(0x100000, 0xffffff))).replace("0x", "#")

def random_line():
    x1 = rn(0, 500)
    y1 = rn(0, 500)
    x2 = rn(0, 500)
    y2 = rn(0, 500)
    color = choixCouleur()
    can.create_line(x1, y1, x2, y2, fill=color)

def random_circle():
    x = rn(0, 500)
    y = rn(0, 500)
    r = rn(0, 100)
    color = choixCouleur()
    can.create_oval(x-r, y-r, x+r, y+r, outline=color, fill=color)

f1 = tk.Frame(fen, bg=fen.background)

b1 = tk.Button(f1, text="Ligne aléatoire", command=random_line)
b1.grid(row=0, column=0)
b2 = tk.Button(f1, text="Cercle aléatoire", command=random_circle)
b2.grid(row=0, column=1)
f1.pack()
can.pack()

fen.mainloop()