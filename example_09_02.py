"""
Повторно использовать функцию создания меню в разных окнах
"""
from tkinter import *

from example_09_01 import makemenu  # импортируем функцию создания меню для повторного использования

root = Tk()
for i in range(3):      # три всплывающих окна с меню
    win = Toplevel(root)
    makemenu(win)
    Label(win, bg='black', height=5, width=25).pack(expand=YES, fill=BOTH)
Button(root, text='Bye', command=root.quit).pack()
root.mainloop()
