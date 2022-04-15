"""
устанавка параметры виджетов после их создания путем вызова метода config
"""
from tkinter import *

root = Tk()
widget = Label(root)
widget.config(text='Hello GUI world!')  # Метод config можно вызвать в любой момент после создания виджета
widget.pack(side=TOP, expand=YES, fill=BOTH)
root.title('example_07_08')  # метод root.title устанавливает текст в заголовке окна
root.mainloop()
