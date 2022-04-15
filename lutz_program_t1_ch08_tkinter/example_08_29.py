"""
Берегите переменные переключателей (о чем действительно легко можно забыть)

Следует сохранять объект переменной tkinter, используемой для связи
с переключателями, все время, пока переключатели отображаются на экране.
Присвойте ссылку на объект глобальной переменной модуля, запомните в структуре
данных с длительным временем существования или сохраните как атрибут долгоживущего
объекта класса, как сделано в примере example_08_25.
В этом случае всегда будет можно получить информацию о состоянии переключателей.

В tkinter классы переменных обладают деструктором __del__,
который автоматически сбрасывает созданную переменную Tk, когда уничтожается
объект Python (то есть утилизируется сборщиком мусора).
В итоге все переключатели могут оказаться невыбранными, если объект переменной
будет утилизирован, до того момента, когда очередной щелчок мышью установит
новое значение переменной Tk.
"""
from tkinter import *

root = Tk()

def radio1():               # локальные переменные являются временными
    # global tmp            # если сделать их глобальными проблема будет решена
    tmp = IntVar()
    for i in range(10):
        rad = Radiobutton(root, text=str(i), value=i, variable=tmp)
        rad.pack(side=LEFT)
    tmp.set(5)              # выбрать 6-й переключатель

# Кажется, что первоначально должен быть выбран переключатель «5»,
# но этого не происходит. Локальная переменная tmp уничтожается при
# выходе из функции, переменная Tk сбрасывается и значение 5 теряет-
# ся (все переключатели оказываются невыбранными). Тем не менее эти
# переключатели прекрасно работают, если попробовать выполнять на
# них щелчки мышью, поскольку при этом переменная Tk переустанав-
# ливается. Если раскомментировать инструкцию global, кнопка 5 будет
# появляться в выбранном состоянии, как и задумывалось.
# Однако в версии Python 3.X это явление, похоже, приобрело дополни-
# тельные отрицательные черты: в этой версии переключатель «5» не
# только не выбирается изначально, но и перемещение указателя мыши
# над невыбранными переключателями порождает эффект незаказан-
# ного выбора многих их них, пока не будет выполнен щелчок мышью.
# (В версии 3.X также требуется инициализировать строковую пере-
# менную StringVar, совместно используемую переключателями, как мы
# делали это в предыдущих примерах; в противном случае переменная
# получит пустую строку, как значение по умолчанию, что переведет все
# переключатели в выбранное состояние!)

radio1()
root.mainloop()
