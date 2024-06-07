import tkinter as tk
fen = tk.Tk()
fen.title("Les bonus")
fen.geometry("400x200")
fen.configure(bg='gray')

menuEx1a5 = tk.Menu(fen)
menuEx1a5.pack()
def switch(n):
    if n == 1:
        exec(open("ex1.py").read())
    elif n == 2:
        exec(open("ex2.py").read())
    elif n == 3:
        exec(open("ex3.py").read())
    elif n == 4:
        exec(open("ex5%20v2.py").read())
    elif n == 5:
        exec(open("bonus.py").read())
menuEx1a5.add_command(label="Exo 1", command=lambda: switch(1))
menuEx1a5.add_command(label="Exo 2", command=lambda: switch(2))
menuEx1a5.add_command(label="Exo 3", command=lambda: switch(3))
menuEx1a5.add_command(label="Exo 4", command=lambda: switch(4))
menuEx1a5.add_command(label="Exo 5", command=lambda: switch(5))

fen.mainloop()