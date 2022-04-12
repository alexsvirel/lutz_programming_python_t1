"""
Расположение меню Menubutton на обыкновенной кнопке

меню, основанные на Menubutton, являются  универсальными и могут появляться 
в любом месте интерфейса, где может располагаться обычная кнопка, а не только 
в строке меню во фрейме Frame. В этом примере создается раскрывающийся 
список Menubutton, который отображается самостоятельно и прикреплен к корневому окну.
"""
from tkinter import *

root = Tk()
mbutton = Menubutton(root, text='Food')         # отдельное раскрывающееся меню
picks = Menu(mbutton)
mbutton.config(menu=picks)
picks.add_command(label='spam', command=root.quit)
picks.add_command(label='eggs', command=root.quit)
picks.add_command(label='bacon', command=root.quit)
mbutton.pack()
mbutton.config(bg='white', bd=4, relief=RAISED)
root.mainloop()
