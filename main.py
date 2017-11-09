# Binary Puzzle by MohamadKh75
# 2017-11-09
# ********************

from tkinter import messagebox
import tkinter as tk
from tkinter import font as tkfont
from pathlib import Path


# Defining Paths
img_path = Path("pix\calculator.png").resolve()
icon_path = Path("pix\icon.ico").resolve()

# Defining Variables


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, NewGame, HighScores, About):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Binary Puzzle", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="New Game",
                            command=lambda: controller.show_frame("NewGame"))
        button2 = tk.Button(self, text="High Scores",
                            command=lambda: controller.show_frame("HighScores"))
        button3 = tk.Button(self, text="About",
                            command=lambda: controller.show_frame("About"))
        button4 = tk.Button(self, text="Exit",
                            command=lambda: app.destroy())

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()


class NewGame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Let's Play!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()



