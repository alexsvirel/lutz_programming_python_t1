"""
Демонстрирует запуск двух отдельных циклов mainloop

Каждый из них возвращает управление после того как главное окно будет закрыто;
Ввод пользователя сохраняется в объекте Python перед тем, как графический интерфейс
будет закрыт;
Обычно в программах с графическим интерфейсом настройка виджетов и вызов mainloop
выполняется всего один раз, а вся их логика распределена по обработчикам событий;
В этом демонстрационном примере вызовы функции mainloop производятся для обеспечения
модальных взаимодействий с пользователем из программы командной строки;
демонстрирует один из способов добавления графического интерфейса к существующим сценариям
командной строки без реорганизации программного кода;
"""

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


class Demo(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        Label(self, text="Basic demos").pack()
        Button(self, text='open', command=self.openfile).pack(fill=BOTH)
        Button(self, text='save', command=self.savefile).pack(fill=BOTH)
        self.open_name = self.save_name = ""

    def openfile(self):  # сохранить результаты пользователя
        self.open_name = askopenfilename()  # указать параметры диалога здесь

    def savefile(self):
        self.save_name = asksaveasfilename(initialdir='C:\\Python31')


if __name__ == "__main__":
    # display window once
    print('popup1...')
    mydialog = Demo()  # присоединить фрейм к окну Tk() по умолчанию
    mydialog.mainloop()  # отобразить; вернуться после закрытия окна
    print(mydialog.open_name)  # nимена сохраняются в объекте, когда окно уже
    print(mydialog.save_name)  # будет закрыто
    # Раздел программы без графического интерфейса, использующей mydialog

    # отобразить окно еще раз
    print('popup2...')
    mydialog = Demo()  # повторно создать виджеты
    mydialog.mainloop()  # повторно отобразить окно
    print(mydialog.open_name)  # в объекте будут сохранены новые значения
    print(mydialog.save_name)
    # Раздел программы без графического интерфейса, где снова используется mydialog
    print('ending...')
