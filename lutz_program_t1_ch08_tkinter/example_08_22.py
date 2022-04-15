"""
создает группу флажков, которые вызывают демонстрационные диалоги

флажки похожи на обычные кнопки, однако функционально они несколько отличаются.
Флажок работает как переключатель:
- щелчок на нем изменяет его состояние из выключенного во включенное
(из невыбранного в выбранное) или обратно – из включенного в выключенное.
- когда флажок выбран, на нем выводится галочка,
а связанная с ним переменная IntVar получает значение 1;
- когда он не выбран, галочка исчезает,
а его переменная IntVar получает значение 0.

Чтобы смоделировать приложение, содержащее флажки, кнопка State в этом примере
запускает метод report в сценарии, который выводит текущие состояния всех пяти
флажков в поток stdout.

Параметр command этого виджета позволяет зарегистрировать обработчик,
который будет вызываться при каждом щелчке на виджете. Для иллюстрации в качестве
обработчика для каждого из флажков в этом сценарии зарегистрирован вызов
демонстрации стандартного диалога: щелчок изменяет состояние переключателя,
а кроме того, выводит один из знакомых диалогов.
"""
from tkinter import *                   # импортировать базовый набор виджетов
from examples.dialogTable import demos  # импортировать готовые диалоги
from examples.quitter import Quitter    # прикрепить к себе объект Quitter

class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        self.tools()
        Label(self, text="Check demos").pack()
        self.vars = []
        for key in demos:
            var = IntVar()
            Checkbutton(self, text=key, variable=var, command=demos[key]).pack(side=LEFT)
            self.vars.append(var)

    def report(self):
        for var in self.vars:
            print(var.get(), end=' ')   # текущее значение флажковЖ 1 или 0
        print()

    def tools(self):
        frm = Frame(self)
        frm.pack(side=RIGHT)
        Button(frm, text='State', command=self.report).pack(fill=X)
        Quitter(frm).pack(fill=X)

if __name__ == '__main__':
    Demo().mainloop()

