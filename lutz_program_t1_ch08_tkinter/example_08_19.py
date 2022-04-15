"""
Снова о создании модальных окон

Сценарий создает модальный диалог с формой:
- используя функции makeform и fetch из примера example_08_18, создает форму
и выводит ее содержимое.
- поля ввода прикрепляются к новому всплывающему окну Toplevel, создаваемому
по требованию и содержащему кнопку OK, генерирующую событие уничтожения окна
- метод wait_window влечет приостановку программы, пока окно не будет закрыто
"""
from tkinter import *
from examples.entry2 import makeform, fetch, fields


def show(entries, popup):
    # popup.destroy()
    fetch(entries)  # извлечь данные перед уничтожением окна!
    popup.destroy()  # если инструкции поменять местами, сценарий
    # будет возбуждать исключение


def ask():
    popup = Toplevel()  # отобразить форму в виде модального диалога
    ents = makeform(popup, fields)
    Button(popup, text='OK', command=(lambda: show(ents, popup))).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()  # ждать закрытия окна


root = Tk()
Button(root, text='Dialog', command=ask).pack()
root.mainloop()
