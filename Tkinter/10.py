import tkinter as tk

def evaluate_expression(label_result, expression):
    try:
        # Tokenize the expression
        tokens = expression.replace(' ', '')
        num = ''
        stack = []
        last_operator = '+'

        for char in tokens:
            if char.isdigit() or char == '.':
                num += char  # Build the number
            else:
                if num:
                    # Convert to float and apply the last operator
                    if last_operator == '+':
                        stack.append(float(num))
                    elif last_operator == '-':
                        stack.append(-float(num))
                    elif last_operator == '*':
                        stack[-1] *= float(num)
                    elif last_operator == '/':
                        stack[-1] /= float(num)
                
                # Reset num and update the last operator
                num = ''
                last_operator = char

        # Handle the last number
        if num:
            if last_operator == '+':
                stack.append(float(num))
            elif last_operator == '-':
                stack.append(-float(num))
            elif last_operator == '*':
                stack[-1] *= float(num)
            elif last_operator == '/':
                stack[-1] /= float(num)

        # Calculate the final result
        result = sum(stack)
        label_result.config(text="Result: %.2f" % result)

    except Exception as e:
        label_result.config(text="Error: Invalid input")

def button_click(value):
    current_text = entry.get()
    if value == '=':
        evaluate_expression(labelResult, current_text)
    elif value == 'C':
        entry.delete(0, tk.END)  # Clear the entry field
        labelResult.config(text="")
    else:
        entry.insert(tk.END, value)  # Append the clicked button value to the entry

# Create the main window
root = tk.Tk()
root.geometry('300x400')
root.title('Calculator')

# Create the display for results
labelResult = tk.Label(root, text="", font=('Helvetica', 16))
labelResult.grid(row=0, column=0, columnspan=4)

# Create an entry field for input
entry = tk.Entry(root, font=('Helvetica', 16))
entry.grid(row=1, column=0, columnspan=4)

# Create buttons for numbers and operations
buttons = [
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('/', 3, 3),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('*', 4, 3),
    ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('-', 5, 3),
    ('0', 6, 0), ('C', 6, 1), ('=', 6, 2), ('+', 6, 3)
]

# Create buttons dynamically
for (text, row, column) in buttons:
    btn = tk.Button(root, text=text, font=('Helvetica', 16),
                    command=lambda value=text: button_click(value))
    btn.grid(row=row, column=column, sticky='nsew')

# Configure grid weights for resizing
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Start the main loop
root.mainloop()