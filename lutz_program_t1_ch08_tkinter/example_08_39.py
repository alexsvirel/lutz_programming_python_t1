#!/usr/bin/env python
"""
Изображения. Имя файла с изображением в командной строке

при запуске из командной строки следует перейти в папку гда находится файл со скриптом
и в командной строке записать:
python example_08_39 путь_и_имя_файла_с_картинкой
"""
from sys import argv
from tkinter import *

gifdir = "D:/Python/lutz/Programming_Python/PP4E-Examples-1.4/Examples/PP4E/Gui/gifs/"

filename = argv[1] if len(argv) > 1 else 'ora-lp4e.gif'         # имя файла в командной строке

win = Tk()
img = PhotoImage(file=gifdir + filename)
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(), height=img.height())              # размер соответственно картинке
can.create_image(2, 2, image=img, anchor=NW)
win.mainloop()
