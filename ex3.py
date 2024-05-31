import tkinter as tk 
from random import choice

fenetre = tk.Tk()
fenetre.title("Pierre, Feuille, Ciseaux !")
fenetre.geometry("600x300")
fenetre.configure(bg='gray')

labeljoueur = tk.Label(fenetre, text="Choix du joueur", bg='gray', fg='white', width=20, font=("Arial", 14))
choixJoueur = tk.Frame(fenetre, bg='gray')
btnJPierre = tk.Button(choixJoueur, text="Pierre", bg='orange', fg='white', width=20, command=lambda: choixJoueur("Pierre"), font=("Arial", 12))
btnJFeuille = tk.Button(choixJoueur, text="Feuille", bg='orange', fg='white', width=20, command=lambda: choixJoueur("Feuille"), font=("Arial", 12))
btnJCiseaux = tk.Button(choixJoueur, text="Ciseaux", bg='orange', fg='white', width=20, command=lambda: choixJoueur("Ciseaux"), font=("Arial", 12))


labeljoueur.pack()
btnJPierre.grid(row=0, column=0)
btnJFeuille.grid(row=0, column=1)
btnJCiseaux.grid(row=0, column=2)
choixJoueur.pack()


labelordi = tk.Label(fenetre, text="Choix de l'ordinateur", bg='gray', fg='white', width=20, font=("Arial", 14))
fchoixOrdi = tk.Frame(fenetre, bg='gray')
btnOPierre = tk.Button(fchoixOrdi, text="Pierre", bg='orange', fg='white', width=20, font=("Arial", 12))
btn0Feuille = tk.Button(fchoixOrdi, text="Feuille", bg='orange', fg='white', width=20, font=("Arial", 12))
btn0Ciseaux = tk.Button(fchoixOrdi, text="Ciseaux", bg='orange', fg='white', width=20, font=("Arial", 12))

labelordi.pack()
btnOPierre.grid(row=0, column=0)
btn0Feuille.grid(row=0, column=1)
btn0Ciseaux.grid(row=0, column=2)
fchoixOrdi.pack()

vainqueur = tk.Label(fenetre, bg='gray', fg='white', width=40, font=("Arial", 20))
attendre = tk.Label(fenetre, bg='gray', fg='white', width=40)
vainqueur.pack()
attendre.pack()

def reset():
    attendre.configure(text="Une nouvelle partie va commencer", font=("Arial", 14))
    for child in fchoixOrdi.winfo_children():
        child.configure(state=tk.NORMAL)

    vainqueur.configure(text="")
    attendre.configure(text="")


def choixJoueur(choix):
    list = ["Pierre", "Feuille", "Ciseaux"]
    choixOrdi = choice(list)

    for child in fchoixOrdi.winfo_children():
        if child.cget("text") == choixOrdi:
            child.invoke()
        else:
            child.configure(state=tk.DISABLED)

    if choix == choixOrdi:
        resultat = "égalité"
    elif list.index(choix) == (list.index(choixOrdi) + 1) % 3:
        resultat = "gagné"
    else:
        resultat = "perdu"

    vainqueur.configure(text=f"Vous avez {resultat}")

    print(resultat)

    fenetre.after(2000, reset)


fenetre.mainloop()