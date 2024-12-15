import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("470x450")  # Increased height to accommodate the larger display
        master.configure(bg='black')  # Set background color to black

        # Create larger display
        self.display = tk.Entry(master, width=20, justify='right', font=('Arial', 24), bg='black', fg='white')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky='nsew')  # Increased padding and made sticky

        # Configure row and column to expand
        master.grid_rowconfigure(0, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

        # Create buttons with colors
        buttons = [
            ('7', '#FF6B6B'), ('8', '#4ECDC4'), ('9', '#45B7D1'), ('/', '#FFA07A'),
            ('4', '#98D8C8'), ('5', '#F67280'), ('6', '#C06C84'), ('*', '#6C5B7B'),
            ('1', '#F8B195'), ('2', '#F67280'), ('3', '#C06C84'), ('-', '#6C5B7B'),
            ('0', '#A8E6CF'), ('.', '#DCEDC1'), ('=', '#FFD3B6'), ('+', '#FFAAA5')
        ]

        # Add buttons to the grid
        row = 1
        col = 0
        for button, color in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(master, text=button, command=cmd, width=10, height=3, font=('Arial', 12),
                      bg=color, fg='black').grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Add reset button
        reset_button = tk.Button(master, text="Reset", command=self.reset, width=42, height=2, font=('Arial', 12),
                                 bg='#FF4136', fg='white')
        reset_button.grid(row=row, column=0, columnspan=4, padx=5, pady=5)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, key)

    def reset(self):
        self.display.delete(0, tk.END)

# Create the main window
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
