import tkinter as tk
from random import choice, shuffle

# Fn : choisit un mot aléatoire dans le fichier dictionnaire7-10.txt
def choisir_mot():
    with open("dictionnaire7-10.txt", "r") as f:
        mots = [mot.rstrip("\n") for mot in f]
    return choice(mots)

fenetre = tk.Tk()
resultFrame = tk.Frame(fenetre)
label_mot = tk.Label(fenetre, bg='gray', fg='white', width=40, font=("Arial", 14))
fEntree = tk.Frame(fenetre, bg='gray')
Entree = tk.Entry(fEntree)
Entree.insert(0, "Entrez un mot")
Essayer = tk.Button(fEntree, text="Essayer")
new = tk.Button(fEntree, text="Nouveau mot")

# Fn : Appelle set_mot() et effectue les modifications nécessaires
def set_mot():
    mot_choisi = choisir_mot()
    mot = list(mot_choisi)
    shuffle(mot)
    label_mot.config(text="Mot à trouver : " + ''.join(mot))
    print(mot_choisi)
    Essayer.config(command=lambda: verifier_mot(Entree, mot_choisi))
    Entree.bind("<Return>", lambda event: verifier_mot(Entree, mot_choisi))
    return mot_choisi

# Fn : Crée la fenêtre principale
def main():
    fenetre.title("Mot caché")
    fenetre.geometry("600x300")
    fenetre.configure(bg='gray')

    
    mot_choisi = set_mot()
    new.config(command=set_mot)
    label_mot.pack()
    Entree.grid(row=0, column=0, padx=10)
    Essayer.grid(row=0, column=1, padx=10)
    new.grid(row=0, column=2, padx=10)
    fEntree.pack()
    resultFrame.pack()

# Fn : Vérifie si le mot entré est correct
def verifier_mot(Entree:tk.Entry, mot_choisi:str):
    mot = Entree.get().upper()
    for child in resultFrame.winfo_children():
        child.destroy()
    if mot == mot_choisi:
        label_resultat = tk.Label(resultFrame, text="Bravo, vous avez trouvé le mot caché !", bg='gray', fg='white', font=("Arial", 14))
        set_mot()
    else:
        label_resultat = tk.Label(resultFrame, text="Désolé, ce n'est pas le mot caché. Réessayez !", bg='gray', fg='white', font=("Arial", 14))
    label_resultat.pack()
    Entree.delete(0, tk.END)


# Appel de la fonction main
if __name__ == "__main__":
    main()
    fenetre.mainloop()