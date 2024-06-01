import tkinter as tk

def button_click(symbol):
    if symbol == "=":
        try:
            result = str(eval(display.get()))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif symbol == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, symbol)

root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the calculation
display = tk.Entry(root, width=20, font=("Arial", 18))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button labels
button_labels = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create buttons and bind actions
row = 1
col = 0
for label in button_labels:
    if col == 4:
        col = 0
        row += 1
    tk.Button(root, text=label, width=5, font=("Arial", 14),
              command=lambda l=label: button_click(l)).grid(row=row, column=col, padx=5, pady=5)
    col += 1

root.mainloop()
