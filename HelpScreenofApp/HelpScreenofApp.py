import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# --- Functions ---

def contact_support():
    """Simulate contacting customer support."""
    messagebox.showinfo(
        "Contact Support",
        "Thank you for reaching out!\n\nOur support team will contact you within 24 hours."
    )

def close_help():
    """Close the help window."""
    if messagebox.askyesno("Exit", "Do you want to close the Help window?"):
        root.destroy()

# --- Main Window Setup ---

root = tk.Tk()
root.title("Help & Support - Event Manager App")
root.geometry("600x500")
root.resizable(False, False)

# --- Main Frame ---
frame = ttk.Frame(root, padding="25 25 25 25")
frame.pack(expand=True, fill="both")

# --- Title ---
title_label = ttk.Label(
    frame, text="Help & Support", font=("Arial", 22, "bold"), anchor="center"
)
title_label.pack(pady=10)

# --- Short Info ---
info_label = ttk.Label(
    frame,
    text="Welcome to the Help Center of Event Manager App.\nHere you can find answers to common questions or contact support.",
    font=("Arial", 11),
    justify="center",
)
info_label.pack(pady=10)

# --- Text Area with Scrollbar ---
help_text_frame = ttk.Frame(frame)
help_text_frame.pack(pady=10, fill="both", expand=True)

scrollbar = ttk.Scrollbar(help_text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

help_text = tk.Text(help_text_frame, wrap="word", width=70, height=15, font=("Arial", 11))
help_text.pack(side=tk.LEFT, fill="both", expand=True)

scrollbar.config(command=help_text.yview)
help_text.config(yscrollcommand=scrollbar.set)

# --- Add Help Information ---
help_content = """
📘  EVENT MANAGER APP - HELP GUIDE

1️⃣  How to Register:
   - Go to the Register screen.
   - Enter your name, email, and password.
   - Click 'Sign Up' to create your account.

2️⃣  How to Login:
   - On the login screen, enter your registered email and password.
   - Click 'Login' to access your dashboard.

3️⃣  Booking an Event:
   - Choose the type of event (Wedding, Birthday, Corporate).
   - Select a date, location, and budget.
   - Click 'Book Now' to confirm your booking.

4️⃣  Managing Vendors:
   - Navigate to the Vendor section.
   - You can view, compare, or contact vendors for your event.

5️⃣  Payment & Confirmation:
   - Payments are handled directly with vendors.
   - Always confirm your booking via the 'My Events' section.

💡  Tips:
   - Keep your email verified for important notifications.
   - Contact customer support for any booking issues.

📞  Contact Us:
   - Email: support@eventmanager.com
   - Phone: +91 98765 43210
   - Working Hours: 9 AM – 8 PM (Mon–Sat)
"""
help_text.insert(tk.END, help_content)
help_text.config(state="disabled")  # Make the text read-only

# --- Buttons ---
button_frame = ttk.Frame(frame)
button_frame.pack(pady=20)

contact_button = ttk.Button(button_frame, text="Contact Support", command=contact_support)
contact_button.grid(row=0, column=0, padx=10, ipadx=10, ipady=5)

exit_button = ttk.Button(button_frame, text="Close Help", command=close_help)
exit_button.grid(row=0, column=1, padx=10, ipadx=10, ipady=5)

# --- Run Application ---
root.mainloop()
