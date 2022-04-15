"""
в качестве функции обратного вызова используем lambda-функцию
это можеть понадобиться из-за того, что функция обратного вызова в tkinter
всегда вызывается без аргументов и надо искать способ передать в неё аргументы при необходимости
"""
import sys
from tkinter import *  # lambda-выражение генерирует функцию

# но содержит всего лишь выражение

widget = Button(None,
                text='Hello event world',
                command=(lambda: print('Hello lambda world') or sys.exit()))
widget.pack()
widget.mainloop()
