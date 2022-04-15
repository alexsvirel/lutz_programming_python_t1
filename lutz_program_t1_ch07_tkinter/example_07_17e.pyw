"""
используем параметр anchor размещения графических элементов в отведенной для них области

Параметр anchor принимает константы из библиотеки tkinter, указывающие восемь направлений
(N, NE, NW, S и так далее), или константу CENTER

за основу кода взят код из примера example_07_17b.pyw
кнопке "Hello" добавлен параметр anchor с константой N - кнопка прилипка к северу (верхунему краю)
"""
from tkinter import *


def greeting():
    print('Hello stdout world...')


win = Frame()
win.pack()
Button(win, text='Hello', command=greeting).pack(side=LEFT, anchor=N)
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT)

win.mainloop()
