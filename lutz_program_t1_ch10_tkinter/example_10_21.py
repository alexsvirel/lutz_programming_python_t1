# тест очереди обработчиков, но для реализации операций используются связанные методы
# В этой версии в качестве обработчиков завершения и информирования
# о ходе выполнения задания, помещаемых в очередь, а также основной
# операции, выполняемой потоком, используются связанные методы.

import time
# from threadtools import threadChecker, startThread
from example_10_20 import threadChecker, startThread
from tkinter.scrolledtext import ScrolledText


class MyGUI:
    def __init__(self, reps=3):
        self.reps = reps  # используется окно Tk по умолчанию
        self.text = ScrolledText()  # сохранить виджет в атрибуте
        self.text.pack()
        threadChecker(self.text)  # запустить цикл проверки потоков
        self.text.bind('<Button-1>',  # 3.x функция list необходима для получения
                       # всех результатов map, для range - нет
                       lambda event: list(map(self.onEvent, range(6))))

    def onEvent(self, i):  # метод, запускающий поток
        myname = 'thread-%s' % i
        startThread(
            action=self.threadaction,
            args=(i,),
            context=(myname,),
            onExit=self.threadexit,
            onFail=self.threadfail,
            onProgress=self.threadprogress)

    # основная операция, выполняемая новым потоком
    def threadaction(self, id, progress):  # то, что делает поток
        for i in range(self.reps):  # доступ к данным в объекте
            time.sleep(1)
            if progress: progress(i)  # обработчик progress: в очередь
        if id % 2 == 1: raise Exception  # ошибочный номер: неудача

    # другие обработчики: передаются главному потоку через очередь
    def threadexit(self, myname):
        self.text.insert('end', '%s\texit\n' % myname)
        self.text.see('end')

    def threadfail(self, exc_info, myname):  # имеет доступ к данным объекта
        self.text.insert('end', '%s\tfail\t%s\n' % (myname, exc_info[0]))
        self.text.see('end')

    def threadprogress(self, count, myname):
        self.text.insert('end', '%s\tprog\t%s\n' % (myname, count))
        self.text.see('end')
        self.text.update()  # допустимо: выполняется в главном потоке


if __name__ == '__main__': MyGUI().text.mainloop()
