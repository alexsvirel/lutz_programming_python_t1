"""
виджет Optionmenu

В библиотеке tkinter имеется родственный (меню Menubutton) виджет Optionmenu,
который отображает выбранный элемент раскрывающегося меню. Он похож на Menubutton,
к которому добавлена метка, и при щелчке на нем выводит меню вариантов выбора.
Однако, чтобы получить результат выбора, нужно не регистрировать обработчик,
а связывать переменные tkinter (описанные в главе 8), при этом элементы меню
передаются конструктору в виде аргументов вслед за переменной.
"""
from tkinter import *

root = Tk()
var1 = StringVar()
var2 = StringVar()
opt1 = OptionMenu(root, var1, 'spam', 'eggs', 'toast')          # как и Menubutton,
opt2 = OptionMenu(root, var2, 'ham', 'bacon', 'sausage')        # но отображает
opt1.pack(fill=X)                                               # выбранный вариант
opt2.pack(fill=X)
var1.set('spam')
var2.set('ham')


def state():
    print(var1.get(), var2.get())                               # связанные переменные


Button(root, command=state, text='state').pack()
root.mainloop()
