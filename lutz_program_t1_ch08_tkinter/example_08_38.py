#!/usr/bin/env python
"""
Изображения. Объект Canvas

Canvas – универсальные поверхности для вывода графики.
Размеры кнопок автоматически изменяются в соответствии с размерами изображений,
холсты свои размеры не изменяют (потому что в холсты можно добавлять объекты).

"""
from tkinter import *

gifdir = "D:/Python/lutz/Programming_Python/PP4E-Examples-1.4/Examples/PP4E/Gui/gifs/"

win = Tk()
img = PhotoImage(file=gifdir + "ora-lp4e.gif")
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2, 2, image=img, anchor=NW)            # координаты x, y
win.mainloop()
