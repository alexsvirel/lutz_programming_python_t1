# обертывает запуск сценария командной строки инструментом перенаправления его
# вывода в графический интерфейс

from tkinter import *
from example_10_10 import runPackDialog
from example_10_12 import redirectedGuiFunc

def runPackDialog_Wrapped(): # обработчик для использования в
    redirectedGuiFunc(runPackDialog) # модуле mytools.py, обертывает прежний обработчик целиком

if __name__ == '__main__':
    root = Tk()
    Button(root, text='pop', command=runPackDialog_Wrapped).pack(fill=X)
    root.mainloop()
