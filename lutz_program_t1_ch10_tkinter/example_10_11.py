# Выводит диалог ввода параметров для сценария example_10_08 (unpacker) и запускает его

from tkinter import *                             # классы виджетов
from example_10_08 import unpack                  # использовать сценарий/модуль example_10_08
from example_10_09 import makeFormRow             # инструмент создания полей формы

def unpackDialog():
    win = Toplevel()
    win.title('Enter Unpack Parameters')
    var = makeFormRow(win, label='Input file', width=11)
    win.bind('<Key-Return>', lambda event: win.destroy())
    win.grab_set()
    win.focus_set()                  # сделать себя модальным
    win.wait_window()                # ждать возврата из диалога
    return var.get()                 # или закрытия его окна

def runUnpackDialog():
    input = unpackDialog()                    # получить входные параметры из диалога
    if input != '':                           # выполнить действия, не связанные с
        print('Unpacker:', input)             # графическим интерфейсом, передав имя
        unpack(ifile=input, prefix='')        # файла из диалога

if __name__ == "__main__":
    Button(None, text='popup', command=runUnpackDialog).pack()
    mainloop()
