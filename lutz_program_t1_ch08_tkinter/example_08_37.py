#!/usr/bin/env python
"""
Изображения. Объекты PhotoImage и BitmapImage.

В библиотеке tkinter графические изображения отображаются за счет создания независимых объектов
PhotoImage или BitmapImage и прикрепления их к другим виджетов путем установки атрибута image.
Кнопки, метки, холсты, текстовые виджеты и меню – все они могут выводить изображения,
связывая таким способом готовые графические объекты.
Объекты PhotoImage и BitmapImage просто загружают графические файлы и позволяют
прикреплять полученные изображения к другим типам виджетов.
Для иллюстрации сценарий в примере выводит картинку на кнопке.
"""
from tkinter import *

gifdir = "D:/Python/lutz/Programming_Python/PP4E-Examples-1.4/Examples/PP4E/Gui/gifs/"

win = Tk()
igm = PhotoImage(file=gifdir + "ora-pp.gif")
Button(win, image=igm).pack()
win.mainloop()
