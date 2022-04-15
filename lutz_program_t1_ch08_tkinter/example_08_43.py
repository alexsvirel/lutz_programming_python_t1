"""
отображает изображение с помощью альтернативного объекта из пакета PIL
поддерживает множество форматов изображений;
"""
import os, sys
from tkinter import *
from PIL.ImageTk import PhotoImage      # <== использовать альтернативный класс из PIL,
                                        # остальной код примера как в example_08_42

imgdir = 'D:/Python/Lutz/Programming_Python/PP4E-Examples-1.4/Examples/PP4E/Gui/PIL/images'
imgfile = 'florida-2009-1.jpg'

if len(sys.argv) > 1:                   # аргумент командной строки задан?
    imgfile = sys.argv[1]

imgpath = os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
imgobj = PhotoImage(file=imgpath)
Label(win, image=imgobj).pack()         # прикрепить к метке Label
print(imgobj.width(), imgobj.height())  # вывести размеры в пикселях
win.mainloop()
