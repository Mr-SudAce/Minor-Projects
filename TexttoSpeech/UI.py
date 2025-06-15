import tkinter as tk  # Import the tkinter library for GUI
from texttospeech import *


def on_submit():
    userInput = entry.get()
    entrytospeak(userInput)


window = tk.Tk()  # Create the main window


screen_width = window.winfo_screenwidth()  # Get the width of the screen
screen_height = window.winfo_screenheight()  # Get the height of the screen


# Set the window size to 700x500 and position it near the center of the screen
window.geometry(f"700x200+{(screen_width // 2) - 400}+{(screen_height // 2) - 300}")


window.configure(bg="#6f6f6f")                                # Set the window background color to red


label = tk.Label(text="Enter to Speak", fg="#000000")         # Label
entry = tk.Entry(window, width=30)                              # Input Box
button = tk.Button(text="Submit", command=on_submit)            # Button


# Using Grid for all widgets
label.grid(row=0, column=0, padx=20, pady=(30, 10), sticky="ew")
entry.grid(row=0, column=1, padx=20, pady=(30, 10), sticky="ew")
button.grid(row=0, column=2, padx=20, pady=(30, 10), sticky="ew")


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
window.columnconfigure(2, weight=1)


window.mainloop()  # Start the GUI event
