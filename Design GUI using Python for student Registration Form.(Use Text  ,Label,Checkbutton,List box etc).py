import tkinter as tk
from tkinter import ttk  # For a more modern look
from tkinter import messagebox

# --- Functions ---

def register_student():
    """Gathers data from the form and displays it in a message box."""
    
    # 1. Get data from Entry widgets
    name = name_entry.get()
    email = email_entry.get()
    
    # 2. Get data from Radiobuttons
    gender = gender_var.get()
    
    # 3. Get data from Listbox
    try:
        # Get the index of the selected item
        selected_index = course_listbox.curselection()[0]
        course = course_listbox.get(selected_index)
    except IndexError:
        course = "Not Selected" # Handle case where nothing is selected
        
    # 4. Get data from Checkbutton
    terms_agreed = terms_var.get()
    
    # --- Validation ---
    if not name or not email or not gender or course == "Not Selected":
        messagebox.showerror("Error", "Please fill all fields.")
        return
        
    if not terms_agreed:
        messagebox.showerror("Error", "You must agree to the terms and conditions.")
        return
        
    # --- Show Success Message ---
    info_message = f"**Registration Successful!**\n\n"
    info_message += f"**Name:** {name}\n"
    info_message += f"**Email:** {email}\n"
    info_message += f"**Gender:** {gender}\n"
    info_message += f"**Course:** {course}"
    
    messagebox.showinfo("Registration Details", info_message)
    # After successful registration, clear the form
    clear_form()

def clear_form():
    """Clears all input fields to their default state."""
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    gender_var.set("")  # Deselects radio buttons
    course_listbox.selection_clear(0, tk.END)  # Deselects listbox item
    terms_var.set(False)  # Unchecks the checkbox
    name_entry.focus_set() # Set focus back to the first field

# --- Main Application Window ---
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("500x500") # Set window size
root.resizable(False, False) # Make window non-resizable

# Use a 'main_frame' with padding to give spacing around the edge
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

# --- Form Title ---
title_label = ttk.Label(main_frame, text="Student Registration Form", 
                        font=("Arial", 18, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# --- Form Fields ---

# 1. Name (Label + Text/Entry)
name_label = ttk.Label(main_frame, text="Full Name:")
name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

name_entry = ttk.Entry(main_frame, width=40)
name_entry.grid(row=1, column=1, padx=10, pady=10)

# 2. Email (Label + Text/Entry)
email_label = ttk.Label(main_frame, text="Email Address:")
email_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

email_entry = ttk.Entry(main_frame, width=40)
email_entry.grid(row=2, column=1, padx=10, pady=10)

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

# 4. Course (Label + Listbox)
course_label = ttk.Label(main_frame, text="Select Course:")
course_label.grid(row=4, column=0, padx=10, pady=10, sticky="nw") # 'nw' = North-West (align top-left)

# Frame to hold listbox and scrollbar
listbox_frame = ttk.Frame(main_frame)
listbox_frame.grid(row=4, column=1, padx=10, pady=10, sticky="w")

course_scrollbar = ttk.Scrollbar(listbox_frame, orient="vertical")
course_listbox = tk.Listbox(listbox_frame, height=5, width=38, 
                            yscrollcommand=course_scrollbar.set, exportselection=False)

# Link scrollbar to listbox
course_scrollbar.config(command=course_listbox.yview)

# Place widgets in the frame
course_scrollbar.pack(side="right", fill="y")
course_listbox.pack(side="left")

# Add items to the Listbox
courses = [
    "Computer Science", "Engineering", "Business Administration", 
    "Arts & Humanities", "Medicine", "Law", "Data Science"
]
for item in courses:
    course_listbox.insert(tk.END, item)

# 5. Terms (Checkbutton)
terms_var = tk.BooleanVar()
terms_check = ttk.Checkbutton(main_frame, 
                              text="I agree to the terms and conditions", 
                              variable=terms_var)
terms_check.grid(row=5, column=0, columnspan=2, pady=15)

# 6. Buttons (Submit, Clear)
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=6, column=0, columnspan=2, pady=10)

submit_button = ttk.Button(button_frame, text="Register", command=register_student)
submit_button.pack(side="left", padx=20, ipadx=10) # ipadx gives internal padding

clear_button = ttk.Button(button_frame, text="Clear", command=clear_form)
clear_button.pack(side="left", padx=20, ipadx=10)


# --- Run the Application ---
root.mainloop()