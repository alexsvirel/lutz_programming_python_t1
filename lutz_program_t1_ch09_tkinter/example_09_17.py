"""
Привязка обработчиков событий к холсту и к элементам на нем

! щелчки отслеживаются только на холсте заданного (100х100) размера
Когда щелчок выполняется в окне сценария за границами текстовых элементов,
вызывается обработчик события холста.
Когда щелчок выполняется на любом текстовом элементе, вызываются оба
обработчика событий – и холста, и элемента.
"""
from tkinter import *

def onCanvasClick(event):
    print('Got canvas click', event.x, event.y, event.widget)

def onObjectClick(event):
    print('Got object click', event.x, event.y, event.widget, end=' ')
    print(event.widget.find_closest(event.x, event.y))  # найти ID текстового объекта

root = Tk()
canv = Canvas(root, width=100, height=100)
obj1 = canv.create_text(50, 30, text='Click me one')
obj2 = canv.create_text(50, 70, text='Click me two')

canv.bind('<Double-1>', onCanvasClick)                  # привязать клик к самому холсту
canv.tag_bind(obj1, '<Double-1>', onObjectClick)        # привязать к элементу
canv.tag_bind(obj2, '<Double-1>', onObjectClick)        # теги тоже можно использовать
canv.pack()

root.mainloop()
