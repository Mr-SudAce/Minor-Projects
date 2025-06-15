import tkinter as tk
from quizQ import quizQ
import random

###################################################### logic ######################################################

# Display the question
def display_question():
    global question, Q_index
    q = question[Q_index]
    question_lable.config(text=f"Q{Q_index + 1}: {q['question']} ")
    for i, option in enumerate(q['options']):
        option_button[i].config(text=option, command=lambda i=i: check_answer(i))


# Next Question display
def next_question():
    global Q_index
    Q_index += 1
    if Q_index >= len(question):
        tk.messagebox.showinfo("Game Over" , f"You got {score} out of {len(question)}")
        root.quit()
    else:
        feedback_label.config(text="")
        for btn in option_button:
            btn.config(state=tk.NORMAL)
        display_question()
        next_button.config(state=tk.DISABLED)


# Checking Answer
def check_answer(i):
    global score
    selected = question[Q_index]['options'][i]
    correct = question[Q_index]['answer']
    for btn in option_button:
        btn.config(state = tk.DISABLED)
    if selected.lower() == correct.lower():
        feedback_label.config(text="Correct", fg="green")
        score += 1
    else:
        feedback_label.config(text=f'Wrong!! | Correct : {correct}', fg="red")    
    next_button.config(state =tk.NORMAL)

###################################################### logic ######################################################


# Created main Window
root = tk.Tk()
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
window_width = 800
window_height = 400

# Calculate x and y coordinates for the Tk root window
x = (screenwidth // 2) - (window_width // 2)
y = (screenheight // 2) - (window_height // 2)

root.title("Quiz Game")
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="#4C4C4C")


# shuffle the question and pick 10 Question
random.shuffle(quizQ)
question = quizQ[:10]

score = 0   # initial score
Q_index = 0 # Question index


# Question Label
question_lable = tk.Label(root, text="", font=("Arial", 18), fg="#ffffff", bg="#000000", padx=100 )
question_lable.pack(pady=20)

# Option button
option_button = []
for i in range(4):
    btn  = tk.Button(root, text="")
    btn.pack(padx=20)
    option_button.append(btn)



    
# Next Question Button
next_button = tk.Button(root, text="Next", command=next_question)
next_button.pack(pady=10)

# feedback lable
feedback_label = tk.Label(text="", font=("Arial", 18)  )
feedback_label.pack(pady=20)

display_question()

root.mainloop()