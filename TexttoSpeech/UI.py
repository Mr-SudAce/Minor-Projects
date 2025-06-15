import tkinter as tk
from texttospeech import *  # Assuming you have a function called entrytospeak()

def on_submit():
    user_input = entry.get()
    entrytospeak(user_input)

# === Main Window ===
window = tk.Tk()
window.title("🗣️ Speak It Out")
window_width, window_height = 700, 200
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.configure(bg="#1f1f1f")

# === Fonts ===
LABEL_FONT = ("Segoe UI", 14)
ENTRY_FONT = ("Segoe UI", 14)
BUTTON_FONT = ("Segoe UI", 12, "bold")

# === Label ===
label = tk.Label(window, text="🎤 Enter text to speak:", font=LABEL_FONT, fg="#ffffff", bg="#1f1f1f")
label.pack(pady=(30, 10))

# === Entry ===
entry = tk.Entry(window, font=ENTRY_FONT, width=50, bd=2, relief="groove", bg="#f0f0f0", fg="#000")
entry.pack(pady=5, ipady=5)

# === Submit Button ===
def on_hover(e): submit_btn.config(bg="#27ae60", fg="#fff")
def on_leave(e): submit_btn.config(bg="#2ecc71", fg="#fff")

submit_btn = tk.Button(window, text="🔊 Speak", font=BUTTON_FONT, bg="#2ecc71", fg="#fff",
                       activebackground="#1abc9c", activeforeground="#ffffff", command=on_submit,
                       relief="ridge", bd=3, padx=20, pady=5, cursor="hand2")
submit_btn.pack(pady=(20, 10))

submit_btn.bind("<Enter>", on_hover)
submit_btn.bind("<Leave>", on_leave)

# === Mainloop ===
window.mainloop()
