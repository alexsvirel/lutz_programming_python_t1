"""
Исправление ошибки - изоляция метода grid от метода pack в отдельном фрейме

Чтобы обеспечить растягивание виджетов, размещаемых с помощью метода grid,
требуется использовать параметры weight и sticky:
- Ряды и колонки становятся растягиваемыми, когда они помечены с помощью
параметра weight (вес)
- Виджеты растягиваются в отведенных им ячейках сетки, когда помечены
с помощью параметра sticky (липкий):
"""
from tkinter import *
from example_09_19 import gridbox, packbox

root = Tk()

frm = Frame(root)
frm.pack() # это работает
gridbox(frm) # у gridbox должен быть собственный родитель

packbox(root)

Button(root, text='Quit', command=root.quit).pack()
mainloop()
