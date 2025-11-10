import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

# --- Functions ---

def book_cab():
    """Handles cab booking confirmation."""
    name = name_entry.get()
    pickup = pickup_entry.get()
    drop = drop_entry.get()
    vehicle = vehicle_type.get()
    date = date_entry.get()
    time = time_entry.get()
    
    # --- Validation ---
    if not all([name, pickup, drop, vehicle, date, time]):
        messagebox.showerror("Error", "All fields are required!")
        return

    # Simple success message (In real app, data would be stored in DB)
    booking_details = (
        f"Booking Confirmed!\n\n"
        f"Name: {name}\n"
        f"Pickup: {pickup}\n"
        f"Drop: {drop}\n"
        f"Vehicle Type: {vehicle}\n"
        f"Date: {date}\n"
        f"Time: {time}\n"
    )
    messagebox.showinfo("Success", booking_details)
    clear_form()

def clear_form():
    """Clears all fields."""
    name_entry.delete(0, tk.END)
    pickup_entry.delete(0, tk.END)
    drop_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    vehicle_type.set("")
    name_entry.focus_set()

def exit_app():
    """Exit confirmation."""
    if messagebox.askyesno("Exit", "Do you want to close the application?"):
        root.destroy()

# --- Main Window ---

root = tk.Tk()
root.title("Cab/Auto Booking App")
root.geometry("500x500")
root.resizable(False, False)

# --- Frame Setup ---
frame = ttk.Frame(root, padding="30 30 30 30")
frame.pack(expand=True)

# --- Title ---
title_label = ttk.Label(frame, text="Cab / Auto Booking", font=("Arial", 22, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=15)

# --- Name ---
name_label = ttk.Label(frame, text="Full Name:")
name_label.grid(row=1, column=0, sticky="w", padx=10, pady=8)
name_entry = ttk.Entry(frame, width=30, font=("Arial", 11))
name_entry.grid(row=1, column=1, padx=10, pady=8)

# --- Pickup Location ---
pickup_label = ttk.Label(frame, text="Pickup Location:")
pickup_label.grid(row=2, column=0, sticky="w", padx=10, pady=8)
pickup_entry = ttk.Entry(frame, width=30, font=("Arial", 11))
pickup_entry.grid(row=2, column=1, padx=10, pady=8)

# --- Drop Location ---
drop_label = ttk.Label(frame, text="Drop Location:")
drop_label.grid(row=3, column=0, sticky="w", padx=10, pady=8)
drop_entry = ttk.Entry(frame, width=30, font=("Arial", 11))
drop_entry.grid(row=3, column=1, padx=10, pady=8)

# --- Vehicle Type ---
vehicle_label = ttk.Label(frame, text="Select Vehicle Type:")
vehicle_label.grid(row=4, column=0, sticky="w", padx=10, pady=8)

vehicle_type = tk.StringVar()
vehicle_dropdown = ttk.Combobox(frame, textvariable=vehicle_type, width=28, font=("Arial", 11))
vehicle_dropdown['values'] = ("Cab", "Auto", "Mini Cab", "Luxury Cab")
vehicle_dropdown.grid(row=4, column=1, padx=10, pady=8)

# --- Date ---
date_label = ttk.Label(frame, text="Date (DD-MM-YYYY):")
date_label.grid(row=5, column=0, sticky="w", padx=10, pady=8)
date_entry = ttk.Entry(frame, width=30, font=("Arial", 11))
date_entry.insert(0, datetime.now().strftime("%d-%m-%Y"))  # Auto-fill today's date
date_entry.grid(row=5, column=1, padx=10, pady=8)

# --- Time ---
time_label = ttk.Label(frame, text="Time (HH:MM):")
time_label.grid(row=6, column=0, sticky="w", padx=10, pady=8)
time_entry = ttk.Entry(frame, width=30, font=("Arial", 11))
time_entry.insert(0, datetime.now().strftime("%H:%M"))
time_entry.grid(row=6, column=1, padx=10, pady=8)

# --- Buttons ---
book_button = ttk.Button(frame, text="Book Ride", command=book_cab)
book_button.grid(row=7, column=0, columnspan=2, pady=20, ipadx=10, ipady=5)

clear_button = ttk.Button(frame, text="Clear", command=clear_form)
clear_button.grid(row=8, column=0, columnspan=2, pady=5, ipadx=10, ipady=5)

exit_button = ttk.Button(frame, text="Exit", command=exit_app)
exit_button.grid(row=9, column=0, columnspan=2, pady=10, ipadx=10, ipady=5)

# --- Run App ---
root.mainloop()
