"""
Попытка вызывать методы pack и grid в одном и том же родителе

вызывает грубую ошибку – только один менеджер компоновки может использоваться
в каждом отдельном родительском окне.
Здесь методы pack и grid одновременно используются в одном и том же родительском
контейнере (здесь, корневое окно), поэтому ОШИБКА!
"""
from tkinter import *
from example_09_19 import gridbox, packbox

root = Tk()
gridbox(root)
packbox(root)
Button(root, text='Quit', command=root.quit).pack()
mainloop()
