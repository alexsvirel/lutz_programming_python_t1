"""
Несколько меню на основе фреймов в одном окне

В этом примере в одном окне будет размещено два меню.
Так как окно одно, то в нем никак не разместить два оконных меню из example_09_01,
зато можно разместить несколько фреймовых меню из примера example_09_03
"""
from tkinter import *

from example_09_03 import makemenu

root = Tk()
for i in range(2):              # 2 меню в одном окне
    mnu = makemenu(root)
    mnu.config(bd=2, relief=RAISED)
    Label(root, bg='black', height=5, width=25).pack(expand=YES, fill=BOTH)
Button(root, text="Bye", command=root.quit).pack()
root.mainloop()
