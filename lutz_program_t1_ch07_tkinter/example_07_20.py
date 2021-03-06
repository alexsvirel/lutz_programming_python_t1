"""
сценарий выводит окно с единственной кнопкой

При нажатии кнопки вызывается связанный метод self.message, который выводит сообщение в stdout.
Атрибут self.data (в данном случае простой счетчик) сохраняет информацию о состоянии
между нажатиями кнопки.

При создании подкласса, наследующего класс Frame, этот класс становится охватывающим контекстом
графического интерфейса:

•• Виджеты добавляются путем прикрепления объектов к self, экзем-
пляру подкласса контейнера Frame (например, Button).

•• Обработчики событий регистрируются как связанные методы объ-
екта self, вследствие чего вызовы направляются обратно в реализа-
цию класса (например, self.message).

•• Информация о состоянии сохраняется между событиями путем при-
своения атрибутам объекта self и доступна всем обработчикам собы-
тий в классе (например, self.data).

•• Легко можно создать несколько экземпляров такого компонента
графического интерфейса, даже внутри одного и того же процесса,
потому что каждый экземпляр класса является отдельным про-
странством имен.

•• Классы обладают естественной возможностью настройки благодаря
возможности наследования и композиции.
"""
from tkinter import *


class Hello(Frame):  # Расширенная версия класса Frame
    def __init__(self, parent=None):
        Frame.__init__(self, parent)  # вызвать метод __init__ суперкласса
        self.pack()
        self.data = 42
        self.make_widgets()  # прикрепить виджеты к себе

    def make_widgets(self):
        widget = Button(self, text='Hello frame world', command=self.message)
        widget.pack(side=LEFT)

    def message(self):
        self.data += 1
        print('Hello frame world %s' % self.data)


if __name__ == '__main__':
    Hello().mainloop()
