""" простое окно с меткой 'Hello GUI world' посередине"""
from tkinter import Label  # импорт виджета

widget = Label(None, text='Hello GUI world')  # создать его
widget.pack()  # разместить
widget.mainloop()  # запустить цикл событий
