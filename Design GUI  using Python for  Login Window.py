import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# --- Functions ---

def login_user():
    """Handles login validation."""
    username = user_entry.get()
    password = pass_entry.get()
    
    # Simple validation
    if not username or not password:
        messagebox.showerror("Error", "Please enter both Username and Password!")
        return
    
    # Example validation (In real case, check database)
    if username == "admin" and password == "12345":
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        clear_form()
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")
        pass_entry.delete(0, tk.END)
        pass_entry.focus_set()

def clear_form():
    """Clears all entry fields."""
    user_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)
    user_entry.focus_set()

def open_signup():
    """Simulate going to sign-up window."""
    messagebox.showinfo("Navigation", "Redirecting to Sign-Up Window...")

# --- Main Application Window ---

root = tk.Tk()
root.title("Login Window")
root.geometry("400x350")
root.resizable(False, False)

# --- Use Themed Frame ---
frame = ttk.Frame(root, padding="30 30 30 30")
frame.pack(expand=True)

# --- Title ---
title_label = ttk.Label(frame, text="User Login", font=("Arial", 22, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=15)

# --- Username ---
user_label = ttk.Label(frame, text="Username:")
user_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

user_entry = ttk.Entry(frame, width=30, font=("Arial", 11))
user_entry.grid(row=1, column=1, padx=10, pady=10)

# --- Password ---
pass_label = ttk.Label(frame, text="Password:")
pass_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)

pass_entry = ttk.Entry(frame, width=30, show="*", font=("Arial", 11))
pass_entry.grid(row=2, column=1, padx=10, pady=10)

# --- Buttons ---
login_button = ttk.Button(frame, text="Login", command=login_user)
login_button.grid(row=3, column=0, columnspan=2, pady=20, ipadx=10, ipady=5)

clear_button = ttk.Button(frame, text="Clear", command=clear_form)
clear_button.grid(row=4, column=0, columnspan=2, pady=5, ipadx=10, ipady=3)

# --- Sign-up Navigation ---
signup_label = ttk.Label(frame, text="Don't have an account?")
signup_label.grid(row=5, column=0, columnspan=2, pady=(20, 5))

signup_button = ttk.Button(frame, text="Create Account", command=open_signup)
signup_button.grid(row=6, column=0, columnspan=2, pady=(5, 10))

# --- Run the Application ---
root.mainloop()
