"""
импорт библиотеке tkinter целиком
в этом случае, при использовании ее модулей надо в именах писать еще и имя библиотеки
"""
import tkinter

widget = tkinter.Label(None, text='Hello GUI world')
widget.pack()
widget.mainloop()
