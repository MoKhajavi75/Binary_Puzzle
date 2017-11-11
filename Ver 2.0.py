# Binary Puzzle by MohamadKh75
# 2017-11-09
# ********************

from tkinter import messagebox
import tkinter as tk
from tkinter import font as tkfont
from pathlib import Path
import webbrowser
import random
import ast

# Defining Paths
img_path = Path("pix\calculator.png").resolve()
icon_path = Path("pix\icon.ico").resolve()


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

        button1 = tk.Button(self, text="New Game", bg="DarkGoldenrod1", font="TimesNewRoman 15",
                            command=lambda: controller.show_frame("NewGame"))
        button2 = tk.Button(self, text="High Scores", bg="DarkGoldenrod2", font="TimesNewRoman 15",
                            command=lambda: controller.show_frame("HighScores"))
        button3 = tk.Button(self, text="About", bg="DarkGoldenrod3", font="TimesNewRoman 15",
                            command=lambda: controller.show_frame("About"))
        button4 = tk.Button(self, text="Exit", bg="DarkGoldenrod4", font="TimesNewRoman 15",
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

        # User's Entries
        rows = 4
        columns = 4
        entries = []
        for i in range(rows):  # Rows
            for j in range(columns):  # Columns
                e = tk.Entry(table, text="", width=10, justify='center')
                e.grid(row=i, column=j, padx=5, pady=5)
                e.insert(0, random.randint(0, 1))
                e.grid_rowconfigure(0, weight=1)
                e.grid_columnconfigure(0, weight=1)
                entries.append(e)

        # Save real answers
        real_ans = ""
        for entry in entries:
            real_ans += str(entry.get())

        # Function: Binary 2 Decimal
        def toDec(number):
            return int(number, 2)

        # Check Button Function
        def checkIt():
            user_ans = ""
            for entry in entries:
                user_ans += str(entry.get())

            # If all Entries are filled
            if len(user_ans) < 16:
                messagebox.showerror("Error", "Fill All Entries!")

            elif len(user_ans) > 16:
                messagebox.showerror("Error", "Just Use 0 or 1!")

            else:
                # If all numbers are 0 OR 1
                for char in user_ans:
                    if char == '0':
                        continue
                    elif char == '1':
                        continue
                    else:
                        messagebox.showerror("Error", "Just Use 0 or 1!")

                # If user is correct :D
                if user_ans == real_ans:
                    messagebox.showinfo("Result", "You Win!")
                    controller.show_frame("HighScores")

                elif messagebox.askyesno("Result", "Try Again?"):
                    pass

                else:
                    for entry in entries:
                        entry.delete(0, 'end')

                    controller.show_frame("StartPage")

        # Column Answers - Row Answers
        c_ans1 = tk.Entry(table, text="", width=10, justify='center')
        c_ans1.grid(row=0, column=4, padx=5, pady=5)
        ans_to_send = real_ans[:4]
        c_ans1.insert(0, toDec(ans_to_send))

        c_ans2 = tk.Entry(table, text="", width=10, justify='center')
        c_ans2.grid(row=1, column=4, padx=5, pady=5)
        ans_to_send = real_ans[4:8]
        c_ans2.insert(0, toDec(ans_to_send))

        c_ans3 = tk.Entry(table, text="", width=10, justify='center')
        c_ans3.grid(row=2, column=4, padx=5, pady=5)
        ans_to_send = real_ans[8:12]
        c_ans3.insert(0, toDec(ans_to_send))

        c_ans4 = tk.Entry(table, text="", width=10, justify='center')
        c_ans4.grid(row=3, column=4, padx=5, pady=5)
        ans_to_send = real_ans[12:16]
        c_ans4.insert(0, toDec(ans_to_send))

        r_ans1 = tk.Entry(table, text="", width=10, justify='center')
        r_ans1.grid(row=4, column=0, padx=5, pady=5)
        ans_to_send = real_ans[0] + real_ans[4] + real_ans[8] + real_ans[12]
        r_ans1.insert(0, toDec(ans_to_send))

        r_ans2 = tk.Entry(table, text="", width=10, justify='center')
        r_ans2.grid(row=4, column=1, padx=5, pady=5)
        ans_to_send = real_ans[1] + real_ans[5] + real_ans[9] + real_ans[13]
        r_ans2.insert(0, toDec(ans_to_send))

        r_ans3 = tk.Entry(table, text="", width=10, justify='center')
        r_ans3.grid(row=4, column=2, padx=5, pady=5)
        ans_to_send = real_ans[2] + real_ans[6] + real_ans[10] + real_ans[14]
        r_ans3.insert(0, toDec(ans_to_send))

        r_ans4 = tk.Entry(table, text="", width=10, justify='center')
        r_ans4.grid(row=4, column=3, padx=5, pady=5)
        ans_to_send = real_ans[3] + real_ans[7] + real_ans[11] + real_ans[15]
        r_ans4.insert(0, toDec(ans_to_send))

        # Let's Clear the real answers!
        for entry in entries:
            entry.delete(0, 'end')

        # Just a horizontal line!
        hr = tk.Frame(self, height=5, width=600, bg="Black")
        hr.pack(fill="x", pady=10)

        # Check Button
        check_button = tk.Button(self, text="Check!", bg="LightSkyBlue1", font="TimesNewRoman 20",
                           command=checkIt)
        check_button.pack(expand=1, fill=tk.BOTH)

        # Just another horizontal line!
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

    # Get screen width and height
    ws = app.winfo_screenwidth()  # width of the screen
    hs = app.winfo_screenheight()  # height of the screen

    # Calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # Set the dimensions of the screen and where it is placed
    app.geometry('%dx%d+%d+%d' % (w, h, x, y))
    app.mainloop()
