"""
реализация графического интерфейса - объединяет GuiMaker, GuiMixin и данный класс
"""
import sys
import os
from tkinter import *
from example_10_02 import *  # подмешиваемые методы: quit, spawn...
from example_10_03 import *  # фрейм плюс построение меню/панели инструментов


class Hello(GuiMixin, GuiMakerWindowMenu):  # или GuiMakerFrameMenu
    def start(self):
        self.hellos = 0
        self.master.title("Gui maker Demo")
        self.master.iconname("GuiMaker")

        def spawnme():
            self.spawn('example_10_04.py')  # отложеный вызов вместо lambda

        self.menuBar = [  # дерево: 3 раскр. меню
            ('File', 0,  # (раскр. меню)
             [('New...', 0, spawnme),
              ('Open...', 0, self.fileOpen),  # [список элементов меню]
              ('Quit', 0, self.quit)]  # метка,клавиша,обработчик
             ),

            ('Edit', 0,
             [('Cut', -1, self.notdone),  # без клавиши| обработчика
              ('Paste', -1, self.notdone),  # lambda:0 тоже можно
              'separator',  # добавить разделитель
              ('Stuff', -1,
               [('Clone', -1, self.clone),  # каскадное подменю
                ('More', -1, self.more)]
               ),
              ('Delete', -1, lambda: 0),
              [5]]  # отключить ‘delete’
             ),

            ('Play', 0,
             [('Hello', 0, self.greeting),
              ('Popup...', 0, self.dialog),
              ('Demos', 0,
               [('Toplevels', 0,
                 lambda: self.spawn(r'D:\Python\Lutz\Programming_Python\PP4E-Examples-1.4\Examples\PP4E\Gui\Tour'
                                    r'\toplevel2.py')),
                ('Frames', 0,
                 lambda: self.spawn(r'D:\Python\Lutz\Programming_Python\PP4E-Examples-1.4\Examples\PP4E\Gui\Tour'
                                    r'\demoAll-frm-ridge.py')),
                ('Images', 0,
                 lambda: self.spawn(r'D:\Python\Lutz\Programming_Python\PP4E-Examples-1.4\Examples\PP4E\Gui\Tour'
                                    r'\buttonpics.py')),
                ('Alarm', 0,
                 lambda: self.spawn(r'D:\Python\Lutz\Programming_Python\PP4E-Examples-1.4\Examples\PP4E\Gui\Tour'
                                    r'\alarm.py', wait=False)),
                ('Other...', - 1, self.pickDemo)]
               )]
             )]

        self.toolBar = [  # добавить 3 кнопки
            ('Quit', self.quit, dict(side=RIGHT)),  # или {'side': RIGHT}
            ('Hello', self.greeting, dict(side=LEFT)),
            ('Popup', self.dialog, dict(side=LEFT, expand=YES))]

    def makeWidgets(self):  # переопределить метод
        middle = Label(self, text='Hello maker world!',  # создания виджетов
                       width=40, height=10,  # в середине окна
                       relief=SUNKEN, cursor='pencil', bg='white')
        middle.pack(expand=YES, fill=BOTH)

    def greeting(self):
        self.hellos += 1
        if self.hellos % 3:
            print("hi")
        else:
            self.infobox("Three", 'HELLO!')  # каждый третий щелчок

    def dialog(self):
        button = self.question('OOPS!',
                               'You typed "rm *" ... continue?',  # старый стиль
                               'questhead', ('yes', 'no'))  # аргументы
        [lambda: None, self.quit][button]()  # игнорируются

    def fileOpen(self):
        pick = self.selectOpenFile(file='example_10_04.py')
        if pick:
            self.browser(pick)  # просмотр файла модуля или другого файла

    def more(self):
        new = Toplevel()
        Label(new, text='A new non - modal window').pack()
        Button(new, text='Quit', command=self.quit).pack(side=LEFT)
        Button(new, text='More', command=self.more).pack(side=RIGHT)

    def pickDemo(self):
        pick = self.selectOpenFile(dir='..')
        if pick:
            self.spawn(pick)  # запустить любую программу Python


if __name__ == '__main__':
    Hello().mainloop()  # создать, запустить
