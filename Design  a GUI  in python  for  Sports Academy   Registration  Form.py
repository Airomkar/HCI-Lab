import tkinter as tk
from tkinter import ttk  # For a slightly better look
from tkinter import messagebox

# --- Functions ---

def submit_form():
    """Gathers data and shows a message."""
    
    # 1. Get data
    name = name_entry.get()
    phone = phone_entry.get()
    
    # 2. Get from Listbox
    try:
        sport_index = sport_listbox.curselection()[0]
        sport = sport_listbox.get(sport_index)
    except IndexError:
        sport = "Not Selected"
        
    # 3. Get from Checkbutton
    agreed = terms_var.get()
    
    # --- Validation ---
    if not name or sport == "Not Selected":
        messagebox.showerror("Error", "Please enter your Name and select a Sport.")
        return
        
    if not agreed:
        messagebox.showerror("Error", "You must agree to the terms.")
        return
        
    # --- Show Success Message ---
    messagebox.showinfo("Success", f"Registered {name} for {sport}!")
    clear_form()

def clear_form():
    """Clears all fields."""
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    sport_listbox.selection_clear(0, tk.END)
    terms_var.set(False)
    name_entry.focus_set()

# --- Main Application Window ---
root = tk.Tk()
root.title("Simple Sports Registration")
root.geometry("400x350")
root.resizable(False, False)

# Use a 'main_frame' with padding
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

# --- 1. Title ---
title_label = ttk.Label(main_frame, text="Sports Registration", 
                        font=("Arial", 18, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# --- 2. Name ---
name_label = ttk.Label(main_frame, text="Full Name:")
name_label.grid(row=1, column=0, padx=5, pady=10, sticky="w")

name_entry = ttk.Entry(main_frame, width=30)
name_entry.grid(row=1, column=1, padx=5, pady=10)

# --- 3. Phone ---
phone_label = ttk.Label(main_frame, text="Phone Number:")
phone_label.grid(row=2, column=0, padx=5, pady=10, sticky="w")

phone_entry = ttk.Entry(main_frame, width=30)
phone_entry.grid(row=2, column=1, padx=5, pady=10)

# --- 4. Sport (Listbox) ---
sport_label = ttk.Label(main_frame, text="Select Sport:")
sport_label.grid(row=3, column=0, padx=5, pady=10, sticky="nw")

sport_listbox = tk.Listbox(main_frame, height=4, width=30, exportselection=False)
sport_listbox.grid(row=3, column=1, padx=5, pady=10)

# Add sports to the listbox
sports = ["Football", "Basketball", "Tennis", "Cricket"]
for s in sports:
    sport_listbox.insert(tk.END, s)

# --- 5. Terms (Checkbutton) ---
terms_var = tk.BooleanVar()
terms_check = ttk.Checkbutton(main_frame, 
                              text="I agree to the terms.",
                              variable=terms_var)
terms_check.grid(row=4, column=1, padx=5, pady=10, sticky="w")

# --- 6. Buttons ---
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=5, column=0, columnspan=2, pady=15)

submit_button = ttk.Button(button_frame, text="Submit", command=submit_form)
submit_button.pack(side="left", padx=10)

clear_button = ttk.Button(button_frame, text="Clear", command=clear_form)
clear_button.pack(side="left", padx=10)

# --- Run the Application ---
root.mainloop()