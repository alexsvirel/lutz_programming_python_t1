"""
Таблица из меток и полей ввода, расположенных по сетке (grid).
"""
from tkinter import *

colors = ['white', 'red', 'orange', 'yellow', 'green', 'light blue', 'blue', 'brown', 'black']

r = 0
for c in colors:
    Label(text=c, relief=RIDGE, width=25).grid(row=r, column=0)
    Entry(bg=c, relief=SUNKEN, width=50).grid(row=r, column=1)
    r += 1

mainloop()
