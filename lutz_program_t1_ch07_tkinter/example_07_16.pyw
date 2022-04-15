"""
для перехвата события нажатия кнопки использует метод bind
Cуществуют различные способы перехвата событий в сценариях tkinter:
- Параметр command кнопки
- Параметры command меню
- Протоколы полос прокрутки
- Обобщенные методы bind виджетов
- Протоколы менеджера окон
- Обработчики планируемых событий
В примере для перехвата события нажатия кнопки использует метод bind, который
принимает низкоуровневые обработчики событий одинарных (<Button-1>) и двойных
щелчков левой кнопкой (<Double-1>) внутри области отображения кнопки.
"""
import sys
from tkinter import *


def hello(event):  # event дает виджет, координаты и т.д.
    print('Press twice to exit')  # одиночный щелчок левой кнопкой мыши


def quit(event):
    print('Hello, I must be going...')  # двойной щелчок кнопкой мыши
    sys.exit()


widget = Button(None, text='Hello event world')
widget.pack()
widget.bind('<Button-1>', hello)  # привязать обработчик одиного щелчка
widget.bind('<Double-1>', quit)  # привязать обработчик двойного щелчка
widget.mainloop()
