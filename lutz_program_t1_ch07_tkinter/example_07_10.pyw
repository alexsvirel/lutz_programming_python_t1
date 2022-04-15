"""
реализует способность программы реагировать на действия пользователя
для этого вместо "нереагурующей" текстовой метки на экран выводим
кнопу, которая при клике по ней может вызвать некое действие - вызвать
функцию обратного вызова
"""
import sys
from tkinter import *

widget = Button(None, text='Hello widget world', command=sys.exit)  # параметр command определяет функцию
# обратного вызова, которая должна
# вызываться при нажатии кнопки.
widget.pack()
widget.mainloop()
