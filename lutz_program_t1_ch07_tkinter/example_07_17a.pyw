"""
изменен порядок создания метки и кнопок
Библиотека tkinter запоминает порядок добавления виджетов - виджет, добавленный первым,
всегда исчезает последним.

Поэтому сценарии могут заранее готовиться к сжатию окон, вызывая вначале метод pack для более
важных виджетов.

Например, при создании меню и панели инструментов в верхней и нижней части окна,
чтобы обеспечить их исчезновение при сжатии окна в последнюю очередь,
они добавляются первыми, перед теми компонентами, которые размещаются в середине.

Аналогично полосы прокрутки, содержащиеся в интерфейсах, обычно добавляются раньше,
чем прокручиваемые ими элементы (например, текстовые окна или списки), чтобы сохраняться
при сжатии окна.
"""
from tkinter import *


def greeting():
    print('Hello stdout world...')


win = Frame()
win.pack()
Button(win, text='Hello', command=greeting).pack(side=LEFT)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT)
Label(win, text='Hello container world').pack(side=TOP)

win.mainloop()