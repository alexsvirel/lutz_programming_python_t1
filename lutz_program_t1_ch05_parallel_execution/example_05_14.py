"""
пример в книге - queuetest.py
Взаимодействие потоков производителей и потребителей посредством очереди

Сценарий в примере 5.14 порождает два потока-потребителя, ко-
торые ожидают появления данных в общей очереди, и четыре потока-
производителя, периодически, через определенные интервалы време-
ни, помещающие данные в очередь (для каждого из них установлена
своя продолжительность интервала, чтобы имитировать выполнение
длительных операций). Другими словами, эта программа запускает
семь потоков выполнения (включая главный поток), шесть из которых
обращаются к общей очереди параллельно.
"""

numconsumers = 2  # количество потоков-потребителей
numproducers = 4  # количество потоков-производителей
nummessages = 4  # количество сообщений, помещаемых производителем

import _thread as thread
import queue
import time

safeprint = thread.allocate_lock()  # в противном случае вывод может перемешиваться

dataQueue = queue.Queue()  # общая очередь неограниченного размера
# ссылка на очередь сохраняется в глобальной переменной. Благодаря этому очередь может
# использоваться всеми порожденными потоками выполнения (все они выполняются в одном
# процессе и в одном глобальном пространстве имен):

def producer(idnum):
    for msgnum in range(nummessages):
        time.sleep(idnum)
        dataQueue.put('[producer id=%d, count=%d]' % (idnum, msgnum))


def consumer(idnum):
    while True:
        time.sleep(0.1)
        try:
            data = dataQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            with safeprint:
                print('consumer', idnum, 'got =>', data)


if __name__ == '__main__':
    for i in range(numconsumers):
        thread.start_new_thread(consumer, (i,))
    for i in range(numproducers):
        thread.start_new_thread(producer, (i,))
    time.sleep(((numproducers - 1) * nummessages) + 1)
    print('Main thread exit.')
