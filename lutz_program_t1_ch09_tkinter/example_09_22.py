"""
Реализация возможности растягивания виджетов, размещаемых по сетке

Чтобы обеспечить полную способность к растягиванию, требуется вызвать метод
rowconfigure контейнера сетки для каждого ряда и метод columnconfigure
для каждой колонки.
Обоим методам нужно передать параметр weight веса со значением больше нуля,
чтобы ряды и колонки стали растягиваемыми. По умолчанию вес принимается равным
нулю (что означает отсутствие поддержки растягивания).
Использование разных весов для разных рядов и колонок заставляет их растягиваться
в различных пропорциях.

Параметр sticky метода grid играет роли обоих параметров, fill и anchor, метода pack.
Чтобы заставить растягиваться виджеты, размещаемые по сетке, можно прилепить их
к одному краю отведенной им ячейки (как с помощью параметра anchor)
или более чем к одному краю (как с помощью параметра fill).
Приклеивать виджеты можно в четырех направлениях – N (север), S (юг), E (восток) и W (запад),
а комбинируя эти четыре буквы, можно обеспечить приклеивание сразу к нескольким сторонам.
"""
from tkinter import *

colors = ['white', 'red', 'orange', 'yellow', 'green', 'light blue', 'blue', 'brown', 'black']

def gridbox(root):
    Label(root, text='Grid').grid(columnspan=2)
    row = 1
    for color in colors:
        lab = Label(root, text=color, relief=RIDGE, width=25)
        ent = Entry(root, bg=color, relief=SUNKEN, width=50)
        lab.grid(row=row, column=0, sticky=NSEW)
        ent.grid(row=row, column=1, sticky=NSEW)
        root.rowconfigure(row, weight=1)
        row += 1
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

def packbox(root):
    Label(root, text='Pack').pack()
    for color in colors:
        row = Frame(root)
        lab = Label(row, text=color, relief=RIDGE, width=25)
        ent = Entry(row, bg=color, relief=SUNKEN, width=50)
        row.pack(side=TOP, expand=YES, fill=BOTH)
        lab.pack(side=LEFT, expand=YES, fill=BOTH)
        ent.pack(side=RIGHT, expand=YES, fill=BOTH)

root = Tk()
gridbox(Toplevel(root))
packbox(Toplevel(root))
Button(root, text='Quit', command=root.quit).pack()
mainloop()

