"""
некоторые параметры настройки виджетов в tkinter

- параметры шрифта (семейство, размер, стиль)
- цвет фона и шрифта
- размер метки
"""
from tkinter import *

root = Tk()
labelfont = ('times', 20, 'bold')   # задаем параметры шрифта: семейство, размер, стиль
widget = Label(root, text='Hello config font')
widget.config(bg='black', fg='yellow')  # зедаем желтый шрифт на черном фоне
widget.config(font=labelfont)           # используем ранее заданный шрифт
widget.config(height=3, width=20)       # начальный размер метки (количество строк, символов в строке)
widget.pack(expand=YES, fill=BOTH)

root.mainloop()
