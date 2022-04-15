"""
демонстрируется специализированный подкласс класса Frame, который прикрепляет экземпляр
класса Hello более объектно-ориентированным способом.

в качестве обработчика события добавленной кнопки он регистрирует метод self.quit,
который является стандартным методом quit виджетов, унаследованным от Frame.

окно демонстрирует действие двух классов Python:
 – виджет встроенного компонента справа (оригинальная кнопка Hello)
 - графические элементы контейнера слева
"""
from tkinter import *
from example_07_20 import Hello


class HelloContainer(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.makeWidgets()

    def makeWidgets(self):
        Hello(self).pack(side=RIGHT)  # прикрепить объект класса Руддщ к себе
        Button(self, text='Attach', command=self.quit).pack(side=LEFT)


if __name__ == '__main__':
    HelloContainer().mainloop()
