"""
Перемещение с применением метода widget.after() вместо циклов time.sleep

Аналогично примеру example_09_30, но с применением метода widget.after() вместо циклов time.sleep;
Поскольку это планируемые события, появляется возможность перемещать овалы и
прямоугольники _одновременно_ и отпадает необходимость вызывать метод update
для обновления графического интерфейса;
Движение станет беспорядочным, если еще раз нажать ‘o’ или ‘r’ в процессе
воспроизведения анимации: одновременно начнут выполняться несколько операций перемещения;

Эта версия наследует все изменения из предыдущей версии и при этом позволяет перемещать
овалы и прямоугольники одновременно – нарисуйте несколько овалов и прямоугольников,
а затем нажмите клавишу O и затем сразу клавишу R. Попробуйте нажать обе клавиши несколько
раз – чем больше нажатий, тем интенсивнее движение, потому что генерируется много событий,
перемещающих объекты из того места, в котором они находятся. Если во время перемещения
нарисовать новую фигуру, она, как и раньше, начнет перемещаться немедленно.
"""
from tkinter import *
import example_09_30

class CanvasEventsDemo(example_09_30.CanvasEventsDemo):
    def moveEm(self, tag, moremoves):
        (diffx, diffy), moremoves = moremoves[0], moremoves[1:]
        self.canvas.move(tag, diffx, diffy)
        if moremoves:
            self.canvas.after(250, self.moveEm, tag, moremoves)

    def moveInSquares(self, tag):
        allmoves = [(+20, 0), (0, +20), (-20, 0), (0, -20)] * 5
        self.moveEm(tag, allmoves)

if __name__ == '__main__':
    CanvasEventsDemo()
    mainloop()
