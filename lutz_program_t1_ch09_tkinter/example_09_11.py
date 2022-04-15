"""
Сохранение в файл, удаление и вставка текста и поиск строки

За счет наследования добавляет в ScrolledText типичные инструменты редактирования;
аналогичного результата можно было бы добиться, применив прием композиции (встраивания);
ненадежно!
"""
import sys

from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.filedialog import asksaveasfilename

from lutz_program_t1_ch08_tkinter.examples.quitter import Quitter as Quitter
from example_09_10 import ScrolledText as ScrolledText


class SimpleEditor(ScrolledText):                       # доп. ф-ции смотрите в PyEdit
    def __init__(self, parent=None, file=None):
        frm = Frame(parent)
        frm.pack(fill=X)
        Button(frm, text='Save', command = self.onSave).pack(side=LEFT)
        Button(frm, text='Cut', command = self.onCut).pack(side=LEFT)
        Button(frm, text='Paste', command = self.onPaste).pack(side=LEFT)
        Button(frm, text='Find', command = self.onFind).pack(side=LEFT)
        Quitter(frm).pack(side=LEFT)
        ScrolledText.__init__(self, parent, file=file)
        self.text.config(font=('courier', 9, 'normal'))

    def onSave(self):
        filename = asksaveasfilename()
        if filename:
            alltext = self.gettext()                        # от начала до конца
            open(filename, 'w').write(alltext)              # сохранить текст в файл

    def onCut(self):
        text = self.text.get(SEL_FIRST, SEL_LAST)           # ошибка, если нет выделения
        self.text.delete(SEL_FIRST, SEL_LAST)               # следует обернуть в try
        self.clipboard_clear()                              # очистить буфер обмена
        self.clipboard_append(text)                         # сохранить строку текста в буфер

    def onPaste(self):                                      # добавляет текст из буфера
        try:
            text = self.selection_get(selection='CLIPBOARD') # получить содержимое буфера, если есть
            self.text.insert(INSERT, text)
        except TclError:
            pass                                            # не вставлять

    def onFind(self):
        target = askstring('SimpleEditor', 'Search String?')
        if target:
            where = self.text.search(target, INSERT, END)   # от позиции курсора
        if where:                                           # вернуть индекс
            print(where)
            pastit = where + ('+ % dc' % len(target))       # индекс за целью
            # self.text.tag_remove(SEL, '1.0', END)         # снять выделение
            self.text.tag_add(SEL, where, pastit)           # выделить найденное
            self.text.mark_set(INSERT, pastit)              # установить метку вставки
            self.text.see(INSERT)                           # прокрутить текст
            self.text.focus()                               # выбрать виджет Text


if __name__ == '__main__':
    if len(sys.argv) > 1:
        SimpleEditor(file=sys.argv[1]).mainloop() # имя файла в ком. строке
    else:
        SimpleEditor().mainloop() # или нет: пустой виджет


