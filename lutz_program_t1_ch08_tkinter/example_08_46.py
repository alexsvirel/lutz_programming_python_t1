"""
то же самое, что в примере example_08_45, но не сохраняет и не загружает миниатюры из файлов:

для маленьких коллекций изображений, кажется, работает также быстро,
но для больших коллекций, при сохранении миниатюр в файлах, запуск происходит намного быстрее;
в некоторых приложениях (например, в веб-страницах) сохранение может оказаться насущной необходимостью
"""
import os
import sys
from tkinter import Tk

from PIL import Image

import example_08_45


def makeThumbs(imgdir, size=(100, 100), subdir='thumbs'):
    """
    создает миниатюры в памяти, но нее сохраняет их в файлах
    """
    thumbs = []
    for imgfile in os.listdir(imgdir):
        imgpath = os.path.join(imgdir, imgfile)
        try:
            imgobj = Image.open(imgpath)  # создать новую миниатюру
            imgobj.thumbnail(size)
            thumbs.append((imgfile, imgobj))
        except:
            print("Skipping: ", imgpath)
    return thumbs


if __name__ == '__main__':
    imgdir = ((len(sys.argv)  > 1 and sys.argv[1]) \
              or 'D:/Python/Lutz/Programming_Python/PP4E-Examples-1.4/Examples/PP4E/Gui/PIL/images')
    example_08_45.makeThumbs = makeThumbs
    main, save = example_08_45.viewer(imgdir, kind=Tk)
    main.mainloop()
