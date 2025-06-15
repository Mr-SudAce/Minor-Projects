import tkinter as tk
from tkinter import messagebox
import random
from quizQ import quizQ

# ==================== Logic ====================

def display_question():
    global question, Q_index
    q = question[Q_index]
    question_label.config(text=f"Q{Q_index + 1}: {q['question']}")
    for i, option in enumerate(q['options']):
        option_buttons[i].config(text=option, command=lambda i=i: check_answer(i), bg="#333", fg="#fff")

def next_question():
    global Q_index
    Q_index += 1
    if Q_index >= len(question):
        messagebox.showinfo("Game Over", f"You got {score} out of {len(question)}")
        root.quit()
    else:
        feedback_label.config(text="")
        for btn in option_buttons:
            btn.config(state=tk.NORMAL, bg="#333", fg="#fff")
        display_question()
        next_button.config(state=tk.DISABLED)

def check_answer(i):
    global score
    selected = question[Q_index]['options'][i]
    correct = question[Q_index]['answer']
    for btn in option_buttons:
        btn.config(state=tk.DISABLED)
    if selected.lower() == correct.lower():
        feedback_label.config(text="✅ Correct!", fg="#27ae60")
        score += 1
    else:
        feedback_label.config(text=f"❌ Wrong! Correct: {correct}", fg="#e74c3c")
    next_button.config(state=tk.NORMAL)

# ==================== UI Setup ====================

root = tk.Tk()
root.title("🔥 Ultimate Quiz Game")
window_width, window_height = 800, 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="#1e1e1e")

# Fonts
QUESTION_FONT = ("Segoe UI", 18, "bold")
OPTION_FONT = ("Segoe UI", 14)
FEEDBACK_FONT = ("Segoe UI", 16, "italic")

# Shuffle and slice questions
random.shuffle(quizQ)
question = quizQ[:10]
score = 0
Q_index = 0

# Question Label
question_label = tk.Label(root, text="", font=QUESTION_FONT, bg="#1e1e1e", fg="#ffffff", wraplength=700, justify="center")
question_label.pack(pady=30)

# Option Buttons
option_buttons = []
for i in range(4):
    btn = tk.Button(
        root,
        text="Option",
        font=OPTION_FONT,
        bg="#333333",
        fg="#ffffff",
        activebackground="#555",
        activeforeground="#00ffff",
        relief="raised",
        bd=3,
        width=40,
        pady=10
    )
    btn.pack(pady=5)
    option_buttons.append(btn)

# Feedback Label
feedback_label = tk.Label(root, text="", font=FEEDBACK_FONT, bg="#1e1e1e")
feedback_label.pack(pady=15)

# Next Button
next_button = tk.Button(
    root,
    text="Next Question ▶️",
    font=("Segoe UI", 12, "bold"),
    bg="#3498db",
    fg="#fff",
    activebackground="#2980b9",
    activeforeground="#fff",
    relief="ridge",
    bd=4,
    command=next_question
)
next_button.pack(pady=10)
next_button.config(state=tk.DISABLED)

# Start the first question
display_question()

root.mainloop()
