"""
Простой компонент холста с вертикальной прокруткой

Полосы прокрутки можно перекрестно связывать с холстами, используя те же протоколы,
которые использовались для добавления их к виджетам Listbox и Text,
но с некоторыми особыми требованиями:
- размеры области прокрутки и видимой области. Можно указать размер видимой области
холста, но при этом обязательно следует указать и размер прокручиваемой области холста
в целом;
- отображение координат в области просмотра в абсолютные координаты. Кроме того, нужно
устанавливать соответствие между координатами видимой области и координатами всего холста,
если холст больше, чем видимая его область.
"""
from tkinter import *

class ScrolledCanvas(Frame):
    def __init__(self, parent=None, color='brown'):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)            # сделать растягиваемым
        canv = Canvas(self, bg=color, relief=SUNKEN)
        canv.config(width=300, height=200)          # размер видимой области
        canv.config(scrollregion=(0, 0, 300, 1000)) # углы холста
        canv.config(highlightthickness=0)           # без рамки

        sbar = Scrollbar(self)
        sbar.config(command=canv.yview)             # связать sbar и canv
        canv.config(yscrollcommand=sbar.set)        # сдвиг одного = сдигу другого
        sbar.pack(side=RIGHT, fill=Y)               # первым добавлен - последним обрезан
        canv.pack(side=LEFT, expand=YES, fill=BOTH) # canv образается первым

        self.fillContent(canv)
        canv.bind('<Double-1>', self.onDoubleClick) # установить обработчик события
        self.canvas = canv

    def fillContent(self, canv):                    # переопределить при наследовании
        for i in range(10):
            canv.create_text(150, 50+(i*100), text='spam'+str(i), fill='beige')

    def onDoubleClick(self, event):                 # переопределить при наследовании
        print(event.x, event.y)
        print(self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))

if __name__ == '__main__':
    ScrolledCanvas().mainloop()
