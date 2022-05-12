"""
Создает фрейм-ряд с меткой и полем ввода и дополнительной кнопкой, вызывающей
диалог выбора файла;

Эта реализация была выделена в отдельный модуль, потому что она может с успехом
использоваться и в других программах;

Вызывающая программа (или обработчики событий, как в данном случае) должна
сохранять ссылку на связанную переменную на все время использования ряда;
"""

from tkinter import *                                # виджеты и константы
from tkinter.filedialog import askopenfilename       # диалог выбора файла

def makeFormRow(parent, label, width=15, browse=True, extend=False):
    var = StringVar()
    row = Frame(parent)
    lab = Label(row, text=label + '?', relief=RIDGE, width=width)
    ent = Entry(row, relief=SUNKEN, textvariable=var)
    row.pack(fill=X)                                  # используются фреймы-ряды
    lab.pack(side=LEFT)                               # с метками фиксированной длины
    ent.pack(side=LEFT, expand=YES, fill=X)           # можно использовать grid(row, col)
    if browse:
        btn = Button(row, text='browse...')
        btn.pack(side=RIGHT)
        if not extend:
            btn.config(command=
                 lambda: var.set(askopenfilename() or var.get()) )
        else:
            btn.config(command=
                 lambda: var.set(var.get() + ' ' + askopenfilename()) )
    return var
