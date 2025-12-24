import tkinter as tk
from tkinter import messagebox, filedialog

# Function to create a new file (clears the text area)
def new_file():
    text.delete(1.0, tk.END)  # Deletes everything from line 1, character 0 to the end

# Function to open an existing text file
def open_file():
    # Ask user to choose a file to open (only text or any file type)
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        # Open the selected file in read mode
        with open(file_path, 'r') as file:
            content = file.read()              # Read file contents
            text.delete(1.0, tk.END)           # Clear current text area
            text.insert(tk.END, content)       # Insert the read content into the text widget

# Function to save current text into a file
def save_file():
    # Ask user for save location and filename
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", 
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        # Open the file in write mode and save content
        with open(file_path, 'w') as file:
            content = text.get(1.0, tk.END)    # Get all text from the text widget
            file.write(content)                # Write content into file
            messagebox.showinfo("Save File", "File saved successfully!")  # Confirmation message

# ------------------ Main Window ------------------
root = tk.Tk()
root.title("Simple Text Editor")       # Set window title
root.geometry("600x400")               # Set window size

# ------------------ Menu Bar ------------------
menu = tk.Menu(root)                   # Create a main menu bar
root.config(menu=menu)                 # Attach menu bar to window

file_menu = tk.Menu(menu)              # Create 'File' dropdown menu
menu.add_cascade(label="File", menu=file_menu)  # Add File menu to the menu bar

# Add options inside 'File' menu
file_menu.add_command(label="New", command=new_file)     # New File option
file_menu.add_command(label="Open", command=open_file)   # Open File option
file_menu.add_command(label="Save", command=save_file)   # Save File option
file_menu.add_separator()                                # Add separator line
file_menu.add_command(label="Exit", command=root.quit)   # Exit option

# ------------------ Text Area ------------------
# Create a text widget for writing/editing text
text = tk.Text(
    root, 
    wrap=tk.WORD,                     # Wrap text by word (not letter)
    font=("Arial", 20),               # Font style and size
    fg="white",                       # Text color
    bg="black",                       # Background color
    insertbackground="white"          # Cursor color (so it's visible on dark background)
)
text.pack(expand=1, fill=tk.BOTH)      # Expand text area to fill the entire window

# ------------------ Run the App ------------------
root.mainloop()                        # Start the Tkinter event loop
