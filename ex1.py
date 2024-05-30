import tkinter as tk

fenetre = tk.Tk()

fenetre.title("Longueur de l'hypothénuse")
fenetre.configure(bg='black', width=200)

def calcul():
    try:
        A = float(Ainput.get())
        B = float(Binput.get())
    except: 
        Coutput.delete(0, tk.END)
        Coutput.insert(0, "Veuillez entrer des nombres")
        return
    C = (A**2 + B**2)**0.5
    Coutput.delete(0, tk.END)
    Coutput.insert(0, C)

txt1 = tk.Label(fenetre, text="Longueur du côté A :", fg='white', bg='black', width=20)
Ainput = tk.Entry(fenetre, bg='gray', fg='white', width=20)
txt2 = tk.Label(fenetre, text="Longueur du côté B :", fg='white', bg='black', width=20,)
Binput = tk.Entry(fenetre, bg='gray', fg='white', width=20)
txt3 = tk.Label(fenetre, text="Longueur de l'hypothénuse", fg='white', bg='black', width=20)
Coutput = tk.Entry(fenetre, bg='gray', fg='white', width=20)
btn = tk.Button(fenetre, text="Calculer", bg='orange', fg='white', width=20, command=calcul)
btn2 = tk.Button(fenetre, text="Quitter", bg='orange', fg='white', width=20, command=fenetre.quit)

txt1.grid(row=0, column=0)
Ainput.grid(row=0, column=1)
txt2.grid(row=1, column=0)
Binput.grid(row=1, column=1)
txt3.grid(row=2, column=0)
Coutput.grid(row=2, column=1)
btn.grid(row=3, column=0)
btn2.grid(row=3, column=1)

fenetre.mainloop()
