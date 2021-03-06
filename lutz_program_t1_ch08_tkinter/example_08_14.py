"""
Обеспечение модальности через рекурсию (не самый удобный вариант)

Если вызвать метод mainloop рекурсивно, возврат из вызова произойдет
только после выполнения метода quit виджета.

Метод quit прекращает выполнение функции mainloop и поэтому обычно завершает
выполнение программы с графическим интерфейсом. Но если произведен рекурсивный
вызов mainloop, метод quit просто завершит его.

Благодаря этому модальные диалоги можно реализовать без обращения к методу ожидания.

Выбирая этот путь, нужно вместо метода destroy вызывать в обработчиках событий
метод quit (destroy не завершает функцию mainloop) и обеспечить вызов quit
кнопкой закрытия окна с помощью метода protocol (иначе не будет завершаться
рекурсивный вызов mainloop, что приведет к генерации странных сообщений
об ошибках при окончательном выходе из программы).
Из-за этой дополнительной сложности более удобным может оказаться использование
wait_window или wait_variable, а не рекурсивных вызовов mainloop.
"""
from tkinter import *

def dialog():
    win = Toplevel()                                    # создать новое окно
    Label(win, text='Hard drive reformated!').pack()    # добавить виджеты
    Button(win, text='OK', command=win.quit).pack()     # установить обработчик quit
    win.protocol('WM_DELETE_WINDOW', win.quit)          # завершить при закрытии окна
    win.focus_set()                                     # принять фокус ввода
    win.grab_set()        # запретить доступ к другим окнам, пока открыт диалог
    win.mainloop()        # запустить вложенный цикл обработчика событий для ожидания
    win.destroy()
    print('dialog exit')

root = Tk()
Button(root, text='popup', command=dialog).pack()
root.mainloop()
