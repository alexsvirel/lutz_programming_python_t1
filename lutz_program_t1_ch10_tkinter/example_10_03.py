"""
Расширенный Frame, автоматически создающий меню и панели инструментов в окне.

GuiMakerFrameMenu предназначен для встраивания компонентов (создает меню на основе фреймов).

GuiMakerWindowMenu предназначен для окон верхнего уровня (создает меню Tk8.0).

Пример древовидной структуры приводится в реализации самотестирования (и в PyEdit).
"""
import sys
from tkinter import *
from tkinter.messagebox import showinfo


class GuiMaker(Frame):
    """
    графический интерфейс
    класс GuiMaker выполняет обход структур с описанием меню и панели инструментов
    и создает соответствующие виджеты.
    """
    menuBar = []  # значения по умолчанию
    toolBar = []  # изменять при создании подклассов
    helpButton = True  # устанавливать в start()

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)  # растягиваемый фрейм
        self.start()  # в подклассе: установить меню/панель инструментов
        self.makeMenuBar()  # здесь: создать полосу меню
        self.makeToolBar()  # здесь: создать панель инструментов
        self.makeWidgets()  # в подклассе: добавить середину

    def makeMenuBar(self):
        """
        создает полосу меню вверху (реализация меню Tk8.0 приводится ниже)
        expand=no, fill=x, чтобы ширина оставалась постоянной
        """
        menubar = Frame(self, relief=RAISED, bd=2)
        menubar.pack(side=TOP, fill=X)

        for (name, key, items) in self.menuBar:
            mbutton = Menubutton(menubar, text=name, underline=key)
            mbutton.pack(side=LEFT)
            pulldown = Menu(mbutton)
            self.addMenuItems(pulldown, items)
            mbutton.config(menu=pulldown)

        if self.helpButton:
            Button(menubar, text='Help',
                   cursor='gumby', relief=FLAT, command=self.help).pack(side=RIGHT)

    def addMenuItems(self, menu, items):
        """
        добавить пункты меню
        """
        for item in items:  # сканировать список вложенных элементов
            if item == 'separator':  # строка: добавить разделитель
                menu.add_separator({})
            elif type(item) == list:  # список: неактивных элементов
                for num in item:
                    menu.entryconfig(num, state=DISABLED)
            elif type(item[2]) != list:
                menu.add_command(label=item[0],  # команда: метка
                                 underline=item[1],  # горячая клавиша
                                 command=item[2])  # обработчик: вызыв. объект
            else:
                pullover = Menu(menu)
                self.addMenuItems(pullover, item[2])  # подменю:
                menu.add_cascade(label=item[0],  # создать подменю
                                 underline=item[1],  # добавить каскад
                                 menu=pullover)

    def makeToolBar(self):
        """
        создает панель с кнопками внизу, если необходимо expand=no, fill=x,
        чтобы ширина оставалась постоянной можно добавить поддержку изображений:
        смотрите главу 9, для чего придется создать минатюры в формате FIF или
        использовать расширение PIL
        """
        if self.toolBar:
            toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
            toolbar.pack(side=BOTTOM, fill=X)
            for (name, action, where) in self.toolBar:
                Button(toolbar, text=name, command=action).pack(where)

    def makeWidgets(self):
        """
        "средняя" часть создается последней, поэтому меню/панель инструментов
        всегда остаются вверху/внизу и обрезаются в последнюю очередь;
        переопределите этот метод,
        для pack: прикрепляйте середину к любому краю;
        для grid: компонуйте середину по сетке во фрейме, который прикрепляется методом pack
        """
        name = Label(self, width=40, height=10, relief=SUNKEN, bg='white',
                     text=self.__class__.__name__, cursor='crosshair')
        name.pack(expand=YES, fill=BOTH, side=TOP)

    def help(self):
        """
        переопределите в подклассе
        :return:
        """
        showinfo('Help', 'Sorry, no help for ' + self.__class__.__name__)

    def start(self):
        """
        переопределите в подклассе: связать меню/панель инструментов с self
        :return:
        """
        pass


GuiMakerFrameMenu = GuiMaker  # используется для меню встраиваемых компонентов

##############################################################################
# Специализированная версия для полосы меню главного окна Tk 8.0
##############################################################################
class GuiMakerWindowMenu(GuiMaker):  # используется для меню окна верхнего уровня
    """
    Реализует меню окон верхнего уровня в стиле Tk 8.0, которые удобно использовать
    в самостоятельных программах и всплывающих окнах.
    """

    def makeMenuBar(self):
        """
        создает полосу меню вверху
        """
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        for (name, key, items) in self.menuBar:
            pulldown = Menu(menubar)
            self.addMenuItems(pulldown, items)
            menubar.add_cascade(label=name, underline=key, menu=pulldown)

        if self.helpButton:
            if sys.platform[:3] == 'win':
                menubar.add_command(label='Help', command=self.help)
            else:
                pulldown = Menu(menubar)  # Linux требуется настоящее меню
                pulldown.add_command(label='About', command=self.help)
                menubar.add_cascade(label='Help', menu=pulldown)


###############################################################################
# Реализация самотестирования, которая выполняется, если запустить модуль как
# самостоятельный сценарий: ‘python guimaker.py’
#
# В реализацию самотестирования включен простой пример структур данных,
# использованных для компоновки меню и панели инструментов:
#
# Шаблоны меню:
# Списки и вложенные подсписки кортежей (метка, горячая_клавиша, обработчик).
# Если обработчик является подсписком, а не функцией или методом, предполагается,
# что это каскадное подменю.
#
# Шаблоны панелей инструментов:
# Список кортежей (метка, обработчик, параметры_компоновки).
# Параметры компоновки определяются в виде словаря параметров, передаваемых
# методу pack виджета, – словарь можно записать в виде литерала {‘k’:v}
# или использовать вызов функции dict(k=v) с именованными аргументами.
# Метод pack принимает словари, однако словари можно трансформировать в именованные аргументы,
# используя синтаксис вызова func(**kargs). В данной реализации метки
# определяются как текст, но точно так же можно было бы реализовать поддержку
# изображений (смотрите раздел «BigGui: клиентская демонстрационная программа» ниже)
###############################################################################

if __name__ == '__main__':
    from example_10_02 import GuiMixin  # встроить метод help

    menuBar = [
        ('File', 0,
         [('Open', 0, lambda: 0),  # lambda:0 - пустая операция
          ('Quit', 0, sys.exit)]),  # здесь использовать sys, а не self
        ('Edit', 0,
         [('Cut', 0, lambda: 0),
          ('Paste', 0, lambda: 0)])]
    toolBar = [('Quit', sys.exit, {'side': LEFT})]


    class TestAppFrameMenu(GuiMixin, GuiMakerFrameMenu):
        def start(self):
            self.menuBar = menuBar
            self.toolBar = toolBar


    class TestAppWindowMenu(GuiMixin, GuiMakerWindowMenu):
        def start(self):
            self.menuBar = menuBar
            self.toolBar = toolBar


    class TestAppWindowMenuBasic(GuiMakerWindowMenu):
        def start(self):
            self.menuBar = menuBar
            self.toolBar = toolBar  # help из GuiMaker, а не из GuiMixin


    root = Tk()
    TestAppFrameMenu(Toplevel())
    TestAppWindowMenu(Toplevel())
    TestAppWindowMenuBasic(root)
    root.mainloop()
