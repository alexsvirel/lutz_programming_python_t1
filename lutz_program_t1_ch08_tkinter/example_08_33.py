"""
Независимые окна

Когда есть набор классов компонентов, реализованных в виде фреймов, годится
любой родительский элемент – и фреймы, и новые окна верхнего уровня.
В этом примере все четыре объекта демонстрационных панелей прикрепляются
к собственным независимым окнам Toplevel, а не к одному и тому же контейнеру.

При этом 4 демонстрационных класса в независимых окнах верхнего уровня не процессы:
при завершении одного щелчком на кнопке Quit завершаются все остальные,
потому что все окна выполняются в одном и том же процессе;

здесь первое окно Tk создается вручную, иначе будет создано пустое окно
"""
from tkinter import *

demoModules = ['example_08_09', 'example_08_22', 'example_08_25', 'example_08_30']


def makePopups(modnames):
    demoObjects = []
    for modname in modnames:
        module = __import__(modname)  # импортировать по имени в виде строки
        window = Toplevel()  # создать новое окно
        demo = module.Demo(window)  # родительским является новое окно
        window.title(module.__name__)
        demoObjects.append(demo)
    return demoObjects


def allstates(demoObjects):
    for obj in demoObjects:
        if hasattr(obj, 'report'):
            print(obj.__module__, end=' ')
            obj.report()


root = Tk()  # явно создать корневое окно
root.title('Popups')
demos = makePopups(demoModules)
Label(root, text='Mutiple Toplevel window demo', bg='white').pack()
Button(root, text='States', command=lambda: allstates(demos)).pack(fill=X)
root.mainloop()
