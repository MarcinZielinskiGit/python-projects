'''
Prevouse verion had a bug- when you presed any of the operators
buttons (+, -, *, /, =) with empty entry field it was coming up with an error.
That's resolved now.
'''

from tkinter import *

root = Tk()
root.title('Calculator')
root.iconbitmap('calc.ico')


def get_entry():
    global first_number
    if entry.get() != '':
        first_number = float(entry.get())
        return first_number
    else:
        try:
            first_number = float(first_number)
        except:
            first_number = 0
        return first_number


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_clear():
    entry.delete(0, END)


def button_add():
    global math
    get_entry()
    math = 'addition'
    entry.delete(0, END)


def button_subtract():
    global math
    get_entry()
    math = 'subtraction'
    entry.delete(0, END)


def button_multiply():
    global math
    get_entry()
    math = 'multiplication'
    entry.delete(0, END)


def button_divide():
    global math
    get_entry()
    math = 'division'
    entry.delete(0, END)


def button_plusminus():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, '-' + str(current))


def button_equal():
    try:
        second_number = float(entry.get())
    except Exception:
        pass
    else:
        try:
            entry.delete(0, END)
            if math == 'addition':
                result = first_number + second_number
            elif math == 'subtraction':
                result = first_number - second_number
            elif math == 'multiplication':
                result = first_number * second_number
            elif math == 'division':
                result = first_number / second_number

            if result % 1 == 0:
                result = int(result)

            entry.insert(0, result)
        except:
            if second_number % 1 == 0:
                entry.insert(0, int(second_number))
            else:
                entry.insert(0, second_number)


# Entry box
entry = Entry(root, width=30, borderwidth=2, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define Button
button_1 = Button(root, text='1', width=10, height=3,
                  command=lambda: button_click(1))
button_2 = Button(root, text='2', width=10, height=3,
                  command=lambda: button_click(2))
button_3 = Button(root, text='3', width=10, height=3,
                  command=lambda: button_click(3))
button_4 = Button(root, text='4', width=10, height=3,
                  command=lambda: button_click(4))
button_5 = Button(root, text='5', width=10, height=3,
                  command=lambda: button_click(5))
button_6 = Button(root, text='6', width=10, height=3,
                  command=lambda: button_click(6))
button_7 = Button(root, text='7', width=10, height=3,
                  command=lambda: button_click(7))
button_8 = Button(root, text='8', width=10, height=3,
                  command=lambda: button_click(8))
button_9 = Button(root, text='9', width=10, height=3,
                  command=lambda: button_click(9))
button_0 = Button(root, text='0', width=10, height=3,
                  command=lambda: button_click(0))

button_plusminus = Button(root, text='+/-', width=10,
                          height=3, command=button_plusminus)
button_decimal = Button(root, text='.', width=10, height=3,
                        command=lambda: button_click('.'))
button_add = Button(root, text='+', width=10, height=3, command=button_add)
button_equal = Button(root, text='=', width=10, height=3, command=button_equal)
button_clear = Button(root, text='Clear', width=10,
                      height=3, command=button_clear)
button_subtract = Button(root, text='-', width=10,
                         height=3, command=button_subtract)
button_multiply = Button(root, text='*', width=10,
                         height=3, command=button_multiply)
button_divide = Button(root, text='/', width=10,
                       height=3, command=button_divide)

# Put the buttons in the grid
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=1)

button_plusminus.grid(row=5, column=0)
button_decimal.grid(row=5, column=2)

button_add.grid(row=4, column=3)
button_equal.grid(row=5, column=3)
button_clear.grid(row=1, column=0)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)

root.mainloop()
