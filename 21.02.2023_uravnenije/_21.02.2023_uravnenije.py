from tkinter import *
from math import sqrt

def solver(a, b, c):
    D = b * b - 4 * a * c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x1 = (-b - sqrt(D)) / (2 * a)
        text = "D = %s \n x1 = %s \n x2 = %s \n" % (D, x1, x2)
    else:
        text = "D = %s \n" "Это уравнение не имеет корней" % D
    return text

def inserter(value):
    output.delete("0.0", END)
    output.insert("0.0", value)



def handler():
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(solver(a_val, b_val, c_val))
    except ValueError:
        inserter("Убедитесь, что ввели 3 числа")
root = Tk()
root.title("Решение квадратного уравнения")
root.geometry("420x200+300+300")
root.resizable(width=False, height=False)
f_top = Frame(root)
f_bot = Frame(root)
f_top.pack()
f_bot.pack()
a = Entry(f_top, width=5, font="Arial 15")
a.pack(side=LEFT, pady=10, padx=10)
a_lab = Label(f_top, text="x**2+", font="Arial 15").pack(side=LEFT, pady=10)
b = Entry(f_top, width=5, font="Arial 15")
b.pack(side=LEFT, pady=10)
b_lab = Label(f_top, text="x +", font="Arial 15").pack(side=LEFT, pady=10)
c = Entry(f_top, width=5, font="Arial 15")
c.pack(side=LEFT, pady=10)
c_lab = Label(f_top, text="= 0", font="Arial 15").pack(side=LEFT, pady=10)
btn = Button(f_top, text="Решить", font="Arial 12 bold", command=handler).pack(side=LEFT, pady=10, padx=10)
output = Text(f_bot, bg="yellow", fg="lime", font="Arial 12")
output.pack(expand=1, fill=BOTH, side=LEFT)


root.mainloop()

