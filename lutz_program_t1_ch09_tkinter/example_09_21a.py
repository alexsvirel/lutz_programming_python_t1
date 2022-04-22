"""
Исправление ошибки - изоляция метода grid от метода pack в отдельном фрейме
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
