# Calculator-

Main Class: Calculator
The Calculator class creates the calculator application. It manages the graphical user interface (GUI) and logic for basic arithmetic operations.

Initialization (__init__)
Window Setup:

master: The main window (Tkinter root).
master.title("Calculator"): Sets the title of the window.
master.geometry("470x450"): Defines the size of the window.
master.configure(bg='black'): Sets the background color to black for a modern look.
Display:

A large text entry field (self.display) is created for user input and displaying results.
The display uses:
width=20: Sets the display size.
font=('Arial', 24): Sets the font style and size.
justify='right': Aligns text to the right.
bg='black', fg='white': Colors the background black and text white.
Resizable Layout:

The grid layout system is used, where:
master.grid_rowconfigure(0, weight=1) ensures the display expands.
Columns (0 to 3) are configured to resize dynamically.
Buttons
Button Definitions:

A list of buttons (buttons) contains tuples:
First element: The button label (e.g., '7', '+', '=').
Second element: The button color.
Button Creation:

A loop iterates over the buttons list, creating buttons with:
text=button: Label displayed on the button.
command=cmd: Calls self.click() when the button is clicked.
bg=color, fg='black': Background and text colors.
width=10, height=3, font=('Arial', 12): Size and style.
Buttons are placed in a grid layout (grid(row=row, column=col)), advancing to the next row after 4 columns.
Reset Button:

A "Reset" button is added at the bottom to clear the display:
command=self.reset: Links to the reset() method.
Button Click Handling (click)
The click() method handles button actions:

= Button:
Evaluates the expression in the display using eval().
If successful, replaces the display content with the result.
If there's an error (e.g., invalid input), it shows "Error".
Other Buttons:
Appends the button's label (e.g., '7', '+', etc.) to the display.
Reset (reset)
The reset() method clears the display (self.display.delete(0, tk.END)), effectively resetting the calculator.

Main Program Execution
Create Tkinter Window (root = tk.Tk()):
Initializes the main application window.
Instantiate Calculator:
The Calculator class is instantiated with root as the parent window.
Run the Application (root.mainloop()):
Starts the Tkinter event loop, keeping the window open and interactive.
How the Calculator Works
Input:
Users can click buttons to enter numbers and operators (e.g., 7, +, 3).
These inputs are displayed in the Entry widget.
Operations:
Pressing = evaluates the inputted expression and displays the result.
Example:
Input: 7+3
Output: 10
Reset:
Clicking "Reset" clears the display, allowing a fresh start.
Features
Resizable Layout: Buttons and the display adapt to window resizing.
Stylized Buttons: Each button has a unique background color.
Error Handling: Displays "Error" for invalid expressions.
Modern Design: Black background, clean fonts, and responsive design.
