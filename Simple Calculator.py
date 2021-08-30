from tkinter import *

# Calculator's logic

num1 = -1
num2 = -1
result = 0 
selected_operand = ""

def num_button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))

def operand_button_click(operand):
    global selected_operand
    global num1
    global num2

    selected_operand = operand    

    if "." in e.get():
        num1 = float(e.get())
    else:
        num1 = int(e.get())

    clear_button_click()

def equal_button_click():
    global num1
    global num2
    global selected_operand
    
    if "." in e.get():
        num2 = float(e.get())
    else:
        num2 = int(e.get())

    if selected_operand == "+":
        result = num1 + num2
    elif selected_operand == "-":
        result = num1 - num2
    elif selected_operand == "*":
        result = num1 * num2
    elif selected_operand == "/":
        result = num1 / num2

    clear_button_click()
    e.insert(0, result)

def clear_button_click():
    e.delete(0, END)

# GUI

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5, justify="right", font="Digital-7\ Mono 20", state="normal")
e.grid(row=0, column=0, columnspan=3,ipady=5, padx=5, pady=5)

# Create buttons 0-9
button_0 = Button(root, text=str(0), padx=55, pady=20, font="Digital-7\ Mono 20", command=lambda: num_button_click(0))
button_1 = Button(root, text=str(1), padx=55, pady=20, font="Digital-7\ Mono 20", command=lambda: num_button_click(1))
button_2 = Button(root, text=str(2), padx=55, pady=20, font="Digital-7\ Mono 20", command=lambda: num_button_click(2))
button_3 = Button(root, text=str(3), padx=55, pady=20, font="Digital-7\ Mono 20", command=lambda: num_button_click(3))
button_4 = Button(root, text=str(4), padx=55, pady=20, font="Digital-7\ Mono 20", command=lambda: num_button_click(4))
button_5 = Button(root, text=str(5), padx=55, pady=20, font="Digital-7\ Mono 20", command=lambda: num_button_click(5))
button_6 = Button(root, text=str(6), padx=55, pady=20, font="Digital-7\ Mono 20", command=lambda: num_button_click(6))
button_7 = Button(root, text=str(7), padx=55, pady=20, font="Digital-7\ Mono 20", command=lambda: num_button_click(7))
button_8 = Button(root, text=str(8), padx=55, pady=20, font="Digital-7\ Mono 20", command=lambda: num_button_click(8))
button_9 = Button(root, text=str(9), padx=55, pady=20, font="Digital-7\ Mono 20", command=lambda: num_button_click(9))

# Create . button
button_dot = Button(root, text=".", padx=55, pady= 20, font="Digital-7\ Mono 20", command=lambda: num_button_click("."))

# Create = button
button_equal = Button(root, text="=", padx=55, pady= 20, font="Digital-7\ Mono 20", command=equal_button_click)

# Create buttons +, -, *, /
button_add = Button(root, text="+", padx=55, pady= 20, font="Digital-7\ Mono 20", command=lambda: operand_button_click("+"))
button_substract = Button(root, text="-", padx=55, pady= 20, font="Digital-7\ Mono 20", command=lambda: operand_button_click("-"))
button_multiply = Button(root, text="*", padx=55, pady= 20, font="Digital-7\ Mono 20", command=lambda: operand_button_click("*"))
button_divide = Button(root, text="/", padx=55, pady= 20, font="Digital-7\ Mono 20", command=lambda: operand_button_click("/"))

# Create "CLEAR" button
button_clear = Button(root, text="CLEAR", padx=38, pady= 20, font="Digital-7\ Mono 16", command=clear_button_click)

# Place the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_dot.grid(row=4, column=1)
button_equal.grid(row=4, column=2)

button_add.grid(row=4, column=3) # +
button_substract.grid(row=3, column=3) # -
button_multiply.grid(row=2, column=3) # *
button_divide.grid(row=1, column=3) # /
button_clear.grid(row=0, column=3) # CLEAR


root.mainloop()