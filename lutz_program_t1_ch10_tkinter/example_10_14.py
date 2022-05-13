# перезагружает обработчики динамически

from tkinter import *
import examples.radactions as radactions    # получить первоначальные обработчики
from importlib import reload


class Hello(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        Button(self, text='message1', command=self.message1).pack(side=LEFT)
        Button(self, text='message2', command=self.message2).pack(side=RIGHT)

    def message1(self):
        reload(radactions)      # перезагрузить модуль radactions перед вызовом
        radactions.message1()   # теперь щелчок на кнопке вызовет новую версию

    def message2(self):
        reload(radactions)  # изменения в radactions.py возымеют эффект благодаря перезагрузке
        radactions.message2(self)   # вызовет свежую версию; передать self

    def method1(self):
        print('exposed method...')  # вызывается из функции в модуле radactions


Hello().mainloop()
