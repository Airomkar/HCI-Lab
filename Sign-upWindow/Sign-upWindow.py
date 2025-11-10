import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# --- Functions ---

def register_user():
    """Handles user registration validation and display."""
    name = name_entry.get()
    username = user_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    confirm_password = confirm_entry.get()
    gender = gender_var.get()
    terms = terms_var.get()

    # --- Validation ---
    if not all([name, username, email, password, confirm_password, gender]):
        messagebox.showerror("Error", "All fields are required!")
        return
    
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        pass_entry.delete(0, tk.END)
        confirm_entry.delete(0, tk.END)
        pass_entry.focus_set()
        return

    if terms == 0:
        messagebox.showerror("Error", "You must accept the Terms & Conditions.")
        return

    # --- Success Message ---
    messagebox.showinfo(
        "Registration Successful",
        f"Welcome, {name}!\nYour account has been created successfully."
    )
    clear_form()

def clear_form():
    """Clears all input fields."""
    name_entry.delete(0, tk.END)
    user_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)
    confirm_entry.delete(0, tk.END)
    gender_var.set("")
    terms_var.set(0)
    name_entry.focus_set()

def exit_app():
    """Exit confirmation."""
    if messagebox.askyesno("Exit", "Do you want to close the Sign-Up Window?"):
        root.destroy()


# --- Main Window Setup ---

root = tk.Tk()
root.title("Sign-Up Window")
root.geometry("500x600")
root.resizable(False, False)

frame = ttk.Frame(root, padding="30 30 30 30")
frame.pack(expand=True)

# --- Title ---
title_label = ttk.Label(frame, text="Create New Account", font=("Arial", 22, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=15)

# --- Full Name ---
name_label = ttk.Label(frame, text="Full Name:")
name_label.grid(row=1, column=0, sticky="w", padx=10, pady=8)
name_entry = ttk.Entry(frame, width=30)
name_entry.grid(row=1, column=1, pady=8)

# --- Username ---
user_label = ttk.Label(frame, text="Username:")
user_label.grid(row=2, column=0, sticky="w", padx=10, pady=8)
user_entry = ttk.Entry(frame, width=30)
user_entry.grid(row=2, column=1, pady=8)

# --- Email ---
email_label = ttk.Label(frame, text="Email:")
email_label.grid(row=3, column=0, sticky="w", padx=10, pady=8)
email_entry = ttk.Entry(frame, width=30)
email_entry.grid(row=3, column=1, pady=8)

# --- Password ---
pass_label = ttk.Label(frame, text="Password:")
pass_label.grid(row=4, column=0, sticky="w", padx=10, pady=8)
pass_entry = ttk.Entry(frame, width=30, show="*")
pass_entry.grid(row=4, column=1, pady=8)

# --- Confirm Password ---
confirm_label = ttk.Label(frame, text="Confirm Password:")
confirm_label.grid(row=5, column=0, sticky="w", padx=10, pady=8)
confirm_entry = ttk.Entry(frame, width=30, show="*")
confirm_entry.grid(row=5, column=1, pady=8)

# --- Gender (Radiobuttons) ---
gender_label = ttk.Label(frame, text="Gender:")
gender_label.grid(row=6, column=0, sticky="w", padx=10, pady=8)
gender_var = tk.StringVar()
ttk.Radiobutton(frame, text="Male", value="Male", variable=gender_var).grid(row=6, column=1, sticky="w", padx=10)
ttk.Radiobutton(frame, text="Female", value="Female", variable=gender_var).grid(row=6, column=1, sticky="w", padx=80)
ttk.Radiobutton(frame, text="Other", value="Other", variable=gender_var).grid(row=6, column=1, sticky="w", padx=160)

# --- Terms & Conditions ---
terms_var = tk.IntVar()
terms_check = ttk.Checkbutton(frame, text="I accept the Terms & Conditions", variable=terms_var)
terms_check.grid(row=7, column=0, columnspan=2, pady=15)

# --- Buttons ---
register_button = ttk.Button(frame, text="Register", command=register_user)
register_button.grid(row=8, column=0, columnspan=2, pady=15, ipadx=10, ipady=5)

clear_button = ttk.Button(frame, text="Clear", command=clear_form)
clear_button.grid(row=9, column=0, columnspan=2, pady=5, ipadx=10, ipady=5)

exit_button = ttk.Button(frame, text="Exit", command=exit_app)
exit_button.grid(row=10, column=0, columnspan=2, pady=5, ipadx=10, ipady=5)

# --- Run Application ---
root.mainloop()
