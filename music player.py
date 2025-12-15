import os
import tkinter as tk
from pygame import  mixer
from tkinter import filedialog

mixer.init()

root = tk.Tk()
root.title("Music Player")
root.geometry("530x350")
root.config(bg='black')

playlist = tk.Listbox(
    root, bg= "black",
    fg= "white",
    width = 50,
    selectbackground= "gray",
    selectforeground= "white"
)

playlist.pack(pady= 20)

def load_music():
    directory = filedialog.askdirectory()
    if directory:
        os.chdir(directory)
        songs = os.listdir(directory)
        playlist.delete(0, tk.END)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(tk.END,song)

def play_music():
    song = playlist.get(tk.ACTIVE)
    mixer.music.load(song)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def resume_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()


control_frame = tk.Frame(root, bg= "#1e1e1e")
control_frame.pack()

tk.Button(control_frame, text="Play",
          command= play_music, width=10,
          bg="green").grid(row=0, column=0, padx=5)

tk.Button(control_frame, text="Pause",
          command=pause_music, width= 10,
          bg= "orange").grid(row=0, column=1, padx=5)

tk.Button(control_frame, text="Resume",
          command=resume_music, width= 10,
          bg= "blue").grid(row=0, column=2, padx=5)

tk.Button(control_frame, text="Stop",
          command=stop_music, width= 10,
          bg= "red").grid(row=0, column=3, padx=5)


control_frame2 = tk.Frame(root, bg="#1e1e1e")
control_frame2.pack(anchor= "center", pady=20)

tk.Button(control_frame2, text="Load Music Folder",
          command=load_music, width= 20,
          bg= "#444").grid(row=0, column=0, padx=5)

root.mainloop()