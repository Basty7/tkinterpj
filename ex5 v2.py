import tkinter as tk
import datetime

fen = tk.Tk()
fen.title("L'heure")
fen.geometry("400x200")

color = "#123456"

def get_time():
    current_time = datetime.datetime.now().time()
    formatted_time = current_time.strftime("%H:%M")
    return [int(i) for i in formatted_time.split(':')]

def timeFrames():
    time = get_time()
    canvas.delete("all")

    for i in range(time[0]//5):
        canvas.create_rectangle(i*200/4, 0, (i+1)*200/4, 24, fill=color, outline="gray")
    for i in range(time[0]%5):
        canvas.create_rectangle(i*200/4, 25, (i+1)*200/4, 49, fill=color, outline="gray")
    for i in range(time[1]//5):
        canvas.create_rectangle(i*200/12, 50, (i+1)*200/12, 74, fill=color, outline="gray")
    for i in range(time[1]%5):
        canvas.create_rectangle(i*200/4, 75, (i+1)*200/4, 100, fill=color, outline="gray")
    
def init_fen():
    global h5, h1, m5, m1, frame2, bigframe, Lh5, Lh1, Lm5, Lm1, Ltime, canvas
    bigframe = tk.Frame(fen)
    bigframe.pack()
    canvas = tk.Canvas(bigframe, width=200, height=100, bg="black")
    canvas.grid(row=0, column=0)
    frame2 = tk.Frame(bigframe)
    frame2.grid(row=0, column=1)

    Lh5 = tk.Label(frame2, text="Cinq heures" ), Lh5.pack()
    Lh1 = tk.Label(frame2, text="Une heure" ), Lh1.pack()
    Lm5 = tk.Label(frame2, text="Cinq minutes" ), Lm5.pack()
    Lm1 = tk.Label(frame2, text="Une minute" ), Lm1.pack()

    Ltime = tk.Label(fen, text="Il est actuellement :")
    Ltime.pack()

    clFrame = tk.Frame(fen)
    clFrame.pack()

    colorE = tk.Entry(clFrame)
    colorE.grid(row=0, column=0)
    colorE.insert(0, color)
    def changeColor():
        global color
        color = colorE.get()
        timeFrames()
    colorB = tk.Button(clFrame, text="Changer la couleur", command=changeColor)
    colorB.grid(row=0, column=1)


def update_time():
    timeFrames()

    Ltime['text'] = "Il est actuellement : " + str(get_time()[0]) + " heures et " + str(get_time()[1]) + " minutes"

    fen.after(10000, update_time)

if __name__ == "__main__":
    init_fen()
    update_time()
    fen.after(10000, update_time)

        
    fen.mainloop()
