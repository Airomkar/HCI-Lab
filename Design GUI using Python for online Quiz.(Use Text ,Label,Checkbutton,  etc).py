import tkinter as tk
from tkinter import ttk  # Use themed widgets for a better look
from tkinter import messagebox

# --- Define Your Quiz Data ---
# A list of dictionaries, where each dictionary is a question.
quiz_data = [
    {
        "question": "What is the output of 2 + 2 * 2?",
        "options": ["4", "6", "8", "2"],
        "answer": "6"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "Which of these is NOT a core data type in Python?",
        "options": ["List", "Dictionary", "Tuple", "Class"],
        "answer": "Class"
    },
    {
        "question": "What does 'GUI' stand for?",
        "options": ["Graphical User Interface", "General User Input", "Gaming User Interface", "Good User Interaction"],
        "answer": "Graphical User Interface"
    }
]

# --- Main Application Class ---
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python GUI Quiz")
        self.root.geometry("600x450")
        self.root.resizable(False, False)
        
        # --- Style Configuration (Optional) ---
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
        style.configure("Header.TLabel", font=("Arial", 18, "bold"))
        style.configure("TRadiobutton", background="#f0f0f0", font=("Arial", 11))
        style.configure("TButton", font=("Arial", 12, "bold"))

        # --- Quiz State Variables ---
        self.quiz_data = quiz_data
        self.current_question = 0
        self.score = 0
        
        # Variable to store the selected answer (for the Radiobuttons)
        self.selected_option = tk.StringVar()
        
        # --- Setup the UI ---
        self.create_widgets()
        
        # Load the first question
        self.load_question()

    def create_widgets(self):
        """Creates and layouts all the GUI components."""
        
        # Main frame to hold all widgets
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill="both", expand=True)

        # --- Question Label ---
        # This Label will display the question text.
        self.question_label = ttk.Label(self.main_frame, text="Question text goes here",
                                        style="Header.TLabel", wraplength=550, justify="center")
        self.question_label.pack(pady=20)

        # --- Options Frame ---
        # A frame to hold the radio buttons
        self.options_frame = ttk.Frame(self.main_frame)
        self.options_frame.pack(pady=10)

        # We will create 4 Radiobuttons
        self.radio_buttons = []
        for i in range(4):
            # The 'text' and 'value' will be set in load_question()
            rb = ttk.Radiobutton(self.options_frame, text=f"Option {i+1}", 
                                 variable=self.selected_option, value=f"Option {i+1}")
            rb.pack(anchor="w", pady=5, padx=20)
            self.radio_buttons.append(rb)
            
        # --- Navigation/Submit Button ---
        self.nav_button = ttk.Button(self.main_frame, text="Next", command=self.next_question)
        self.nav_button.pack(pady=30, ipadx=20, ipady=5)

        # --- Score Label ---
        # This Label will display the current score
        self.score_label = ttk.Label(self.root, text=f"Score: 0 / {len(self.quiz_data)}", 
                                     font=("Arial", 10), padding="10")
        self.score_label.pack(anchor="e") # 'e' = east (right-aligned)

    def load_question(self):
        """Loads the current question and its options into the UI."""
        
        # Check if quiz is over
        if self.current_question >= len(self.quiz_data):
            self.show_results()
            return

        # Get the current question's data
        q_data = self.quiz_data[self.current_question]
        
        # Update the question label
        self.question_label.config(text=q_data["question"])
        
        # Get the options
        options = q_data["options"]
        
        # Update the Radiobuttons
        for i in range(4):
            self.radio_buttons[i].config(text=options[i], value=options[i])
            
        # Deselect any previous answer
        self.selected_option.set("")
        
        # Change button text to "Submit" for the last question
        if self.current_question == len(self.quiz_data) - 1:
            self.nav_button.config(text="Submit")
        else:
            self.nav_button.config(text="Next")

    def next_question(self):
        """Checks the answer, updates the score, and moves to the next question."""
        
        # 1. Get selected answer
        selected = self.selected_option.get()
        
        # Check if an option was selected
        if not selected:
            messagebox.showwarning("No Answer", "Please select an answer before proceeding.")
            return
            
        # 2. Check if it's correct
        correct_answer = self.quiz_data[self.current_question]["answer"]
        if selected == correct_answer:
            self.score += 1
            
        # 3. Update score label
        self.score_label.config(text=f"Score: {self.score} / {len(self.quiz_data)}")
        
        # 4. Move to the next question
        self.current_question += 1
        
        # 5. Load the next question (or show results)
        self.load_question()

    def show_results(self):
        """Displays the final score in a message box and disables the app."""
        # Hide the main frame
        self.main_frame.pack_forget()
        self.score_label.pack_forget()
        
        # Show final score message
        result_message = f"Quiz Completed!\n\nYour final score is: {self.score} / {len(self.quiz_data)}"
        
        # Display the result in a new frame
        result_frame = ttk.Frame(self.root, padding="20")
        result_frame.pack(fill="both", expand=True)
        
        ttk.Label(result_frame, text="Quiz Completed!", style="Header.TLabel").pack(pady=20)
        ttk.Label(result_frame, text=f"Your final score is:", font=("Arial", 16)).pack(pady=10)
        ttk.Label(result_frame, text=f"{self.score} / {len(self.quiz_data)}", font=("Arial", 24, "bold")).pack(pady=30)
        
        # Add a restart button
        restart_button = ttk.Button(result_frame, text="Restart Quiz", command=self.restart_quiz)
        restart_button.pack(pady=20)
        
    def restart_quiz(self):
        """Resets the quiz to the beginning."""
        self.score = 0
        self.current_question = 0
        
        # Remove the result frame (if it exists)
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Frame):
                widget.destroy()
                
        # Re-create the main UI
        self.create_widgets()
        self.load_question()


# --- Run the Application ---
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
    