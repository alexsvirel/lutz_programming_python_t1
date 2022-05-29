# графический интерфейс: действует так же, как example_10_26, но явно создает
# главное окно и запускает цикл событий

from tkinter import *
from example_10_12 import redirectedGuiShellCmd


def launch():
    redirectedGuiShellCmd('python -u examples/pipe-nongui.py')


window = Tk()
Button(window, text='GO!', command=launch).pack()
window.mainloop()
