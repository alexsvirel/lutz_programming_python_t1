"""
Расположение кнопок (миниатюр) с фиксированным размером кнопок

Использует кнопки фиксированного размера для миниатюр, благодаря чему достигается
еще более стройное размещение;

Размеры определяются по объектам изображений, при этом предполагается,
что для всех миниатюр был установлен один и тот же максимальный размер;

По сути именно это и делают графические интерфейсы файловых менеджеров;
"""
import sys
import math

from tkinter import *
from PIL.ImageTk import PhotoImage

from example_08_45 import makeThumbs
from example_08_45 import ViewOne

def viewer(imgdir, kind=Toplevel, cols=None):
    """
    измененная версия, выполняет размещение с использованием кнопок фиксированного размера
    """
    win = kind()
    win.title('Viewer: ' + imgdir)
    thumbs = makeThumbs(imgdir)
    if not cols:
        cols = int(math.ceil(math.sqrt(len(thumbs))))   # фиксированное или N x N

    savephotos = []
    while thumbs:
        thumbsrow, thumbs = thumbs[:cols], thumbs[cols:]
        row = Frame(win)
        row.pack(fill=BOTH)
        for (imgfile, imgobj) in thumbsrow:
            size = max(imgobj.size)                     # ширинаб высота
            photo = PhotoImage(imgobj)
            link = Button(row, image=photo)
            handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
            link.config(command=handler, width=size, height=size)
            link.pack(side=LEFT, expand=YES)
            savephotos.append(photo)

    Button(win, text='Quit', command=win.quit, bg='beige').pack(fill=X)
    return win, savephotos

if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1])  \
             or 'D:/Python/Lutz/Programming_Python/PP4E-Examples-1.4/Examples/PP4E/Gui/PIL/images'
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()
