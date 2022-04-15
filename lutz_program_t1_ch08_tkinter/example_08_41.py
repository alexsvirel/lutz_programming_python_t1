"""
Развлечения с кнопками и картинками в виде класса

Пример example_08_40 переделан в виде класса:
В основном переделка состоит в добавлении отступов и префикса self перед именами
глобальных переменных. Эта версия действует точно так же, как и оригинал,
но теперь ее можно прикрепить к любому другому графическому интерфейсу.
"""

from tkinter import *           # импортировать базовый набор виджетов,
from glob import glob           # чтобы получить список файлов по расширению
import example_08_22            # прикрепить демонстрационный пример с флажками
import random                   # выбрать случайную картинку

gifdir = 'D:/Python/lutz/Programming_Python/PP4E-Examples-1.4/Examples/PP4E/Gui/gifs/' # каталог с GIF-файлами

class ButtonPicsDemo(Frame):
    def __init__(self, gifdir=gifdir, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.lbl = Label(self, text="none", bg='blue', fg='red')
        self.pix = Button(self, text="Press me", command=self.draw, bg='white')
        self.lbl.pack(fill=BOTH)
        self.pix.pack(pady=10)
        example_08_22.Demo(self, relief=SUNKEN, bd=2).pack(fill=BOTH)
        files = glob(gifdir + "*.gif")
        self.images = [(x, PhotoImage(file=x)) for x in files]
        print(files)

    def draw(self):
        name, photo = random.choice(self.images)
        self.lbl.config(text=name)
        self.pix.config(image=photo)

if __name__ == '__main__':
    ButtonPicsDemo().mainloop()