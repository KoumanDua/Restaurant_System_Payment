from tkinter import *

def calculator(parent):
    text_input = StringVar()
    operator = ""

    def btnClick(numbers):
        nonlocal operator
        operator += str(numbers)
        text_input.set(operator)

    def btnClearDisplay():
        nonlocal operator
        operator = ""
        text_input.set(operator)

    def btnEqual():
        nonlocal operator
        try:
            total = str(eval(operator))
            text_input.set(total)
        except:
            text_input.set("Error")
            operator = ""

    # Création du cadre pour la calculatrice
    calc_frame = Frame(parent)
    calc_frame.pack()

    Entry(calc_frame, borderwidth=30, font=("arial", 20, "bold"),
          insertwidth=4, background="light blue", justify="right",
          textvariable=text_input).grid(columnspan=4)

    Button(calc_frame, padx=59, pady=15, borderwidth=8, font=("arial", 20, "bold"),
           text="C", background="light blue", command=btnClearDisplay).grid(row=1, columnspan=2)
    Button(calc_frame, padx=19, pady=15, borderwidth=9, font=("arial", 20, "bold"),
           text="(", background="light blue", command=lambda: btnClick("(")).grid(row=1, column=2)
    Button(calc_frame, padx=19, pady=15, borderwidth=9, font=("arial", 20, "bold"),
           text=")", background="light blue", command=lambda: btnClick(")")).grid(row=1, column=3)

    buttons = [
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
        ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
    ]

    for (text, row, col) in buttons:
        action = btnEqual if text == '=' else lambda x=text: btnClick(x)
        Button(calc_frame, padx=19, pady=16, borderwidth=8, font=("arial", 20, "bold"),
               text=text, background="light blue", command=action).grid(row=row, column=col)
