import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# --- Functions ---

def submit_feedback():
    """Collect and display feedback."""
    name = name_entry.get()
    email = email_entry.get()
    food_quality = food_quality_var.get()
    service_quality = service_quality_var.get()
    ambiance = ambiance_var.get()
    suggestion = suggestion_text.get("1.0", tk.END).strip()

    # --- Validation ---
    if not name or not email:
        messagebox.showerror("Error", "Please enter your Name and Email!")
        return

    # --- Collect selected feedback ---
    liked_items = []
    if taste_var.get():
        liked_items.append("Taste")
    if cleanliness_var.get():
        liked_items.append("Cleanliness")
    if price_var.get():
        liked_items.append("Price")
    if staff_var.get():
        liked_items.append("Staff Service")

    # Prepare the result
    feedback_summary = (
        f"Thank you for your feedback!\n\n"
        f"Name: {name}\n"
        f"Email: {email}\n\n"
        f"Food Quality: {food_quality}\n"
        f"Service Quality: {service_quality}\n"
        f"Ambiance: {ambiance}\n"
        f"Liked Aspects: {', '.join(liked_items) if liked_items else 'None'}\n\n"
        f"Suggestions:\n{suggestion if suggestion else 'No additional comments.'}"
    )

    # Display thank-you message
    messagebox.showinfo("Feedback Submitted", feedback_summary)
    clear_form()


def clear_form():
    """Reset all form fields."""
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    food_quality_var.set("Good")
    service_quality_var.set("Good")
    ambiance_var.set("Good")
    taste_var.set(0)
    cleanliness_var.set(0)
    price_var.set(0)
    staff_var.set(0)
    suggestion_text.delete("1.0", tk.END)
    name_entry.focus_set()

def exit_app():
    """Exit confirmation."""
    if messagebox.askyesno("Exit", "Do you want to close the Feedback Form?"):
        root.destroy()


# --- Main Window ---
root = tk.Tk()
root.title("Hotel Food Feedback Form")
root.geometry("550x600")
root.resizable(False, False)

frame = ttk.Frame(root, padding="25 25 25 25")
frame.pack(expand=True)

# --- Title ---
title_label = ttk.Label(frame, text="Customer Feedback Form", font=("Arial", 22, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=15)

# --- Customer Details ---
name_label = ttk.Label(frame, text="Name:")
name_label.grid(row=1, column=0, sticky="w", padx=10, pady=8)
name_entry = ttk.Entry(frame, width=35)
name_entry.grid(row=1, column=1, pady=8)

email_label = ttk.Label(frame, text="Email:")
email_label.grid(row=2, column=0, sticky="w", padx=10, pady=8)
email_entry = ttk.Entry(frame, width=35)
email_entry.grid(row=2, column=1, pady=8)

# --- Ratings using Radiobuttons ---
food_quality_var = tk.StringVar(value="Good")
service_quality_var = tk.StringVar(value="Good")
ambiance_var = tk.StringVar(value="Good")

ttk.Label(frame, text="Food Quality:").grid(row=3, column=0, sticky="w", padx=10, pady=8)
for i, level in enumerate(["Excellent", "Good", "Average", "Poor"]):
    ttk.Radiobutton(frame, text=level, value=level, variable=food_quality_var).grid(row=3, column=i+1, sticky="w")

ttk.Label(frame, text="Service Quality:").grid(row=4, column=0, sticky="w", padx=10, pady=8)
for i, level in enumerate(["Excellent", "Good", "Average", "Poor"]):
    ttk.Radiobutton(frame, text=level, value=level, variable=service_quality_var).grid(row=4, column=i+1, sticky="w")

ttk.Label(frame, text="Ambiance:").grid(row=5, column=0, sticky="w", padx=10, pady=8)
for i, level in enumerate(["Excellent", "Good", "Average", "Poor"]):
    ttk.Radiobutton(frame, text=level, value=level, variable=ambiance_var).grid(row=5, column=i+1, sticky="w")

# --- Checkbuttons (Liked Aspects) ---
ttk.Label(frame, text="What did you like most?").grid(row=6, column=0, sticky="w", padx=10, pady=10)
taste_var = tk.IntVar()
cleanliness_var = tk.IntVar()
price_var = tk.IntVar()
staff_var = tk.IntVar()

ttk.Checkbutton(frame, text="Taste", variable=taste_var).grid(row=6, column=1, sticky="w")
ttk.Checkbutton(frame, text="Cleanliness", variable=cleanliness_var).grid(row=6, column=2, sticky="w")
ttk.Checkbutton(frame, text="Price", variable=price_var).grid(row=6, column=3, sticky="w")
ttk.Checkbutton(frame, text="Staff Service", variable=staff_var).grid(row=6, column=4, sticky="w")

# --- Suggestions (Text box) ---
suggestion_label = ttk.Label(frame, text="Additional Suggestions:")
suggestion_label.grid(row=7, column=0, sticky="nw", padx=10, pady=10)
suggestion_text = tk.Text(frame, width=40, height=5, font=("Arial", 10))
suggestion_text.grid(row=7, column=1, columnspan=3, pady=10)

# --- Buttons ---
submit_button = ttk.Button(frame, text="Submit", command=submit_feedback)
submit_button.grid(row=8, column=0, columnspan=2, pady=15, ipadx=10, ipady=5)

clear_button = ttk.Button(frame, text="Clear", command=clear_form)
clear_button.grid(row=9, column=0, columnspan=2, pady=5, ipadx=10, ipady=5)

exit_button = ttk.Button(frame, text="Exit", command=exit_app)
exit_button.grid(row=10, column=0, columnspan=2, pady=5, ipadx=10, ipady=5)

# --- Run App ---
root.mainloop()
