"""
Два корневых окна

Чтобы закрыть только одно окно, вместо функции sys.exit, которая завершает работу всей программы,
вызывается метод destroy этого окна
"""
import tkinter
from tkinter import Tk, Button

tkinter.NoDefaultRoot()     # подавить создание корневого окна по умолчанию

win1 = Tk()                 # два независимых корневых окна
win2 = Tk()

Button(win1, text='spam', command=win1.destroy).pack()  # метод destroy закрывает только одно окно
Button(win2, text='SPAM', command=win2.destroy).pack()

win1.mainloop()

