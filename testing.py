import tkinter as tk

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def clear():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry widget
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Create number buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for button_data in buttons:
    button_text, row, column = button_data
    button = tk.Button(window, text=button_text, width=7, height=3,
                       command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=column)

# Create the clear button
clear_button = tk.Button(window, text="C", width=7, height=3, command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Start the main event loop
window.mainloop()
