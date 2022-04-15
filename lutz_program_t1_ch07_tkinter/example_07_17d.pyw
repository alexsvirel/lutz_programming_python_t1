"""
добавлены параметры side, expand и fill для фрейма
теперь фрейм растягивается вместе с окном и вместе с фреймом растяиваются и
кнопки с меткой
"""
from tkinter import *


def greeting():
    print('Hello stdout world...')


win = Frame()
win.pack(side=TOP, expand=YES, fill=BOTH)
Button(win, text='Hello', command=greeting).pack(side=LEFT, fill=Y)
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT, expand=YES, fill=X)

win.mainloop()
