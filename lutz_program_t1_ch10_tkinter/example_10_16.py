"""
Классы, инкапсулирующие интерфейсы верхнего уровня.

Позволяют создавать главные, всплывающие или присоединяемые окна;
Эти классы могут наследоваться непосредственно, смешиваться с другими классами или
вызываться непосредственно, без создания подклассов;
Должны подмешиваться после (то есть правее) более конкретных прикладных классов:
иначе подклассы будут получать методы (destroy, okayToQuit) из этих,
а не из прикладных классов, и лишатся возможности переопределить их.
"""

import glob
import os
from tkinter import Tk, Toplevel, Frame, YES, BOTH, RIDGE
from tkinter.messagebox import showinfo, askyesno


class _window:
    """
    подмешиваемый класс, используется классами главных и всплывающих окон
    """
    foundicon = None  # совместно используется всеми экземплярами
    iconpatt = '*.ico'  # может быть сброшен
    iconmine = 'py.ico'

    def configBorders(self, app, kind, iconfile):
        if not iconfile:  # ярлык не был передан?
            iconfile = self.findIcon()  # поиск в текущем каталоге и в каталоге модуля
        title = app
        if kind: title += ' - ' + kind
        self.title(title)  # на рамке окна
        self.iconname(app)  # при свертывании
        if iconfile:
            try:
                self.iconbitmap(iconfile)  # изображение ярлыка окна
            except:  # проблема с интерпретатором или платформой
                pass
        self.protocol('WM_DELETE_WINDOW', self.quit)  # не закрывать без подтверждения

    def findIcon(self):
        if _window.foundicon:  # ярлык уже найден?
            return _window.foundicon
        iconfile = None  # сначала искать в тек. каталоге
        iconshere = glob.glob(self.iconpatt)  # допускается только один
        if iconshere:  # удалить ярлык с красными буквами Tk
            iconfile = iconshere[0]
        else:  # поиск в каталоге модуля
            mymod = __import__(__name__)  # импортировать, получить каталог
            path = __name__.split('.')  # возможно, путь пакета
            for mod in path[1:]:  # по всему пути до конца
                mymod = getattr(mymod, mod)  # только самый первый
            mydir = os.path.dirname(mymod.__file__)
            myicon = os.path.join(mydir, self.iconmine)  # использовать myicon, а не tk
            if os.path.exists(myicon): iconfile = myicon
        _window.foundicon = iconfile  # не выполнять поиск вторично
        return iconfile


class MainWindow(Tk, _window):
    """
    главное окно верхнего уровня
    """

    def __init__(self, app, kind='', iconfile=None):
        self.findIcon()
        Tk.__init__(self)
        self.__app = app
        self.configBorders(app, kind, iconfile)

    def quit(self):
        if self.okayToQuit():  # потоки запущены?
            if askyesno(self.__app, 'Verify Quit Program?'):
                self.destroy()  # завершить приложение
        else:
            showinfo(self.__app, 'Quit not allowed')  # или в okayToQuit?

    def destroy(self):  # просто завершить
        Tk.quit(self)  # переопределить, если необходимо

    def okayToQuit(self):   # переопределить, если используются потоки выполнения
        return True


class PopupWindow(Toplevel, _window):
    """
    вторичное всплывающее окно
    """

    def __init__(self, app, kind='', iconfile=None):
        Toplevel.__init__(self)
        self.__app = app
        self.configBorders(app, kind, iconfile)

    def quit(self):  # переопределить, если потребуется изменить
        if askyesno(self.__app, 'Verify Quit Window?'):  # или вызвать destroy
            self.destroy()  # чтобы закрыть окно

    def destroy(self):  # просто закрыть окно
        Toplevel.destroy(self)  # переопределить, если необходимо


class QuietPopupWindow(PopupWindow):
    def quit(self):
        self.destroy()  # закрывать без предупреждения


class ComponentWindow(Frame):
    """
    при присоединении к другим интерфейсам
    """

    def __init__(self, parent):  # если не фрейм
        Frame.__init__(self, parent)  # предоставить контейнер
        self.pack(expand=YES, fill=BOTH)
        self.config(relief=RIDGE, border=2)  # перенастроить при необходимости

    def quit(self):
        showinfo('Quit', 'Not supported in attachment mode')

    # destroy из фрейма: просто удалить фрейм
    # переопределить, если необходимо
