import tkinter as tk
from tkinter import ttk  # For a modern look
from tkinter import messagebox

# --- Functions ---

def perform_transfer():
    """Simulates the fund transfer process."""
    
    # 1. Get data from form
    from_account = from_account_combo.get()
    to_account = to_account_entry.get()
    recipient_name = recipient_name_entry.get()
    amount_str = amount_entry.get()
    remarks = remarks_entry.get()
    
    # --- 2. Validation ---
    
    # Check for empty essential fields
    if not all([from_account, to_account, recipient_name, amount_str]):
        messagebox.showerror("Error", "Please fill all required fields:\n"
                                     "- From Account\n"
                                     "- Recipient Account No.\n"
                                     "- Recipient Name\n"
                                     "- Amount")
        return

    # Check for a valid amount
    try:
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError("Amount must be positive.")
    except ValueError:
        messagebox.showerror("Error", "Invalid Amount. Please enter a valid number (e.g., 1500.50).")
        amount_entry.delete(0, tk.END)
        amount_entry.focus_set()
        return

    # --- 3. Confirmation (Simulated) ---
    
    # Format the message
    confirm_message = (
        f"**Please Confirm Transaction:**\n\n"
        f"**From:** {from_account}\n"
        f"**To:** {recipient_name} ({to_account})\n"
        f"**Amount:** ₹{amount:,.2f}\n"  # Format as currency
        f"**Remarks:** {remarks if remarks else 'None'}\n\n"
        f"Proceed with transfer?"
    )
    
    # Show a confirmation dialog
    is_confirmed = messagebox.askyesno("Confirm Transfer", confirm_message)
    
    if is_confirmed:
        # --- 4. Process (Simulated) ---
        print(f"Processing transfer of ₹{amount} from {from_account} to {to_account}")
        
        messagebox.showinfo("Success", f"Transfer of ₹{amount:,.2f} to {recipient_name} was successful!")
        
        # Clear the form
        clear_form()
    else:
        messagebox.showinfo("Cancelled", "Fund transfer was cancelled.")

def clear_form():
    """Clears all fields and resets the form."""
    from_account_combo.set("")
    to_account_entry.delete(0, tk.END)
    recipient_name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    remarks_entry.delete(0, tk.END)
    from_account_combo.focus_set()

# --- Main Application Window ---
root = tk.Tk()
root.title("Fund Transfer")
root.geometry("450x450")
root.resizable(False, False)

# --- Use a Themed Frame for styling ---
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

# --- 1. Title ---
title_label = ttk.Label(main_frame, text="Fund Transfer 💸", 
                        font=("Arial", 20, "bold"))
# columnspan=2 makes the label span across both columns
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# --- 2. From Account (Dropdown) ---
from_account_label = ttk.Label(main_frame, text="From Account:")
from_account_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

# A sample list of accounts
account_list = [
    "Savings Account (***1234)",
    "Checking Account (***5678)"
]

from_account_combo = ttk.Combobox(main_frame, values=account_list, 
                                  width=35, state="readonly")
from_account_combo.grid(row=1, column=1, padx=10, pady=5)

# --- 3. Recipient Account Number (Text) ---
to_account_label = ttk.Label(main_frame, text="Recipient Account No:")
to_account_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

to_account_entry = ttk.Entry(main_frame, width=38)
to_account_entry.grid(row=2, column=1, padx=10, pady=5)

# --- 4. Recipient Name (Text) ---
recipient_name_label = ttk.Label(main_frame, text="Recipient Name:")
recipient_name_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

recipient_name_entry = ttk.Entry(main_frame, width=38)
recipient_name_entry.grid(row=3, column=1, padx=10, pady=5)

# --- 5. Amount (Text) ---
amount_label = ttk.Label(main_frame, text="Amount (₹):")
amount_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)

amount_entry = ttk.Entry(main_frame, width=38)
amount_entry.grid(row=4, column=1, padx=10, pady=5)

# --- 6. Remarks (Text) ---
remarks_label = ttk.Label(main_frame, text="Remarks (Optional):")
remarks_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)

remarks_entry = ttk.Entry(main_frame, width=38)
remarks_entry.grid(row=5, column=1, padx=10, pady=5)

# --- 7. Buttons (Frame) ---
# A new frame to hold the buttons
button_frame = ttk.Frame(main_frame)
button_frame.grid(row=6, column=0, columnspan=2, pady=30)

# Transfer Button
transfer_button = ttk.Button(button_frame, text="Transfer Now", command=perform_transfer)
transfer_button.pack(side="left", padx=15, ipadx=10, ipady=5)

# Cancel Button
cancel_button = ttk.Button(button_frame, text="Cancel", command=clear_form)
cancel_button.pack(side="left", padx=15, ipadx=10, ipady=5)

# --- Run the Application ---
root.mainloop()
