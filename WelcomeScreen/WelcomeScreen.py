import tkinter as tk
from tkinter import ttk  # For a modern look
from tkinter import messagebox

# --- Functions ---

def go_to_login():
    """Placeholder function to simulate navigating to a login window."""
    messagebox.showinfo("Navigate", "Navigating to Login Screen...")
    # In a real app, you would destroy this frame
    # and create the login frame.

def go_to_signup():
    """Placeholder function to simulate navigating to a sign-up window."""
    messagebox.showinfo("Navigate", "Navigating to Sign Up Screen...")
    # In a real app, you would destroy this frame
    # and create the sign-up frame.

# --- Main Application Window ---
root = tk.Tk()
root.title("Welcome to MyApp")
root.geometry("500x350")  # Set a good size
root.resizable(False, False) # Keep the window a fixed size

# --- Main Frame ---
# This frame holds all content and we'll use .pack() 
# with expand=True to center everything.
main_frame = ttk.Frame(root)
main_frame.pack(expand=True, fill="both")

# --- Content Frame ---
# A second frame inside the main one to group the widgets.
# This makes centering them with .pack() very easy.
content_frame = ttk.Frame(main_frame)
content_frame.pack(expand=True)

# --- Widgets ---

# 1. Title Label
title_label = ttk.Label(
    content_frame,
    text="Welcome! 👋",
    font=("Arial", 32, "bold")  # Large, bold font
)
title_label.pack(pady=10)

# 2. Subtitle Label
subtitle_label = ttk.Label(
    content_frame,
    text="We're glad to have you here. Please log in or sign up to get started.",
    font=("Arial", 13),
    wraplength=400,    # Wrap text if it gets too long
    justify="center"   # Center the wrapped text
)
subtitle_label.pack(pady=(5, 30))  # (top, bottom) padding

# 3. Button Frame
# A frame to hold the buttons side-by-side
button_frame = ttk.Frame(content_frame)
button_frame.pack(pady=20)

# 4. Login Button
login_button = ttk.Button(
    button_frame,
    text="Login",
    command=go_to_login
)
# Use ipadx/ipady (internal padding) to make buttons bigger
login_button.pack(side="left", padx=15, ipadx=20, ipady=10)

# 5. Sign Up Button
signup_button = ttk.Button(
    button_frame,
    text="Sign Up",
    command=go_to_signup
)
signup_button.pack(side="left", padx=15, ipadx=20, ipady=10)

# --- Run the Application ---
root.mainloop()
