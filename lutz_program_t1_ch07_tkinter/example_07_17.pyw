"""
интерфейс пользователя с несколькими виджетами
Сценарий создает виджет Frame (класс из библиотеки tkinter),
к которому прикрепляются три других виджета – Label и два Button – путем
передачи объекта Frame в первом аргументе. Это означает, что виджет Frame
становится родителем для трех других виджетов.
Обе кнопки этого интерфейса вызывают следующие обработчики:
•• Щелчок на кнопке Hello запускает функцию greeting, определенную
внутри этого файла, которая производит вывод в поток stdout.
•• Щелчок на кнопке Quit вызывает стандартный метод tkinter quit, который виджет win
наследует от класса Frame
(Frame.quit имеет тот же эффект, что и использованный ранее метод Tk.quit).
"""
from tkinter import *


def greeting():
    print('Hello stdout world...')


win = Frame()
win.pack()
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Hello', command=greeting).pack(side=LEFT)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT)

win.mainloop()
