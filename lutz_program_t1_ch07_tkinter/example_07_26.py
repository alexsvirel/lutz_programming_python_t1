"""
пример "решения" ошибок при использовании автономного класса

импортирование расширенной версии класса HelloPackage из модуля example_07_24
"""
from tkinter import *
import example_07_24


class HelloPackage(example_07_24.HelloPackage):
    def __getattr__(self, name):
        return getattr(self.top, name)  # передать вызов настоящему виджету


if __name__ == '__main__':
    HelloPackage().mainloop()  # вызывает __getattr__
