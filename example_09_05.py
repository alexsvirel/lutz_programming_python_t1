"""
Использование меню на основе фреймов в составе другого прикрепляемого компонента

Благодаря отсутствию привязки к охватывающему окну меню на основе фреймов можно
использовать в составе другого прикрепляемого компонента.

Например, прием встраивания меню в этом примере действует, даже когда родителем меню
является другой контейнер Frame, а не окно верхнего уровня.
Этот пример похож на предыдущий, но он создает три полнофункциональных строки меню,
прикрепленных к фреймам внутри окна.
"""
from tkinter import *

from example_09_03 import makemenu

root = Tk()
for i in range(3):              # 3 меню вложенные в контейнеры
    frm = Frame()
    frm.pack(expand=YES, fill=BOTH)
    mnu = makemenu(frm)
    mnu.config(bd=2, relief=RAISED)
    Label(frm, bg='black', height=5, width=25).pack(expand=YES, fill=BOTH)
Button(root, text="Bye", command=root.quit).pack()
root.mainloop()
