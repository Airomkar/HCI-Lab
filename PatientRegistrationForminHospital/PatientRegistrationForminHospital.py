import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# --- Functions ---

def submit_form():
    """Handles form submission."""
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    contact = contact_entry.get()
    address = address_text.get("1.0", tk.END).strip()
    
    # Get selected doctor specialization from listbox
    selected_index = specialization_listbox.curselection()
    specialization = specialization_listbox.get(selected_index) if selected_index else "Not Selected"
    
    # Collect symptoms
    selected_symptoms = []
    if fever_var.get():
        selected_symptoms.append("Fever")
    if cough_var.get():
        selected_symptoms.append("Cough")
    if headache_var.get():
        selected_symptoms.append("Headache")
    if bp_var.get():
        selected_symptoms.append("High/Low BP")
    if diabetes_var.get():
        selected_symptoms.append("Diabetes")

    # --- Validation ---
    if not name or not age or not gender or not contact:
        messagebox.showerror("Error", "Please fill all required fields (Name, Age, Gender, Contact).")
        return

    # --- Success Message ---
    summary = (
        f"✅ Patient Registration Successful!\n\n"
        f"Name: {name}\n"
        f"Age: {age}\n"
        f"Gender: {gender}\n"
        f"Contact: {contact}\n"
        f"Address: {address}\n"
        f"Doctor Specialization: {specialization}\n"
        f"Symptoms: {', '.join(selected_symptoms) if selected_symptoms else 'None'}"
    )
    messagebox.showinfo("Patient Registered", summary)
    clear_form()


def clear_form():
    """Reset all form fields."""
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    address_text.delete("1.0", tk.END)
    gender_var.set("")
    fever_var.set(0)
    cough_var.set(0)
    headache_var.set(0)
    bp_var.set(0)
    diabetes_var.set(0)
    specialization_listbox.selection_clear(0, tk.END)
    name_entry.focus_set()


def exit_form():
    """Exit confirmation."""
    if messagebox.askyesno("Exit", "Do you want to close the registration form?"):
        root.destroy()


# --- Main Window Setup ---

root = tk.Tk()
root.title("Hospital Patient Registration Form")
root.geometry("650x750")
root.resizable(False, False)

frame = ttk.Frame(root, padding="25 25 25 25")
frame.pack(expand=True)

# --- Title ---
title_label = ttk.Label(frame, text="🏥 Patient Registration Form", font=("Arial", 22, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=15)

# --- Name ---
name_label = ttk.Label(frame, text="Full Name:")
name_label.grid(row=1, column=0, sticky="w", padx=10, pady=8)
name_entry = ttk.Entry(frame, width=40)
name_entry.grid(row=1, column=1, pady=8)

# --- Age ---
age_label = ttk.Label(frame, text="Age:")
age_label.grid(row=2, column=0, sticky="w", padx=10, pady=8)
age_entry = ttk.Entry(frame, width=40)
age_entry.grid(row=2, column=1, pady=8)

# --- Gender (Radiobuttons) ---
gender_label = ttk.Label(frame, text="Gender:")
gender_label.grid(row=3, column=0, sticky="w", padx=10, pady=8)
gender_var = tk.StringVar()
ttk.Radiobutton(frame, text="Male", value="Male", variable=gender_var).grid(row=3, column=1, sticky="w", padx=10)
ttk.Radiobutton(frame, text="Female", value="Female", variable=gender_var).grid(row=3, column=1, sticky="w", padx=80)
ttk.Radiobutton(frame, text="Other", value="Other", variable=gender_var).grid(row=3, column=1, sticky="w", padx=160)

# --- Contact ---
contact_label = ttk.Label(frame, text="Contact Number:")
contact_label.grid(row=4, column=0, sticky="w", padx=10, pady=8)
contact_entry = ttk.Entry(frame, width=40)
contact_entry.grid(row=4, column=1, pady=8)

# --- Address (Text Widget) ---
address_label = ttk.Label(frame, text="Address:")
address_label.grid(row=5, column=0, sticky="nw", padx=10, pady=8)
address_text = tk.Text(frame, width=30, height=4, font=("Arial", 10))
address_text.grid(row=5, column=1, pady=8)

# --- Symptoms (Checkbuttons) ---
symptom_label = ttk.Label(frame, text="Symptoms:")
symptom_label.grid(row=6, column=0, sticky="nw", padx=10, pady=8)

fever_var = tk.IntVar()
cough_var = tk.IntVar()
headache_var = tk.IntVar()
bp_var = tk.IntVar()
diabetes_var = tk.IntVar()

ttk.Checkbutton(frame, text="Fever", variable=fever_var).grid(row=6, column=1, sticky="w")
ttk.Checkbutton(frame, text="Cough", variable=cough_var).grid(row=7, column=1, sticky="w")
ttk.Checkbutton(frame, text="Headache", variable=headache_var).grid(row=8, column=1, sticky="w")
ttk.Checkbutton(frame, text="High/Low BP", variable=bp_var).grid(row=9, column=1, sticky="w")
ttk.Checkbutton(frame, text="Diabetes", variable=diabetes_var).grid(row=10, column=1, sticky="w")

# --- Doctor Specialization (Listbox) ---
specialization_label = ttk.Label(frame, text="Select Doctor Specialization:")
specialization_label.grid(row=11, column=0, sticky="nw", padx=10, pady=10)

specialization_listbox = tk.Listbox(frame, height=5, width=30, font=("Arial", 10))
specialization_listbox.grid(row=11, column=1, pady=10)
specializations = ["General Physician", "Cardiologist", "Dermatologist", "Neurologist", "Dentist", "Pediatrician"]
for spec in specializations:
    specialization_listbox.insert(tk.END, spec)

# --- Buttons ---
submit_button = ttk.Button(frame, text="Submit", command=submit_form)
submit_button.grid(row=12, column=0, columnspan=2, pady=20, ipadx=10, ipady=5)

clear_button = ttk.Button(frame, text="Clear", command=clear_form)
clear_button.grid(row=13, column=0, columnspan=2, pady=5, ipadx=10, ipady=5)

exit_button = ttk.Button(frame, text="Exit", command=exit_form)
exit_button.grid(row=14, column=0, columnspan=2, pady=5, ipadx=10, ipady=5)

# --- Run App ---
root.mainloop()
