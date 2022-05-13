# перезагружает обработчики динамически
# запустить сценарий example_10_14 и изменять сообщения, которые выводит example_10_15,
# в другом окне. Gри нажатии кнопок в окно консоли будут выводиться новые сообщения.

from tkinter import *
import example_10_15    # получить первоначальные обработчики
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
        reload(example_10_15)      # перезагрузить модуль radactions перед вызовом
        example_10_15.message1()   # теперь щелчок на кнопке вызовет новую версию

    def message2(self):
        reload(example_10_15)  # изменения в radactions.py возымеют эффект благодаря перезагрузке
        example_10_15.message2(self)   # вызовет свежую версию; передать self

    def method1(self):
        print('exposed method...')  # вызывается из функции в модуле radactions


Hello().mainloop()
