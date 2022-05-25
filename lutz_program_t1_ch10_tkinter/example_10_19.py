# графический интерфейс, отображающий данные, производимые рабочими
# потоками на основе класса.

import queue
import threading
import time
from tkinter.scrolledtext import ScrolledText  # or PP4E.Gui.Tour.scrolledtext


class ThreadGui(ScrolledText):
    threadsPerClick = 5

    def __init__(self, parent=None):
        ScrolledText.__init__(self, parent)
        self.pack()
        self.dataQueue = queue.Queue()              # бесконечной длины
        self.bind('<Button-1>', self.makethreads)   # по щелчку левой кнопкой
        self.consumer()                             # цикл проверки очереди в главном
                                                    # потоке выполнения

    def producer(self, id):
        for i in range(5):
            # time.sleep(0.1)
            time.sleep(2.1)
            self.dataQueue.put('[producer id=%d, count=%d]' % (id, i))

    def consumer(self):
        try:
            data = self.dataQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            self.insert('end', 'consumer got => %s\n' % str(data))
            self.see('end')
        self.after(100, self.consumer)    # 10 раз в секунду

    def makethreads(self, event):
        for i in range(self.threadsPerClick):
            threading.Thread(target=self.producer, args=(i,)).start()

if __name__ == '__main__':
    root = ThreadGui()      # в главном потоке: создать GUI, запустить цикл таймера
    root.mainloop()         # войти в цикл событий tk
