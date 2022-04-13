#!/usr/local/bin/python
"""
Окна с меню и панелью инструментов

Помимо меню, отображаемого в верхней части, окна часто содержат ряд кнопок в нижней части.
Этот нижний ряд кнопок называют панелью инструментов, и он нередко содержит кнопки для вы-
полнения наиболее часто используемых операций, присутствующих в главном меню.
Добавить в окно панель инструментов достаточно просто: нужно прикрепить кнопки (и другие
виджеты) к фрейму, прикрепить фрейм к нижней границе окна и определить для него возможность
растягивания только в горизонтальном направлении. Нужно следить, чтобы панели инструментов
и строки меню, основанные на фреймах, прикреплялись раньше других виджетов, чтобы при сжатии
окна сначала обрезались виджеты, находящиеся в середине экрана, – желательно, чтобы панели
инструментов и полосы меню имели приоритет перед другими виджетами.

Пример демонстрирует также:
- как добавлять изображения в пункты меню (присвоить атрибуту image ссылку на объект PhotoImage)
- как делать пункты меню недоступными для выбора, изображая их в серых тонах (вызвать метод меню
  entryconfig, передав ему индекс отключаемого пункта; отсчет начинается с 1)
- изменяет форму указателя мыши над панелью инструментов

Объекты PhotoImage сохраняются в виде списка – в отличие от других виджетов, они будут утеряны,
если не сохранить ссылки на них.
"""
# """
from tkinter import *  # импортировать базовый набор виджетов
from tkinter.messagebox import *  # импортировать стандартные диалоги


class NewMenuDemo(Frame):  # расширенный фрейм
    def __init__(self, parent=None):  # прикрепляется к корневому окну?
        Frame.__init__(self, parent)  # вызвать метод суперкласса
        self.pack(expand=YES, fill=BOTH)
        self.createWidgets()  # прикрепить фреймы/виджеты
        self.master.title('Toolbars and Menus')  # для менеджера окон
        self.master.iconname('tkpython')  # текст метки при свертывании

    def createWidgets(self):
        self.makeMenuBar()
        self.makeToolBar()
        L = Label(self, text='Menu and Toolbar Demo')
        L.config(relief=SUNKEN, width=40, height=10, bg='white')
        L.pack(expand=YES, fill=BOTH)

    def makeToolBar(self):
        toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
        toolbar.pack(side=BOTTOM, fill=X)
        Button(toolbar, text='Quit', command=self.quit).pack(side=RIGHT)
        Button(toolbar, text='Hello', command=self.greeting).pack(side=LEFT)

    def makeMenuBar(self):
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)  # master=окно верхнего уровня
        self.fileMenu()
        self.editMenu()
        self.imageMenu()

    def fileMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='Open...', command=self.notdone)
        pulldown.add_command(label='Quit', command=self.quit)
        self.menubar.add_cascade(label='File', underline=0, menu=pulldown)

    def editMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='Paste', command=self.notdone)
        pulldown.add_command(label='Spam', command=self.greeting)
        pulldown.add_separator()
        pulldown.add_command(label='Delete', command=self.greeting)
        pulldown.entryconfig(4, state=DISABLED)
        self.menubar.add_cascade(label='Edit', underline=0, menu=pulldown)

    def imageMenu(self):
        photoFiles = ('ora-lp4e.gif', 'pythonPowered.gif', 'python_conf_ora.gif')
        pulldown = Menu(self.menubar)
        self.photoObjs = []
        for file in photoFiles:
            img = PhotoImage(file='../../PP4E-Examples-1.4/Examples/PP4E/Gui/gifs/' + file)
            pulldown.add_command(image=img, command=self.notdone)
            self.photoObjs.append(img)  # сохранить ссылку
        self.menubar.add_cascade(label='Image', underline=0, menu=pulldown)

    def greeting(self):
        showinfo('greeting', 'Greetings')

    def notdone(self):
        showerror('Not implemented', 'Not yet available')

    def quit(self):
        if askyesno('Verify quit', 'Are you sure you want to quit?'):
            Frame.quit(self)


if __name__ == '__main__':
    NewMenuDemo().mainloop()  # если запущен как самостоятельный сценарий
