import tkinter as tk
from tkinter import ttk  # For modern-looking widgets
from tkinter import messagebox

# --- Functions ---

def submit_feedback():
    """Gathers all feedback data and displays it in a message box."""
    
    # 1. Get Customer Info
    name = name_entry.get()
    room = room_entry.get()
    meal = meal_combo.get()
    
    # 2. Get Ratings
    # Use .get() on the variables, not the scales themselves
    quality = quality_var.get()
    presentation = presentation_var.get()
    service = service_var.get()
    
    # 3. Get Comments
    # "1.0" means start at line 1, character 0. tk.END means "to the end".
    # .strip() removes any trailing newlines.
    comments = comments_text.get("1.0", tk.END).strip()
    
    # --- Validation ---
    if not name or not meal:
        messagebox.showerror("Error", "Please enter your Name and select a Meal.")
        return
        
    # --- Format and Display Success Message ---
    feedback_summary = f"**Thank You, {name}!**\n\n"
    feedback_summary += "We have received your feedback:\n\n"
    feedback_summary += f"**Room:** {room if room else 'N/A'}\n"
    feedback_summary += f"**Meal:** {meal}\n\n"
    feedback_summary += "**Your Ratings:**\n"
    feedback_summary += f"  - Food Quality: {quality:.1f} / 5.0\n"
    feedback_summary += f"  - Presentation: {presentation:.1f} / 5.0\n"
    feedback_summary += f"  - Service Speed: {service:.1f} / 5.0\n\n"
    feedback_summary += f"**Comments:**\n{comments if comments else 'None'}"
    
    messagebox.showinfo("Feedback Submitted", feedback_summary)
    
    # Clear the form after successful submission
    clear_form()

def clear_form():
    """Resets all form fields to their default state."""
    name_entry.delete(0, tk.END)
    room_entry.delete(0, tk.END)
    meal_combo.set("") # Clear combobox
    
    # Reset scales to their default value (e.g., 3)
    quality_var.set(3.0)
    presentation_var.set(3.0)
    service_var.set(3.0)
    
    # Clear the text box
    comments_text.delete("1.0", tk.END)
    
    # Set focus back to the first field
    name_entry.focus_set()

# --- Main Application Window ---
root = tk.Tk()
root.title("Hotel Food Feedback Form")
root.geometry("500x650") # Set window size
root.resizable(False, False) # Make window non-resizable

# Use a main frame with padding
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

# --- 1. Form Title ---
title_label = ttk.Label(main_frame, text="Food Feedback Form 🍽️", 
                        font=("Arial", 20, "bold"))
# Use .grid() for layout. columnspan=2 to span across both columns
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# --- 2. Customer Info Section ---
# Frame for customer details
info_frame = ttk.LabelFrame(main_frame, text="Your Details", padding="10")
info_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew") # ew = stretch east-west

ttk.Label(info_frame, text="Full Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = ttk.Entry(info_frame, width=40)
name_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(info_frame, text="Room Number:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
room_entry = ttk.Entry(info_frame, width=40)
room_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(info_frame, text="Meal:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
meal_combo = ttk.Combobox(info_frame, width=38, 
                          values=["Breakfast", "Lunch", "Dinner", "Room Service"], 
                          state="readonly") # readonly = user can't type
meal_combo.grid(row=2, column=1, padx=5, pady=5)

# --- 3. Ratings Section ---
ratings_frame = ttk.LabelFrame(main_frame, text="Please Rate Your Experience (1=Poor, 5=Excellent)", padding="10")
ratings_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Variables to store scale values
quality_var = tk.DoubleVar(value=3.0)
presentation_var = tk.DoubleVar(value=3.0)
service_var = tk.DoubleVar(value=3.0)

# Food Quality Slider
ttk.Label(ratings_frame, text="Food Quality:").grid(row=0, column=0, padx=5, pady=10, sticky="w")
ttk.Scale(ratings_frame, from_=1, to=5, orient="horizontal", 
          variable=quality_var, length=300).grid(row=0, column=1, padx=5, pady=10)

# Food Presentation Slider
ttk.Label(ratings_frame, text="Presentation:").grid(row=1, column=0, padx=5, pady=10, sticky="w")
ttk.Scale(ratings_frame, from_=1, to=5, orient="horizontal", 
          variable=presentation_var, length=300).grid(row=1, column=1, padx=5, pady=10)

# Service Speed Slider
ttk.Label(ratings_frame, text="Service Speed:").grid(row=2, column=0, padx=5, pady=10, sticky="w")
ttk.Scale(ratings_frame, from_=1, to=5, orient="horizontal", 
          variable=service_var, length=300).grid(row=2, column=1, padx=5, pady=10)

# --- 4. Comments Section (Multi-line Text) ---
comments_frame = ttk.LabelFrame(main_frame, text="Additional Comments", padding="10")
comments_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Frame to hold text box and scrollbar
text_scroll_frame = ttk.Frame(comments_frame)
text_scroll_frame.pack(fill="both", expand=True)

# Create Scrollbar
comments_scroll = ttk.Scrollbar(text_scroll_frame)
comments_scroll.pack(side="right", fill="y")

# Create Text widget
comments_text = tk.Text(text_scroll_frame, width=50, height=5, 
                        wrap="word", yscrollcommand=comments_scroll.set)
comments_text.pack(side="left", fill="both", expand=True)

# Link scrollbar to text widget
comments_scroll.config(command=comments_text.yview)

# --- 5. Submission Buttons ---
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=4, column=0, columnspan=2, pady=20)

submit_button = ttk.Button(button_frame, text="Submit Feedback", command=submit_feedback)
submit_button.pack(side="left", padx=20, ipadx=10, ipady=5) # ipad = internal padding

clear_button = ttk.Button(button_frame, text="Clear Form", command=clear_form)
clear_button.pack(side="left", padx=20, ipadx=10, ipady=5)

# --- Run the Application ---
root.mainloop()