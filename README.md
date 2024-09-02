Project Summary: Password Generator Application
Objective: Create a graphical user interface (GUI) application using Tkinter in Python that generates passwords based on user-selected criteria. The application allows users to specify the complexity and length of the password.

Features:

Password Generation:

Weak Password: Consists of only lowercase letters.
Medium Password: Consists of lowercase and uppercase letters.
Strong Password: Consists of lowercase letters, uppercase letters, digits, and special characters.
User Inputs:

Password Length: Users can specify the desired length of the password (between 5 and 18 characters) using a Spinbox.
Widgets:

Labels: Display static text such as 'Password Generator' and 'Password Length'.
Radio Buttons: Allow users to select the password complexity level (Weak, Medium, Strong).
Spinbox: Enables users to select the length of the password.
Button: Triggers password generation based on the selected criteria.
Entry Field: Displays the generated password.
Layout:

Centering: The application window is centered on the screen for a better user experience.
Packing: Widgets are arranged vertically with padding to ensure a clean and organized layout.
Functionality:

Password Generation Logic: Uses the random.sample method to generate passwords based on the selected criteria and length.
Centering Function: Calculates the position to place the window in the center of the screen.
Code Summary:

Imports: Tkinter for GUI, string for character sets, and random for generating random selections.
generator Function: Generates a password based on user-selected complexity and length, and displays it in the Entry field.
center_window Function: Centers the application window on the screen.
GUI Setup: Creates and configures the main window, adds widgets (labels, radio buttons, spinbox, button, entry field), and runs the Tkinter event loop to keep the window open.
This project provides a functional and user-friendly application for generating passwords with varying levels of complexity and length, making it a practical tool for enhancing password security.
