"""
расширяем класс Hello, а не просто прикрепляем его

для этоо переопределяем некоторые его методы в новом подклассе, который сам
станет специализированным виджетом Frame.

Метод make_widgets этого подкласса сначала создает виджеты обращением к методу суперкласса,
а затем добавляет справа вторую кнопку Extend
"""
from tkinter import *
from example_07_20 import Hello


class HelloExtender(Hello):
    def make_widgets(self):  # расширение метода
        Hello.make_widgets(self)
        Button(self, text='Extend', command=self.quit).pack(side=RIGHT)

    def message(self):
        print('hello', self.data)  # переопределение метода


if __name__ == '__main__':
    HelloExtender().mainloop()
