"""
Иерархическое построение графического интерфейса

Объединяет четыре сценария панелей запуска диалогов из примеров 8.9, 8.22, 8.25 и 8.30
В одном окне присутствуют 5 кнопок Quitter, щелчок на любой из них приводит к завершению
программы; графические интерфейсы могут повторно использоваться, как фреймы в контейнере,
независимые окна или процессы
"""
from tkinter import *
from examples.quitter import Quitter

demoModules = ['example_08_09', 'example_08_22', 'example_08_25', 'example_08_30']
parts = []

def addComponents(root):
    for demo in demoModules:
        module = __import__(demo)               # импортировать по имени в виде строки
        part = module.Demo(root)                # прикрепить экземпляр
        part.config(bd=2, relief=GROOVE)        # или передать параметры конструктору Demo
        part.pack(side=LEFT, expand=YES, fill=BOTH) # панели растягиваются вместе с окном
        # part.pack(side=LEFT, fill=BOTH)       # убран expand=YES - размер панелей неизменен
        parts.append(part)                      # добавить в список

def dumpState():
    for part in parts:
        print(part.__module__ + ':', end=' ')
        if hasattr(part, 'report'):
            part.report()
        else:
            print('none')

root = Tk()
root.title('Frames')
Label(root, text='Multiple Frame demo', bg='white').pack()
Button(root, text='States', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()

