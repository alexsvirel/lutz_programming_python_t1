# Выводит диалог ввода параметров для сценария example_10_07 и запускает его

from glob import glob                           # расширение шаблонов имен файлов
from tkinter import *                           # виджеты графического интерфейса
from example_10_07 import pack                  # использовать сценарий/модуль example_10_07
from example_10_09 import makeFormRow           # использовать инструмент создания форм

def packDialog():                               # новое окно верхнего уровня
    win = Toplevel()                            # с 2 фреймами-рядами + кнопка ok
    win.title('Enter Pack Parameters')
    var1 = makeFormRow(win, label='Output file')
    var2 = makeFormRow(win, label='Files to pack', extend=True)
    Button(win, text='OK', command=win.destroy).pack()
    win.grab_set()
    win.focus_set()                  # модальный: захватить мышь, фокус ввода, ждать закрытия
    win.wait_window()                # окна диалога (иначе возврат произойдет немедленно);

    return var1.get(), var2.get()    # извлечь значения связанных переменных

def runPackDialog():
    output, patterns = packDialog()                  # вывести диалог и ждать щелчка на
    if output != "" and patterns != "":              # кнопке ok или закрытия окна
        patterns = patterns.split()                  # выполнить действия не связанные с
        filenames = []                               # графическим интерфейсом
        for sublist in map(glob, patterns):          # вып. расширение шаблона вручную
            filenames += sublist                     # командные оболочки Unix
        print('Packer:', output, filenames)          # делают это автоматически
        pack(ofile=output, ifiles=filenames)         # вывод также можно показать в
                                                     # графическом интерфейсе

if __name__ == '__main__':
    root = Tk()
    Button(root, text='popup', command=runPackDialog).pack(fill=X)
    Button(root, text='bye',   command=root.quit).pack(fill=X)
    root.mainloop()
