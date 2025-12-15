from tkinter import Label, Tk, mainloop
from time import strftime

window = Tk()
window.title("Digital Clock")

def time():
    mytime = strftime("%H:%M:%S %p")
    clock.config(text = mytime)
    clock.after(1000, time)

clock = Label(window,
              font = ("arial",48, "bold"),
              background= "dark green",
              foreground= "white")

clock.pack(anchor= "center")
time()

mainloop()