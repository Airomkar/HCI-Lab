import tkinter as tk
from tkinter import ttk  # For modern widgets
from tkinter import messagebox

# --- Mock Help Data ---
# This dictionary stores all the help topics and answers.
# The structure is: Category -> Question -> Answer
HELP_TOPICS = {
    "Getting Started": {
        "How to open a file?": (
            "To open a file:\n\n"
            "1. Go to the 'File' menu at the top.\n"
            "2. Click on 'Open...'\n"
            "3. Select the file you want to open and click 'OK'."
        ),
        "How to save your work?": (
            "To save your file:\n\n"
            "1. Go to the 'File' menu.\n"
            "2. Click on 'Save' to overwrite the current file.\n"
            "3. Click 'Save As...' to save a new copy."
        )
    },
    "Editing": {
        "How to copy and paste text?": (
            "To copy and paste:\n\n"
            "1. Select the text you want to copy.\n"
            "2. Press 'Ctrl+C' (or 'Cmd+C' on Mac) to copy.\n"
            "3. Click where you want to paste the text.\n"
            "4. Press 'Ctrl+V' (or 'Cmd+V' on Mac) to paste."
        ),
        "How to use the Crop tool?": (
            "The Crop tool is for images:\n\n"
            "1. Select the 'Crop' tool from the toolbar.\n"
            "2. Click and drag a box around the area you want to keep.\n"
            "3. Press 'Enter' to apply the crop."
        )
    },
    "Account": {
        "How to reset your password?": (
            "To reset your password:\n\n"
            "1. Go to the 'Account' menu.\n"
            "2. Click on 'Change Password...'\n"
            "3. If you forgot your password, please use the 'Forgot Password' link on our website."
        )
    }
}

# --- Functions ---

def populate_tree(search_term=""):
    """Clears and re-populates the help topic tree."""
    # Delete all existing items
    for item in topic_tree.get_children():
        topic_tree.delete(item)

    search_term = search_term.lower()

    # Insert categories and topics
    for category, questions in HELP_TOPICS.items():
        # Add category as a parent item
        category_id = topic_tree.insert(parent="", index="end", iid=category, 
                                        text=category.upper(), open=True)
        
        # Add questions as child items
        for question, answer in questions.items():
            # If searching, only add items that match
            if search_term:
                if (search_term in question.lower() or 
                    search_term in answer.lower() or 
                    search_term in category.lower()):
                    
                    topic_tree.insert(parent=category_id, index="end", iid=question, 
                                      text=question)
            else:
                # If not searching, add all
                topic_tree.insert(parent=category_id, index="end", iid=question, 
                                  text=question)

def on_topic_select(event):
    """Called when a user clicks on a topic in the tree."""
    
    # Get the ID of the selected item
    selected_id = topic_tree.focus()
    
    # Check if the selected item is a question (a child)
    parent_id = topic_tree.parent(selected_id)
    
    if parent_id: # If it has a parent, it's a question
        question = selected_id
        category = parent_id
        
        # Get the answer from our data
        answer = HELP_TOPICS[category][question]
        
        # Update the text widget
        # Set state to normal to allow editing
        answer_text.config(state="normal")
        
        # Clear previous content
        answer_text.delete("1.0", tk.END)
        
        # Insert new content with a title
        answer_text.insert("1.0", question + "\n\n", "title")
        answer_text.insert(tk.END, answer)
        
        # Set state back to disabled to make it read-only
        answer_text.config(state="disabled")
    else:
        # User clicked a category, clear the text
        answer_text.config(state="normal")
        answer_text.delete("1.0", tk.END)
        answer_text.insert("1.0", "Please select a specific question from the list on the left.")
        answer_text.config(state="disabled")

def search_topics():
    """Filters the tree based on the search entry."""
    term = search_entry.get()
    populate_tree(term)

def clear_search():
    """Clears the search box and repopulates the tree."""
    search_entry.delete(0, tk.END)
    populate_tree()

def contact_support():
    """Opens a simple message box for contacting support."""
    messagebox.showinfo("Contact Support", 
                        "We are here to help!\n\n"
                        "Please email us at: support@yourapp.com\n"
                        "Or call us at: 1-800-555-1234")

# --- Main Application Window ---
root = tk.Tk()
root.title("Help & Support")
root.geometry("800x600")

# --- Style Configuration ---
style = ttk.Style()
style.configure("Treeview", rowheight=25, font=("Arial", 10))
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

# --- Main Layout (Paned Window) ---
# A PanedWindow gives a resizable splitter between two frames
paned_window = ttk.PanedWindow(root, orient="horizontal")
paned_window.pack(fill="both", expand=True, padx=10, pady=10)

# --- 1. Left Frame (Topics) ---
left_frame = ttk.Frame(paned_window, width=300)
paned_window.add(left_frame, weight=1) # weight=1 makes it resize

# Search Bar
search_frame = ttk.Frame(left_frame)
search_frame.pack(fill="x", padx=5, pady=5)

search_label = ttk.Label(search_frame, text="Search:")
search_label.pack(side="left", padx=(0, 5))

search_entry = ttk.Entry(search_frame)
search_entry.pack(side="left", fill="x", expand=True)

search_button = ttk.Button(search_frame, text="Go", width=5, command=search_topics)
search_button.pack(side="left", padx=5)

# Topic Tree
tree_frame = ttk.Frame(left_frame)
tree_frame.pack(fill="both", expand=True, padx=5, pady=5)

topic_tree = ttk.Treeview(tree_frame, show="tree")
topic_tree.pack(side="left", fill="both", expand=True)

# Scrollbar for Tree
tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=topic_tree.yview)
tree_scroll.pack(side="right", fill="y")
topic_tree.config(yscrollcommand=tree_scroll.set)

# Bind the selection event
topic_tree.bind("<<TreeviewSelect>>", on_topic_select)

# --- 2. Right Frame (Answers) ---
right_frame = ttk.Frame(paned_window, width=500)
paned_window.add(right_frame, weight=3) # weight=3 makes it 3x larger

# Answer Text Area
answer_frame = ttk.Frame(right_frame)
answer_frame.pack(fill="both", expand=True, padx=5, pady=5)

answer_text = tk.Text(answer_frame, wrap="word", font=("Arial", 11), 
                      padx=15, pady=15, state="disabled", background="#fdfdfd")
answer_text.pack(side="left", fill="both", expand=True)

# Scrollbar for Text
text_scroll = ttk.Scrollbar(answer_frame, orient="vertical", command=answer_text.yview)
text_scroll.pack(side="right", fill="y")
answer_text.config(yscrollcommand=text_scroll.set)

# Configure a "tag" for the title
answer_text.tag_configure("title", font=("Arial", 16, "bold"), spacing3=10)

# --- 3. Bottom Frame (Contact Button) ---
bottom_frame = ttk.Frame(root)
bottom_frame.pack(fill="x", padx=10, pady=5)

contact_button = ttk.Button(bottom_frame, text="Contact Support", command=contact_support)
contact_button.pack(side="right", padx=10, pady=5, ipadx=10)

# Add a "Clear Search" button
clear_search_button = ttk.Button(bottom_frame, text="Clear Search", command=clear_search)
clear_search_button.pack(side="left", padx=10, pady=5)

# --- Start the Application ---
populate_tree() # Fill the tree with all topics at the start
root.mainloop()