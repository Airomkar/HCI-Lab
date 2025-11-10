import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# --- Quiz Data ---
questions = [
    {
        "question": "1. Which programming language is used to create this GUI?",
        "options": ["C++", "Java", "Python", "HTML"],
        "answer": "Python"
    },
    {
        "question": "2. Which library in Python is used for GUI applications?",
        "options": ["NumPy", "Pandas", "Tkinter", "Matplotlib"],
        "answer": "Tkinter"
    },
    {
        "question": "3. Which method is used to start a Tkinter GUI event loop?",
        "options": ["start()", "run()", "mainloop()", "execute()"],
        "answer": "mainloop()"
    },
    {
        "question": "4. What widget is used to display text in Tkinter?",
        "options": ["Label", "Entry", "Button", "Checkbutton"],
        "answer": "Label"
    },
    {
        "question": "5. What is the file extension for Python files?",
        "options": [".txt", ".java", ".py", ".html"],
        "answer": ".py"
    }
]

# --- Functions ---

def submit_quiz():
    """Calculate score and show result."""
    score = 0
    for i, q in enumerate(questions):
        selected_option = answer_vars[i].get()
        if selected_option == q["answer"]:
            score += 1

    messagebox.showinfo("Quiz Result", f"Your Score: {score} / {len(questions)}")
    reset_quiz()

def reset_quiz():
    """Clears all selections and text area."""
    for var in answer_vars:
        var.set(None)
    comment_text.delete("1.0", tk.END)

def exit_quiz():
    """Exit confirmation."""
    if messagebox.askyesno("Exit", "Do you want to close the Quiz?"):
        root.destroy()

# --- Main Window Setup ---

root = tk.Tk()
root.title("Online Quiz Application")
root.geometry("600x700")
root.resizable(False, False)

frame = ttk.Frame(root, padding="25 25 25 25")
frame.pack(expand=True)

# --- Title ---
title_label = ttk.Label(frame, text="🧠 Online Quiz", font=("Arial", 24, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=15)

# --- Display Questions ---
answer_vars = []

for i, q in enumerate(questions):
    question_label = ttk.Label(frame, text=q["question"], font=("Arial", 12, "bold"))
    question_label.grid(row=(i*5)+1, column=0, sticky="w", columnspan=2, pady=5)

    answer_var = tk.StringVar(value=None)
    answer_vars.append(answer_var)

    for j, opt in enumerate(q["options"]):
        ttk.Radiobutton(
            frame, text=opt, value=opt, variable=answer_var
        ).grid(row=(i*5)+2+j, column=0, sticky="w", padx=30)

# --- Comments Section ---
comment_label = ttk.Label(frame, text="💬 Any Comments or Suggestions:")
comment_label.grid(row=30, column=0, sticky="w", pady=10)

comment_text = tk.Text(frame, width=60, height=5, font=("Arial", 10))
comment_text.grid(row=31, column=0, columnspan=2, pady=5)

# --- Buttons ---
submit_button = ttk.Button(frame, text="Submit", command=submit_quiz)
submit_button.grid(row=32, column=0, columnspan=2, pady=15, ipadx=10, ipady=5)

clear_button = ttk.Button(frame, text="Clear", command=reset_quiz)
clear_button.grid(row=33, column=0, columnspan=2, pady=5, ipadx=10, ipady=5)

exit_button = ttk.Button(frame, text="Exit", command=exit_quiz)
exit_button.grid(row=34, column=0, columnspan=2, pady=10, ipadx=10, ipady=5)

# --- Run App ---
root.mainloop()
