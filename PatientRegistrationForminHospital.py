import tkinter as tk
from tkinter import ttk  # For a modern, themed look
from tkinter import messagebox

# --- Functions ---

def register_patient():
    """Gathers data from the form and displays it."""
    
    # 1. Get data from Entry widgets
    name = name_entry.get()
    phone = phone_entry.get()
    emergency_contact = emergency_entry.get()
    
    # 2. Get data from Radiobuttons
    gender = gender_var.get()
    
    # 3. Get data from Listbox
    try:
        # Get the index of the selected item
        selected_index = dept_listbox.curselection()[0]
        department = dept_listbox.get(selected_index)
    except IndexError:
        department = "Not Selected" # Handle case where nothing is selected
        
    # 4. Get data from Checkbutton
    is_first_visit = "Yes" if first_visit_var.get() else "No"
    
    # 5. Get data from Text widget
    # "1.0" means start at line 1, character 0. tk.END means "to the end".
    history = history_text.get("1.0", tk.END).strip()
    
    # --- Validation ---
    if not name or not phone or not gender or department == "Not Selected":
        messagebox.showerror("Error", "Please fill all required fields:\n"
                                     "- Full Name\n"
                                     "- Phone Number\n"
                                     "- Gender\n"
                                     "- Department")
        return
        
    # --- Show Success Message ---
    info_message = f"**Patient Registered Successfully!**\n\n"
    info_message += f"**Name:** {name}\n"
    info_message += f"**Phone:** {phone}\n"
    info_message += f"**Gender:** {gender}\n"
    info_message += f"**Department:** {department}\n"
    info_message += f"**Emergency Contact:** {emergency_contact if emergency_contact else 'N/A'}\n"
    info_message += f"**First Visit:** {is_first_visit}\n\n"
    info_message += f"**Medical History:**\n{history if history else 'None'}"
    
    messagebox.showinfo("Registration Details", info_message)
    # After successful registration, clear the form
    clear_form()

def clear_form():
    """Clears all input fields to their default state."""
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    emergency_entry.delete(0, tk.END)
    
    gender_var.set("")  # Deselects radio buttons
    dept_listbox.selection_clear(0, tk.END)  # Deselects listbox item
    first_visit_var.set(False)  # Unchecks the checkbox
    history_text.delete("1.0", tk.END) # Clear text widget
    
    name_entry.focus_set() # Set focus back to the first field

# --- Main Application Window ---
root = tk.Tk()
root.title("Hospital Patient Registration 🏥")
root.geometry("550x700") # Set window size
root.resizable(False, False) # Make window non-resizable

# Use a 'main_frame' with padding to give spacing around the edge
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

# --- Form Title ---
title_label = ttk.Label(main_frame, text="Patient Registration Form", 
                        font=("Arial", 20, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# --- Form Fields (using .grid() layout) ---

# 1. Full Name (Label + Text/Entry)
name_label = ttk.Label(main_frame, text="Full Name:")
name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

name_entry = ttk.Entry(main_frame, width=40)
name_entry.grid(row=1, column=1, padx=10, pady=10)

# 2. Phone Number (Label + Text/Entry)
phone_label = ttk.Label(main_frame, text="Phone Number:")
phone_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

phone_entry = ttk.Entry(main_frame, width=40)
phone_entry.grid(row=2, column=1, padx=10, pady=10)

# 3. Gender (Label + Radiobuttons)
gender_label = ttk.Label(main_frame, text="Gender:")
gender_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

gender_var = tk.StringVar()
# A frame to hold the radio buttons horizontally
gender_frame = ttk.Frame(main_frame)
gender_frame.grid(row=3, column=1, padx=10, pady=10, sticky="w")

ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left")
ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left", padx=10)
ttk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other").pack(side="left")

# 4. Emergency Contact (Label + Text/Entry)
emergency_label = ttk.Label(main_frame, text="Emergency Contact:")
emergency_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

emergency_entry = ttk.Entry(main_frame, width=40)
emergency_entry.grid(row=4, column=1, padx=10, pady=10)

# 5. Department (Label + Listbox)
dept_label = ttk.Label(main_frame, text="Department to Visit:")
# 'nw' = North-West (align top-left)
dept_label.grid(row=5, column=0, padx=10, pady=10, sticky="nw") 

# Frame to hold listbox and scrollbar
listbox_frame = ttk.Frame(main_frame)
listbox_frame.grid(row=5, column=1, padx=10, pady=10, sticky="w")

dept_scrollbar = ttk.Scrollbar(listbox_frame, orient="vertical")
dept_listbox = tk.Listbox(listbox_frame, height=5, width=38, 
                           yscrollcommand=dept_scrollbar.set, exportselection=False)
dept_scrollbar.config(command=dept_listbox.yview) # Link scrollbar to listbox

dept_scrollbar.pack(side="right", fill="y")
dept_listbox.pack(side="left")

# Add items to the Listbox
departments = [
    "General Medicine", "Cardiology", "Orthopedics", "Neurology",
    "Pediatrics", "Gynecology", "Dermatology", "ENT"
]
for item in departments:
    dept_listbox.insert(tk.END, item)

# 6. Medical History (Label + Text Widget)
history_label = ttk.Label(main_frame, text="Brief Medical History:")
history_label.grid(row=6, column=0, padx=10, pady=10, sticky="nw")

history_frame = ttk.Frame(main_frame)
history_frame.grid(row=6, column=1, padx=10, pady=10)

history_scroll = ttk.Scrollbar(history_frame)
history_scroll.pack(side="right", fill="y")

history_text = tk.Text(history_frame, width=36, height=5, 
                       wrap="word", yscrollcommand=history_scroll.set)
history_text.pack(side="left")
history_scroll.config(command=history_text.yview)

# 7. First Visit (Checkbutton)
first_visit_var = tk.BooleanVar()
first_visit_check = ttk.Checkbutton(main_frame, 
                                    text="This is my first visit", 
                                    variable=first_visit_var)
first_visit_check.grid(row=7, column=1, padx=10, pady=15, sticky="w")

# 8. Buttons (Submit, Clear)
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=8, column=0, columnspan=2, pady=20)

submit_button = ttk.Button(button_frame, text="Register Patient", command=register_patient)
submit_button.pack(side="left", padx=20, ipadx=10, ipady=5)

clear_button = ttk.Button(button_frame, text="Clear Form", command=clear_form)
clear_button.pack(side="left", padx=20, ipadx=10, ipady=5)

# --- Run the Application ---
root.mainloop()
