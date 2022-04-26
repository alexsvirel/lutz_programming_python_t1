"""
Перемещение с применением тегов и функции time.sleep

Перемещение с применением тегов и функции time.sleep (без помощи метода widget.after
или потоков выполнения);
Функция time.sleep не блокирует цикл событий графического интерфейса на время паузы,
но интерфейс не обновляется до выхода из обработчика или вызова метода widget.update;
Текущему вызову обработчика onMove уделяется исключительное внимание,
пока он не вернет управление: если в процессе перемещения нажать клавишу ‘R’ или ‘O’;

Все три сценария в этом разделе при вытягивании новых фигур с помощью левой кнопки мыши
создают окно с голубыми овалами и красными прямоугольниками. Сама реализация вытягивания
наследуется из суперкласса. Щелчок правой кнопкой мыши немедленно перемещает одну фигуру,
а двойной щелчок левой кнопкой по-прежнему очищает холст – эти операции также унаследованы
из суперкласса.
В действительности в этом новом сценарии лишь изменены методы, создающие объекты, –
теперь они ассоциируют создаваемые объекты с тегами и окрашивают их
в соответствующие цвета, добавлено текстовое поле в верхней части холста и
добавлены обработчики событий, выполняющие перемещение.
С помощью клавиш O и R начинается анимация всех нарисованных овалов и прямоугольников
соответственно. Например, при нажатии клавиши O начинают синхронно перемещаться все
голубые овалы. Объекты, которые подвергаются анимации, помечаются пятью квадратами
вокруг своего местоположения, и перемещаются со скоростью четыре шага в секунду.
Новые объекты, которые вытягиваются, когда другие находятся в движении, тоже начинают
перемещаться, потому что помечены тегами.
"""
import time

from tkinter import *

import example_09_16

class CanvasEventDemo(example_09_16.CanvasEventsDemo):
    def __init__(self, parent=None):
        example_09_16.CanvasEventsDemo.__init__(self, parent)
        self.canvas.master.bind('<KeyPress-o>', self.onMoveOvals)
        self.canvas.master.bind('<KeyPress-r>', self.onMoveRectangles)
        self.kinds = self.create_oval_tagged, self.create_rectangle_tagged

    def create_oval_tagged(self, x1, y1, x2, y2):
        objectId = self.canvas.create_oval(x1, y1, x2, y2)
        self.canvas.itemconfig(objectId, tag='ovals', fill='blue')
        return objectId

    def create_rectangle_tagged(self, x1, y1, x2, y2):
        objectId = self.canvas.create_rectangle(x1, y1, x2, y2)
        self.canvas.itemconfig(objectId, tag='rectangles', fill='red')
        return objectId

    def onMoveOvals(self, event):
        print('moving ovals')
        self.moveInSquares(tag='ovals')         # переместить все овалы с данным тегом

    def onMoveRectangles(self, event):
        print('moving rectangles')
        self.moveInSquares(tag='rectangles')

    def moveInSquares(self, tag):               # 5 повторений по 4 раза в секунду
        for i in range(5):
            for (diffx, diffy) in [(+20, 0), (0, +20), (-20, 0), (0, -20)]:
                self.canvas.move(tag, diffx, diffy)
                self.canvas.update()            # принудительно обновить изображение
                time.sleep(0.25)                # пауза, не блокирующая интерфейс


if __name__ == '__main__':
    CanvasEventDemo()
    mainloop()
