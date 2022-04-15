"""
«Переменные» tkinter и альтернативные способы компоновки форм

example_08_20
Виджеты Entry (наряду с другими) поддерживают понятие ассоциированной
переменной – изменение значения ассоциированной переменной изменяет текст,
отображаемый виджетом Entry, а изменение текста в Entry изменяет значение
переменной. Однако это не обычные переменные Python.

Переменные, связанные с виджетами, являются экземплярами классов переменных
в библиотеке tkinter. Эти классы носят названия StringVar, IntVar, DoubleVar
и BooleanVar. Выбор того или иного класса зависит от контекста, в котором
он должен использоваться. Например, можно связать с полем Entry экземпляр
класса StringVar, как показано в этом примере

виджеты в окне компонуются как фрейм с двумя вложенными фреймами, образующими
левую и правую колонки в области формы, – но конечный результат при отображении
на экран оказывается тем же самым как в примере example_08_18
"""
from tkinter import *
from examples.quitter import Quitter   # «Умная» и многократно используемая кнопка Quit

fields = 'Name', 'Job', 'Pay'

def fetch(variables):
    for variable in variables:
        print('Input = > "% s"' % variable.get())   # извлечь из переменных

def makeform(root, fields):
    form = Frame(root)                              # создать внешний фрейм
    left = Frame(form)                              # создать две колонки
    rite = Frame(form)
    form.pack(fill=X)
    left.pack(side=LEFT)
    rite.pack(side=RIGHT, expand=YES, fill=X)       # растягивать по горизонтали

    variables = []
    for field in fields:
        lab = Label(left, width=5, text=field)      # добавить в колонки
        ent = Entry(rite)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X)                  # растягивать по горизонтали
        var = StringVar()
        ent.config(textvariable=var)                # связать поле с переменной
        var.set('enter here')
        variables.append(var)
    return variables

if __name__ == '__main__':
    root = Tk()
    vars = makeform(root, fields)
    Button(root, text='Fetch', command = (lambda: fetch(vars))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: fetch(vars)))
    root.mainloop()

