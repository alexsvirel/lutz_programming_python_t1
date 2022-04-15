"""
напишем собственную функцию обратного вызова (вызывается при нажатии кнопки)
"""
import sys
from tkinter import *


def quit():  # собственный обработчик событий
    print('Hello, I must be going...')  # распечатать в поток stdout
    sys.exit()  # закрыть окно и завершить процесс


widget = Button(None, text='Hello, event world', command=quit)
widget.pack()
widget.mainloop()
