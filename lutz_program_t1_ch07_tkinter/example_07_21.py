"""
создаем экземпляр класса и прикрепляем к нему пакет виджетов, создаваемых родительским классом,
передав ему родительский виджет

кнопка Hello добавляется к правому краю родителя parent – контейнера Frame и является встроенным
компонентом: она представляет прикрепленный объект класса Python. Нажатие кнопки  Hello выводит сообщение.

нажатие новой кнопки Attach закрывает окно вызовом sys.exit
"""
from sys import exit
from tkinter import *
from example_07_20 import Hello  # импортировать подкласс фрейма

parent = Frame(None)  # создать контейнерный виджет
parent.pack()
Hello(parent).pack(side=RIGHT)  # прикрепить виджет Hello, не запуская его

Button(parent, text='Attach', command=exit).pack(side=LEFT)
parent.mainloop()
