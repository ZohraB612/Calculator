# Import packages
import tkinter as tk

def on_click(button_value):
    if button_value == '=':
        calculate_result()
    else:
        current_text = entry.get()
        new_text = current_text + str(button_value)
        entry.delete(0, tk.END)
        entry.insert(0, new_text)

def clear_entry():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Let's create the main window
app = tk.Tk()
app.title("Basic Calculator")

# Use entry widget to display the inputs and results
entry = tk.Entry(app, width=20, font=("Arial", 16), borderwidth=5, relief=tk.GROOVE)
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(app, text=button, width=5, height=2, command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(app, text="C", width=5, height=2, command=clear_entry).grid(row=row_val, column=0)

# Run the app
app.mainloop()
