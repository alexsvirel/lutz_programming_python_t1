"""
Автономные классы-контейнеры

Большая часть преимуществ от создания компонентов на основе классов может быть получена
в результате создания автономных классов, не являющихся производными от класса Frame или
других классов виджетов из библиотеки tkinter.

В примере класс HelloPackage не является подклассом виджета Frame. Он вообще не является подклассом
какого-либо виджета – он служит только для создания пространства имен, хранящего действительные
объекты виджетов и информацию о состоянии.

По этой причине виджеты прикрепляются к объекту self.top (встроенному фрейму Frame), а не к self.
И все ссылки на объект как на виджет должны передаваться вниз, встроенному фрейму, как, например,
вызов метода top.mainloop для запуска интерфейса в конце сценария.
"""
from tkinter import *


class HelloPackage:
    def __init__(self, parent=None):
        self.top = Frame(parent)
        self.top.pack()
        self.data = 0  # атрибут self.data сохраняет информацию о со стоянии между событиями
        self.make_widgets()  # прикрепить виджеты к self.top

    def make_widgets(self):
        Button(self.top, text='Bye', command=self.top.quit).pack(side=LEFT)
        Button(self.top, text='Hye', command=self.message).pack(side=RIGHT)

    def message(self):
        self.data += 1
        print('Hello number', self.data)


if __name__ == '__main__':
    HelloPackage().top.mainloop()
