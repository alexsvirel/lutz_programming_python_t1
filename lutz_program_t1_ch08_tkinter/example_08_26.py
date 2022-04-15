"""
Что произойдет, если несколько переключателей будут иметь одно и то же значение

Если щелкнуть на переключателе 1, 4 или 7, будут выбраны все три, а предыдущие
выбранные окажутся сброшенными (их значение не равно «1»).
Обычно это не то, что требуется, – переключатели как правило используются для
представления групп с возможностью выбора единственного варианта (возможность
выбора сразу нескольких вариантов реализуется с помощью флажков).

Чтобы переключатели действовали, как им положено, надо, чтобы всем переключателям
была назначена одна и та же переменная, но разные значения.
Например, в примере example_08_25 имя демонстрационного диалога дает естественное
уникальное значение для каждой кнопки.
"""
from tkinter import *
root = Tk()
var = StringVar()
for i in range(10):
    rad = Radiobutton(root, text=str(i), variable=var, value=str(i % 3))
    rad.pack(side=LEFT)
var.set(' ')        # все переключатели сделать невыбранными
root.mainloop()
