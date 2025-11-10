import tkinter as tk
from tkinter import ttk  # For a modern look
from tkinter import messagebox

# --- Functions ---

def register_user():
    """Handles the sign-up logic."""
    
    # 1. Get data from Entry widgets
    name = name_entry.get()
    username = user_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    confirm_password = confirm_entry.get()
    
    # --- 2. Simple Validation ---
    
    # Check if any field is empty
    if not all([name, username, email, password, confirm_password]):
        messagebox.showerror("Error", "All fields are required!")
        return
        
    # Check if passwords match
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        # Clear the password fields
        pass_entry.delete(0, tk.END)
        confirm_entry.delete(0, tk.END)
        pass_entry.focus_set()
        return
        
    # --- 3. Success (Placeholder) ---
    # In a real app, you would save this data to a database.
    
    success_message = (
        f"**Account Created Successfully!**\n\n"
        f"**Name:** {name}\n"
        f"**Username:** {username}\n"
        f"**Email:** {email}"
    )
    messagebox.showinfo("Registration Successful", success_message)
    
    # Clear the form after success
    clear_form()

def clear_form():
    """Clears all entry fields."""
    name_entry.delete(0, tk.END)
    user_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)
    confirm_entry.delete(0, tk.END)
    name_entry.focus_set() # Set focus to the first field

def go_to_login():
    """Placeholder function to simulate navigating to a login window."""
    messagebox.showinfo("Navigate", "Navigating to Login Window...")
    # In a real app, you might destroy this frame
    # and create the login frame.
    
# --- Main Application Window ---
root = tk.Tk()
root.title("Create New Account")
root.geometry("450x550")
root.resizable(False, False)

# --- Use a Themed Frame for better styling ---
# We use .grid() inside this frame
frame = ttk.Frame(root, padding="30 30 30 30")
frame.pack(expand=True)

# --- Form Title ---
title_label = ttk.Label(frame, text="Sign Up", 
                        font=("Arial", 24, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# --- Form Fields ---

# 1. Full Name
name_label = ttk.Label(frame, text="Full Name:")
name_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

name_entry = ttk.Entry(frame, width=30, font=("Arial", 11))
name_entry.grid(row=1, column=1, padx=10, pady=5)

# 2. Username
user_label = ttk.Label(frame, text="Username:")
user_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

user_entry = ttk.Entry(frame, width=30, font=("Arial", 11))
user_entry.grid(row=2, column=1, padx=10, pady=5)

# 3. Email
email_label = ttk.Label(frame, text="Email:")
email_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

email_entry = ttk.Entry(frame, width=30, font=("Arial", 11))
email_entry.grid(row=3, column=1, padx=10, pady=5)

# 4. Password
pass_label = ttk.Label(frame, text="Password:")
pass_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)

pass_entry = ttk.Entry(frame, width=30, show="*", font=("Arial", 11))
pass_entry.grid(row=4, column=1, padx=10, pady=5)

# 5. Confirm Password
confirm_label = ttk.Label(frame, text="Confirm Password:")
confirm_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)

confirm_entry = ttk.Entry(frame, width=30, show="*", font=("Arial", 11))
confirm_entry.grid(row=5, column=1, padx=10, pady=5)


# --- 6. Sign-Up Button ---
# We use 'ipadx' and 'ipady' (internal padding) to make the button bigger
signup_button = ttk.Button(frame, text="Create Account", command=register_user)
signup_button.grid(row=6, column=0, columnspan=2, pady=30, ipadx=10, ipady=5)


# --- 7. "Already have an account?" ---
# A simple label and a button to simulate navigation
login_label = ttk.Label(frame, text="Already have an account?")
login_label.grid(row=7, column=0, columnspan=2, pady=(15, 0))

login_button = ttk.Button(frame, text="Login Now", command=go_to_login)
login_button.grid(row=8, column=0, columnspan=2, pady=(5, 10))

# --- Run the Application ---
root.mainloop()