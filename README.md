Password Strength Checker
A simple Python application for checking password strength. This project includes both a command-line interface and a graphical user interface built with Tkinter.
Features

Checks if passwords are at least 8 characters long
Verifies the presence of uppercase letters
Verifies the presence of lowercase letters
Verifies the presence of numbers
Verifies the presence of special characters
Provides clear feedback on password strength
GUI interface with show/hide password option

Requirements

Python 3.x
No additional libraries required (uses only standard libraries)

How to Use
Command Line Interface
Run the command-line version:
Copypython password_checker.py
This will prompt you to enter a password and will display feedback on its strength.
Graphical User Interface
Run the GUI version:
Copypython password_checker_gui.py
The GUI provides:

A text field to enter your password (hidden by default)
A checkbox to show/hide the password
A button to check the password strength
Visual feedback on password strength (green for strong, red for weak)

How It Works
The password checker evaluates passwords based on multiple criteria:

Length: Passwords must be at least 8 characters long
Character variety: Passwords must include:

At least one uppercase letter
At least one lowercase letter
At least one digit
At least one special character (!, @, #, $, etc.)



Project Structure

password_checker.py - Command-line interface
password_checker_gui.py - Graphical user interface

Future Improvements
Some possible enhancements for the future:

Add a strength meter (weak, medium, strong, very strong)
Check for common passwords against a database
Add password generation capabilities
Detect keyboard patterns (e.g., "qwerty")
Implement password storage with encryption

Author
Created by Samuel G.
