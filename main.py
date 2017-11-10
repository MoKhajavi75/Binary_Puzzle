# Binary Puzzle by MohamadKh75
# 2017-11-09
# ********************

from tkinter import messagebox
import tkinter as tk
from tkinter import font as tkfont
from pathlib import Path
import webbrowser
import random

# Defining Paths
img_path = Path("pix\calculator.png").resolve()
icon_path = Path("pix\icon.ico").resolve()

# Defining Variables
Numbers = [random.randint(0, 1) for _ in range(16)]
for x in Numbers:
    print(Numbers[x])


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
        label = tk.Label(self, text="Binary Puzzle", bg="Black", fg="Yellow", font=controller.title_font)
        label.pack(side="top", fill="x", pady=30, ipady=5)

        button1 = tk.Button(self, text="New Game", bg="Gray", font="TimesNewRoman 15",
                            command=lambda: controller.show_frame("NewGame"))
        button2 = tk.Button(self, text="High Scores", bg="Gray", font="TimesNewRoman 15",
                            command=lambda: controller.show_frame("HighScores"))
        button3 = tk.Button(self, text="About", bg="Gray", font="TimesNewRoman 15",
                            command=lambda: controller.show_frame("About"))
        button4 = tk.Button(self, text="Exit", bg="Gray", font="TimesNewRoman 15",
                            command=lambda: app.destroy())

        button1.pack(fill="x", pady=5, ipady=15)
        button2.pack(fill="x", pady=5, ipady=15)
        button3.pack(fill="x", pady=5, ipady=15)
        button4.pack(fill="x", pady=5, ipady=15)


class NewGame(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Let's Play!", bg="Black", fg="Yellow", font=controller.title_font)
        label.pack(side="top", fill="x", ipady=20)

        # Just a horizontal line!
        hr = tk.Frame(self, height=5, width=600, bg="Black")
        hr.pack(fill="x", pady=10)

        # Table's Frame!
        table = tk.Frame(self, height=200, width=100, bg="White")
        table.pack(fill="x", padx=115, pady=10)

        rows = 5
        columns = 5
        for i in range(rows):  # Rows
            for j in range(columns):  # Columns
                b = tk.Entry(table, text="", width=10)
                b.grid(row=i, column=j, padx=5, pady=5, sticky='SW')
                b.grid_rowconfigure(0, weight=1)
                b.grid_columnconfigure(0, weight=1)

                if i != 4:
                    if j != 4:
                        b.insert(0, random.randint(0, 1))

        # Just a horizontal line!
        hr = tk.Frame(self, height=5, width=600, bg="Black")
        hr.pack(fill="x", pady=10)

        # Return Button
        button = tk.Button(self, text="Return To Main Menu", bg="Gray", font="TimesNewRoman 20",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(expand=1, fill=tk.BOTH)


class HighScores(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="High Scores", bg="Black", fg="Yellow", font=controller.title_font)
        label.pack(side="top", fill="x", ipady=20)

        # Just a horizontal line!
        hr = tk.Frame(self, height=5, width=600, bg="Black")
        hr.pack(fill="x", pady=10)

        # Info
        label2 = tk.Label(self, text="...", bg="White",
                          font="TimesNewRoman 13 bold")
        label2.pack(side="top", fill="x", pady=10)

        # Just a horizontal line!
        hr = tk.Frame(self, height=5, width=600, bg="Black")
        hr.pack(fill="x", pady=10)

        # Return Button
        button = tk.Button(self, text="Return To Main Menu", bg="Gray", font="TimesNewRoman 20",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(expand=1, fill=tk.BOTH)


class About(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="About Us", bg="Black", fg="Yellow", font=controller.title_font)
        label.pack(side="top", fill="x", ipady=20)

        # Just a horizontal line!
        hr = tk.Frame(self, height=5, width=600, bg="Black")
        hr.pack(fill="x", pady=10)

        # Info
        def callback(event):
            webbrowser.open_new(r"https://github.com/MohamadKh75/Binary_Puzzle")

        label2 = tk.Label(self, text="\nMohamadKh75\n", bg="White",
                          font="TimesNewRoman 13 bold")
        label2.pack(side="top", fill="x", pady=10)
        link = tk.Label(self, text="\nMy Github page!\n", bg="White", fg="blue",
                        font="TimesNewRoman 13 italic", cursor="hand2")
        link.pack(side="top", fill="x")
        link.bind("<Button-1>", callback)

        # Just a horizontal line!
        hr = tk.Frame(self, height=5, width=600, bg="Black")
        hr.pack(fill="x", pady=10)

        # Return Button
        button = tk.Button(self, text="Return To Main Menu", bg="Gray", font="TimesNewRoman 20",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(expand=1, fill=tk.BOTH)


if __name__ == "__main__":
    app = SampleApp()
    app.title("Binary Puzzle")
    app.iconbitmap(icon_path)

    w = 600  # width for the Tk root
    h = 450  # height for the Tk root

    # get screen width and height
    ws = app.winfo_screenwidth()  # width of the screen
    hs = app.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    app.geometry('%dx%d+%d+%d' % (w, h, x, y))
    app.mainloop()
