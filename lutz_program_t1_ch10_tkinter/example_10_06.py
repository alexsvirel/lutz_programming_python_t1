#!/usr/local/bin/python
"""
Определяются два набора инструментов, специфичных для типов,

чтобы предоставить наборы доступных инструментов в виде списка и словаря.
Обычно достаточно одного из них, но модуль иллюстрирует применение обоих.
Кроме того, именно этот модуль запускает графический интерфейс,
а модуль example_10_05 (shellgui) является всего лишь библиотекой классов.

Классы в этом модуле являются конкретными наборами утилит. Чтобы вывести
другой набор имен утилит, нужно написать и использовать новый подкласс.
"""
from example_10_05 import * # интерфейсы, специфичные для типов
from lutz_program_t1_ch10_tkinter.examples.packdlg import runPackDialog # диалоги для ввода данных
from lutz_program_t1_ch10_tkinter.examples.unpkdlg import runUnpackDialog # оба используют классы приложений

class TextPak1(ListMenuGui):
    def __init__(self):
        self.myMenu = [('Pack ', runPackDialog),    # простые функции
                       ('Unpack', runUnpackDialog),  # длина меток одинаковая
                       ('Mtool ', self.notdone)]  # метод из GuiMixin
        ListMenuGui.__init__(self)

    def forToolBar(self, label):
        return label in {'Pack ', 'Unpack'}  # синтаксис множеств в 3.x


class TextPak2(DictMenuGui):
    def __init__(self):
        self.myMenu = {'Pack ': runPackDialog, # или использовать input...
                       'Unpack': runUnpackDialog, # вместо диалогов ввода
                       'Mtool ': self.notdone}
        DictMenuGui.__init__(self)


if __name__ == '__main__': # реализация самопроверки...
    from sys import argv # 'example_10_06.py list|^'
    if len(argv) > 1 and argv[1] == 'list':
        print('list test')
        TextPak1().mainloop()
    else:
        print('dict test')
        TextPak2().mainloop()

