import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# --- Functions ---

def transfer_funds():
    """Handles the fund transfer process."""
    sender_acc = sender_entry.get()
    receiver_acc = receiver_entry.get()
    receiver_name = receiver_name_entry.get()
    amount = amount_entry.get()
    mode = mode_var.get()

    # --- Validation ---
    if not all([sender_acc, receiver_acc, receiver_name, amount, mode]):
        messagebox.showerror("Error", "All fields are required!")
        return
    
    if not amount.isdigit() or int(amount) <= 0:
        messagebox.showerror("Error", "Please enter a valid positive amount.")
        return
    
    if sender_acc == receiver_acc:
        messagebox.showerror("Error", "Sender and Receiver Account cannot be same!")
        return

    # --- Success Message ---
    success_message = (
        f"Fund Transfer Successful!\n\n"
        f"From Account: {sender_acc}\n"
        f"To Account: {receiver_acc}\n"
        f"Receiver Name: {receiver_name}\n"
        f"Amount: ₹{amount}\n"
        f"Mode: {mode}\n"
    )
    messagebox.showinfo("Transaction Complete", success_message)
    clear_form()


def clear_form():
    """Clears all the fields."""
    sender_entry.delete(0, tk.END)
    receiver_entry.delete(0, tk.END)
    receiver_name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    mode_var.set("")
    sender_entry.focus_set()

def exit_app():
    """Exit confirmation."""
    if messagebox.askyesno("Exit", "Do you want to close the application?"):
        root.destroy()


# --- Main Window Setup ---

root = tk.Tk()
root.title("Fund Transfer Window")
root.geometry("500x500")
root.resizable(False, False)

frame = ttk.Frame(root, padding="30 30 30 30")
frame.pack(expand=True)

# --- Title ---
title_label = ttk.Label(frame, text="Fund Transfer", font=("Arial", 22, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=15)

# --- Sender Account ---
sender_label = ttk.Label(frame, text="Sender Account No.:")
sender_label.grid(row=1, column=0, sticky="w", padx=10, pady=8)
sender_entry = ttk.Entry(frame, width=30, font=("Arial", 11))
sender_entry.grid(row=1, column=1, padx=10, pady=8)

# --- Receiver Account ---
receiver_label = ttk.Label(frame, text="Receiver Account No.:")
receiver_label.grid(row=2, column=0, sticky="w", padx=10, pady=8)
receiver_entry = ttk.Entry(frame, width=30, font=("Arial", 11))
receiver_entry.grid(row=2, column=1, padx=10, pady=8)

# --- Receiver Name ---
receiver_name_label = ttk.Label(frame, text="Receiver Name:")
receiver_name_label.grid(row=3, column=0, sticky="w", padx=10, pady=8)
receiver_name_entry = ttk.Entry(frame, width=30, font=("Arial", 11))
receiver_name_entry.grid(row=3, column=1, padx=10, pady=8)

# --- Amount ---
amount_label = ttk.Label(frame, text="Amount (₹):")
amount_label.grid(row=4, column=0, sticky="w", padx=10, pady=8)
amount_entry = ttk.Entry(frame, width=30, font=("Arial", 11))
amount_entry.grid(row=4, column=1, padx=10, pady=8)

# --- Mode of Payment ---
mode_label = ttk.Label(frame, text="Mode of Payment:")
mode_label.grid(row=5, column=0, sticky="w", padx=10, pady=8)
mode_var = tk.StringVar()
mode_combo = ttk.Combobox(frame, textvariable=mode_var, width=28, font=("Arial", 11))
mode_combo['values'] = ("UPI", "Net Banking", "NEFT", "IMPS")
mode_combo.grid(row=5, column=1, padx=10, pady=8)

# --- Buttons ---
transfer_button = ttk.Button(frame, text="Transfer", command=transfer_funds)
transfer_button.grid(row=6, column=0, columnspan=2, pady=20, ipadx=10, ipady=5)

clear_button = ttk.Button(frame, text="Clear", command=clear_form)
clear_button.grid(row=7, column=0, columnspan=2, pady=5, ipadx=10, ipady=5)

exit_button = ttk.Button(frame, text="Exit", command=exit_app)
exit_button.grid(row=8, column=0, columnspan=2, pady=10, ipadx=10, ipady=5)

# --- Run Application ---
root.mainloop()
