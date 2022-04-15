"""
Cвязанный метод класса вместо функции или результата lambda-выражения.
Cвязанные методы класса прекрасно справляются с ролью обработчиков событий
в графических интерфейсах – они запоминают не только экземпляр, которому было послано событие,
но и связанный с ним метод, который должен быть вызван
"""
import sys
from tkinter import *


class HelloClass:
    def __init__(self):
        widget = Button(None, text='Hello event world', command=self.quit)
        widget.pack()

    def quit(self):
        print('Hello class method world')  # self.quit - связанный метод
        sys.exit()  # хранит пару self+quit


HelloClass()
mainloop()
