"""
Скрывает и отображает окно целиком
"""
from tkinter import *
import example_09_27


class Alarm(example_09_27.Alarm):
    def repeater(self):                         # каждые N миллисекунд
        self.bell()                             # подать сигнал
        if self.master.state() == 'normal':     # окно отображается?
            self.master.withdraw()              # скрыть окно, без ярлыка
        else:                                   # iconify свертывает в ярлык
            self.master.deiconify()             # иначе перерисовать окно
        self.master.lift()                      # и поднять над остальными
        self.after(self.msecs, self.repeater)   # переустановить обработчик


if __name__ == '__main__':
    Alarm(msecs=1500).mainloop()                          # master = корневое окно Tk по умолчанию
