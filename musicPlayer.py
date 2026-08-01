import tkinter as tk
from tkinter import ttk
import threading
import time
import vlc
import yt_dlp


class MusicPlayer:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jarvis Music Player")
        self.root.geometry("500x230")
        self.root.resizable(False, False)

        self.player = None
        self.length = 0

        self.song_label = tk.Label(
            self.root,
            text="No song playing",
            font=("Arial", 14)
        )
        self.song_label.pack(pady=10)

        self.slider = ttk.Scale(
            self.root,
            from_=0,
            to=100,
            orient="horizontal",
            length=420
        )
        self.slider.pack()

        self.time_label = tk.Label(
            self.root,
            text="00:00 / 00:00"
        )
        self.time_label.pack()

        self.volume = ttk.Scale(
            self.root,
            from_=0,
            to=200,
            orient="horizontal",
            length=250,
            command=self.change_volume
        )
        self.volume.set(120)
        self.volume.pack(pady=10)

        buttons = tk.Frame(self.root)
        buttons.pack()

        tk.Button(
            buttons,
            text="⏸ Pause",
            command=self.pause
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            buttons,
            text="▶ Resume",
            command=self.resume
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            buttons,
            text="⏹ Stop",
            command=self.stop
        ).grid(row=0, column=2, padx=5)

    def play(self, url, name):

        self.song_label.config(text=name)

        ydl_opts = {
            "format": "bestaudio/best",
            "quiet": True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            stream = info["url"]

        self.player = vlc.MediaPlayer(stream)
        self.player.audio_set_volume(120)
        self.player.play()

        self.update_slider()

    def update_slider(self):

        while True:

            if self.player is None:
                break

            length = self.player.get_length()

            current = self.player.get_time()

            if length > 0:

                self.slider.configure(to=length)

                self.slider.set(current)

                self.time_label.config(
                    text=f"{current//60000:02}:{(current//1000)%60:02} / {length//60000:02}:{(length//1000)%60:02}"
                )

            self.root.after(500, self.update_slider)
            return

    def pause(self):
        if self.player:
            self.player.pause()

    def resume(self):
        if self.player:
            self.player.play()

    def stop(self):
        if self.player:
            self.player.stop()

    def change_volume(self, value):
        if self.player:
            self.player.audio_set_volume(int(float(value)))

    def start(self):
        self.root.mainloop()