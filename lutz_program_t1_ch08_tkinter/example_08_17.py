"""
создаем окно для ввода Entry

и используем "умную" кнопку из примера example_08_07
"""
from tkinter import *
from examples.quitter import Quitter   # «Умная» и многократно используемая кнопка Quit

def fetch():
    print('Input => "%s"' % ent.get())      # извлечь текст

root = Tk()
ent = Entry(root)
ent.insert(0, 'Tipe words here')            # записать текст
ent.pack(side=TOP, fill=X)                  # растянуть по горизонтали

ent.focus()                                 # сразу становить фокус, чтобы избавить
                                            # от необходимости щелкать мышью

ent.bind('<Return>', (lambda event: fetch()))   # по нажатию клавиши Enter
btn = Button(root, text='Fetch', command=fetch) # и по щелчку на кнопке
btn.pack(side=LEFT)

Quitter(root).pack(side=RIGHT)
root.mainloop()


