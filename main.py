import tkinter as tk

fenetre = tk.Tk()

fenetre.geometry("600x300")

fenetre.title("TG!")
fenetre.configure(bg='black')

txt_aLaCon = tk.Label(fenetre, text="Hello World", bg='orange', fg='white', width=10, height=5)
txt_aLaCon.pack()

txt_aLaCon.configure(text="Je suis là")

txt_aLaCon.bind("<Button-1>", lambda e: txt_aLaCon.configure(text="J'ai été cliqué"))

fenetre.mainloop()