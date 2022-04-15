"""
обобщенный метод __call__ класса фактически замещает связанный метод
Объекты экземпляров классов в Python могут вызываться как функции, если
они наследуют метод __call__ для перехвата этой операции,
поэтому их можно использовать в качестве обработчиков событий.
В примере экземпляр класса HelloCallable, зарегистрированный в command,
вызывается как обычная функция – Python вызовет его метод __call__ для обработки
операции вызова, выполняемой в tkinter при нажатии кнопки.
"""
import sys
from tkinter import *


class HelloCallable:
    def __init__(self):
        self.msg = 'Hello __call__ world'

    def __call__(self):  # __call__ вызывается при обращении к объектуу класса как к функции
        print(self.msg)
        sys.exit()


widget = Button(None, text='Hello event world', command=HelloCallable())
widget.pack()
widget.mainloop()
