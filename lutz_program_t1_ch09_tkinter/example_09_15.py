"""
Расширенная версия сценария просмотра изображений:

отображает миниатюры на кнопках фиксированного размера, чтобы обеспечить
равномерное их размещение, и добавляет возможность прокрутки при просмотре
больших коллекций изображений, отображая миниатюры в виджете Canvas
с полосами прокрутки; требует наличия библиотеки PIL для отображения изображений
в таких форматах, как JPEG, и повторно использует инструменты создания миниатюр
и просмотра единственного изображения из сценария example_08_48.py;

предостережение/что сделать: можно также реализовать возможность прокрутки
при отображении единственного изображения, если его размеры оказываются больше
размеров экрана, которое сейчас обрезается в Windows;
"""
import sys
import math

from tkinter import *

from PIL.ImageTk import PhotoImage

from lutz_program_t1_ch08_tkinter.example_08_45 import makeThumbs
from lutz_program_t1_ch08_tkinter.example_08_45 import ViewOne

def viewer(imgdir, kind=Toplevel, numcols=None, height=300, width=300):
    """
    использует кнопки фиксированного размера и холст с возможностью прокрутки;
определяет размер области прокрутки (всего холста) и располагает
миниатюры по абсолютным координатам x,y холста; предупреждение:
предполагается, что все миниатюры имеют одинаковые размеры
    :param imgdir:
    :param kind:
    :param numcols:
    :param height:
    :param width:
    :return:
    """
    win = kind()
    win.title('Simple viewer: ' + imgdir)
    quit = Button(win, text='Quit', command=win.quit, bg='beige')
    quit.pack(side=BOTTOM, fill=X)

    canvas = Canvas(win, borderwidth=0)
    vbar = Scrollbar(win)
    hbar = Scrollbar(win, orient='horizontal')

    vbar.pack(side=RIGHT, fill=Y)               # прикрепить холст после полос прокрутки
    hbar.pack(side=BOTTOM, fill=X)              # чтобы он обрезался первым
    canvas.pack(side=TOP,fill=BOTH, expand=YES)

    vbar.config(command=canvas.yview)           # обработчики событий
    hbar.config(command=canvas.xview)           # перемещения полос прокрутки
    canvas.config(yscrollcommand=vbar.set)      # обработчики событий
    canvas.config(xscrollcommand=hbar.set)      # прокрутки холста
    canvas.config(height=height, width=width)   # начальные размеры видимой области, изменяемой
                                                # при изменении размеров окна
    thumbs = makeThumbs(imgdir)                 # [(imgfile, imgobj)]
    numthumbs = len(thumbs)
    if not numcols:
        numcols = int(math.ceil(math.sqrt(numthumbs)))  # фиксиров. или N x N
    numrows = int(math.ceil(numthumbs / numcols))       # истинное деление в 3.x

    linksize = max(thumbs[0][1].size)                       # (ширина, высота)
    fullsize = (0, 0,                                       # верхний левый угол X,Y
                (linksize * numcols), (linksize * numrows)) # нижний правый угол X,Y
    canvas.config(scrollregion=fullsize)                    # размер области прокрутки

    rowpos = 0
    savephotos = []
    while thumbs:
        thumbsrow, thumbs = thumbs[:numcols], thumbs[numcols:]
        colpos = 0
        for (imgfile, imgobj) in thumbsrow:
            photo = PhotoImage(imgobj)
            link = Button(canvas, image=photo)
            handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
            link.config(command=handler, width=linksize, height=linksize)
            link.pack(side=LEFT, expand=YES)
            canvas.create_window(colpos, rowpos, anchor=NW,
                                 window=link, width=linksize, height=linksize)
            colpos += linksize
            savephotos.append(photo)
        rowpos += linksize
    return win, savephotos

if __name__ == '__main__':
    imgdir = ('D:/Python/Lutz/Programming_Python/PP4E-Examples-1.4/Examples/PP4E/Gui/PIL/images' \
        if len(sys.argv) < 2 else sys.argv[1])
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()

