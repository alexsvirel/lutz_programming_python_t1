"""
Флажки. Сложный способ (без переменных)

В примере ведется свой список состояний флажков, который вручную обновляется
в обработчиках событий, определяемых с помощью параметра command

lambda-выражение передает индекс нажатой кнопки в списке states

Состояния флажков обновляются при каждом щелчке на флажках и
выводятся при выходе из программы
"""
from tkinter import *

states = []  # изменение объекта - не имени


def onPress(i):  # сохраняет состояния
    states[i] = not states[i]  # изменяет состояние False->True, True->False


root = Tk()
for i in range(10):
    chk = Checkbutton(root, text=str(i), command=(lambda i=i: onPress(i)))
    chk.pack(side=LEFT)
    states.append(False)

root.mainloop()
print(states)  # при выходе вывести все состояние
