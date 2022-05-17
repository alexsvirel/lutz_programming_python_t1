# Использование классов, инкапсулирующих интерфейсы верхнего уровня,
# из example_10_16 в различных режимах:
# – в качестве подмешиваемых классов,
# - в качестве суперклассов и
# - непосредственно – из обычного процедурного программного кода.
# модуль windows должен импортироваться, иначе атрибут __name__ будет иметь
# значение __main__ в функции findIcon

from tkinter import Button, mainloop
from example_10_16 import MainWindow, PopupWindow, ComponentWindow

def _selftest():

    # использовать, как подмешиваемый класс
    class content:
        "используется так же, как Tk, Toplevel и Frame"
        def __init__(self):
            Button(self, text='Larch', command=self.quit).pack()
            Button(self, text='Sing ', command=self.destroy).pack()

    class contentmix(MainWindow, content):
        def __init__(self):
            MainWindow.__init__(self, 'mixin', 'Main')
            content.__init__(self)
    contentmix()

    class contentmix(PopupWindow, content):
        def __init__(self):
            PopupWindow.__init__(self, 'mixin', 'Popup')
            content.__init__(self)
    prev = contentmix()

    class contentmix(ComponentWindow, content):
        def __init__(self):                               # вложенный фрейм
            ComponentWindow.__init__(self, prev)          # в предыдущем окне
            content.__init__(self)                        # кнопка Sing стирает фрейм
    contentmix()

    # использовать в подклассах
    class contentsub(PopupWindow):
        def __init__(self):
            PopupWindow.__init__(self, 'popup', 'subclass')
            Button(self, text='Pine', command=self.quit).pack()
            Button(self, text='Sing', command=self.destroy).pack()
    contentsub()

    # использование в процедурном программном коде
    win = PopupWindow('popup', 'attachment')
    Button(win, text='Redwood', command=win.quit).pack()
    Button(win, text='Sing   ', command=win.destroy).pack()
    mainloop()

if __name__ == '__main__':
    _selftest()
