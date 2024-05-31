import tkinter as tk
from tkinter import ttk
import datetime

fen = tk.Tk()
fen.title("L'heure")
fen.geometry("400x200")


def get_time():
    current_time = datetime.datetime.now().time()
    formatted_time = current_time.strftime("%H:%M:%S")
    ft = [int(i) for i in formatted_time.split(':')][0:2]
    return ft

def init_fen():
    global h5, h1, m5, m1, frame1, frame2, bigframe, Lh5, Lh1, Lm5, Lm1, Ltime
    bigframe = tk.Frame(fen)
    bigframe.pack()
    frame1 = tk.Frame(bigframe)
    frame1.grid(row=0, column=0)
    frame2 = tk.Frame(bigframe)
    frame2.grid(row=0, column=1)

    h5 = ttk.Progressbar(frame1, length=200, orient="horizontal", mode="determinate", maximum=4)
    h5.pack()
    h1 = ttk.Progressbar(frame1, length=200, orient="horizontal", mode="determinate", maximum=4)
    h1.pack()
    m5 = ttk.Progressbar(frame1, length=200, orient="horizontal", mode="determinate", maximum=11)
    m5.pack()
    m1 = ttk.Progressbar(frame1, length=200, orient="horizontal", mode="determinate", maximum=4)
    m1.pack()

    Lh5 = tk.Label(frame2, text="Cinq heures")
    Lh5.pack()
    Lh1 = tk.Label(frame2, text="Une heure")
    Lh1.pack()
    Lm5 = tk.Label(frame2, text="Cinq minutes")
    Lm5.pack()
    Lm1 = tk.Label(frame2, text="Une minute")
    Lm1.pack()

    Ltime = tk.Label(fen, text="Il est actuellement :")
    Ltime.pack()


def update_time():
    time = get_time()
    h5["value"] = time[0]//5
    h1["value"] = time[0]%5
    m5["value"] = time[1]//5
    m1["value"] = time[1]%5

    Ltime['text'] = "Il est actuellement : " + str(time[0]) + " heures et " + str(time[1]) + " minutes"

    fen.after(10000, update_time)

if __name__ == "__main__":
    init_fen()
    update_time()
    fen.after(10000, update_time)

        
    fen.mainloop()
