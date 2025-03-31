import string
import tkinter as tk
from tkinter import ttk

def check_password_strength(password):
    if len(password) < 8:
        return "Weak password: Must be at least 8 characters long.", "red"
    
    # Check for uppercase, lowercase, digits, and special characters
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    # Check if all conditions are met
    if has_upper and has_lower and has_digit and has_special:
        return "Strong password!", "green"
    else:
        return "Weak password: Try using uppercase, lowercase, numbers, and special characters.", "red"

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")

# Create a main frame
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

# Create the header label
header_label = ttk.Label(main_frame, text="Password Strength Checker", font=("Arial", 16, "bold"))
header_label.pack(pady=(0, 20))

# Create the password label and entry
password_label = ttk.Label(main_frame, text="Enter your password:")
password_label.pack(anchor="w")

password_entry = ttk.Entry(main_frame, width=30, show="•")
password_entry.pack(pady=(5, 15), fill="x")
password_entry.focus()

# Result label to show password strength
result_label = ttk.Label(main_frame, text="")
result_label.pack(pady=10)

# Function to check password
def check_password():
    password = password_entry.get()
    result, color = check_password_strength(password)
    result_label.config(text=result, foreground=color)

# Show password function
def toggle_password():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="•")

# Create a check button for showing password
show_password_var = tk.BooleanVar()
show_password_cb = ttk.Checkbutton(
    main_frame, 
    text="Show password", 
    variable=show_password_var,
    command=toggle_password
)
show_password_cb.pack(anchor="w")

# Button to check password
check_button = ttk.Button(main_frame, text="Check Strength", command=check_password)
check_button.pack(pady=10)

# Bind Enter key to check password
root.bind("<Return>", lambda event: check_password())

# Start the main event loop
root.mainloop()
