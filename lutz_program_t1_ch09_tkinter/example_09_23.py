"""
Создание крупных таблиц с помощью grid

простая двухмерная таблица, в корневом окне Tk по умолчанию
"""
from tkinter import *

for i in range(10):
    for j in range(8):
        lab = Label(text='%d.%d' % (i, j), relief=RIDGE)
        lab.grid(row=i, column=j, sticky=NSEW)

mainloop()
