from tkinter import *

root = Tk()
root.title("Basic calculator")

e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=5, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, f'{str(current)}{str(number)}')


def button_clear():
    e.delete(0, END)


def button_plus():
    first_number = e.get()
    global f_num
    global math
    math = "plus"
    f_num = float(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "plus":
        e.insert(0, f_num + float(second_number))
    if math == "minus":
        e.insert(0, f_num - float(second_number))
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "division":
        e.insert(0, f_num / float(second_number))
    if math == "rooting":
        e.insert(0, f_num ** 0.5)
    if math == "exponentiation":
        e.insert(0, f_num ** float(second_number))


def button_minus():
    first_number = e.get()
    global f_num
    global math
    math = "minus"
    f_num = float(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


def button_square_root():
    first_number = e.get()
    global f_num
    global math
    math = "rooting"
    f_num = float(first_number)
    e.delete(0, END)


def button_exponent():
    first_number = e.get()
    global f_num
    global math
    math = "exponentiation"
    f_num = float(first_number)
    e.delete(0, END)


def button_dot():
    current = e.get()
    e.delete(0, END)
    e.insert(0, f'{str(current)}.')


button_0 = Button(root, text="0", padx=20, pady=10, command=lambda: button_click(0))
button_1 = Button(root, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=20, pady=10, command=lambda: button_click(9))

button_dot = Button(root, text=".", padx=22, pady=10, command=button_dot)
button_plus = Button(root, text="+", padx=18, pady=10, command=button_plus)
button_minus = Button(root, text="-", padx=22, pady=10, command=button_minus)
button_multiply = Button(root, text="×", padx=19, pady=10, command=button_multiply)
button_divide = Button(root, text="÷", padx=19, pady=10, command=button_divide)
button_clear = Button(root, text="C", padx=20, pady=10, command=button_clear)
button_square_root = Button(root, text="√", padx=20, pady=10, command=button_square_root)
button_exponent = Button(root, text="^", padx=20, pady=10, command=button_exponent)
button_equal = Button(root, text="=", padx=47, pady=10, command=button_equal)

button_0.grid(row=4, column=0)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_dot.grid(row=4, column=1)
button_plus.grid(row=4, column=2)
button_minus.grid(row=1, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=3, column=3)
button_clear.grid(row=1, column=4)
button_square_root.grid(row=2, column=4)
button_exponent.grid(row=3, column=4)
button_equal.grid(row=4, column=3, columnspan=2)


root.mainloop()
