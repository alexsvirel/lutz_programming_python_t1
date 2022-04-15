"""
Выводит изображения в каталоге, открывая новые окна для каждой картинки

GIF-файлы поддерживаются стандартными средствами tkinter, но JPEG-файлы будут
пропускаться при отсутствии пакета PIL
"""
import os, sys
from tkinter import *
from PIL.ImageTk import PhotoImage          # для JPEG и других форматов

imgdir = 'D:/Python/Lutz/Programming_Python/PP4E-Examples-1.4/Examples/PP4E/Gui/PIL/images' # путь к папке с картинками

if len(sys.argv) > 1:
    imgdir = sys.argv[1]

imgfiles = os.listdir(imgdir)

main = Tk()                 # создаем одно главное окно с кнопкой Quit, щелчок на которой
                            # закрывает все дополнительные окна
main.title('Viewe')
quit = Button(main, text='Quit all', command=main.quit, font=('courier', 25))
quit.pack()
savephotos = []

for imgfile in imgfiles:    # создаем дополнительные окна для каждой картинки в каталоге
    imgpath = os.path.join(imgdir, imgfile)
    win = Toplevel()
    win.title(imgfile)
    try:
        imgobj = PhotoImage(file=imgpath)
        Label(win, image=imgobj).pack()
        print(imgpath, imgobj.width(), imgobj.height()) # размер в пикселях
        savephotos.append(imgobj)
    except:
        errmsg = 'skipping %s\n%s' % (imgfile, sys.exc_info()[1])
        Label(win, text=errmsg).pack()

main.mainloop()
