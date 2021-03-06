"""
использование мьютексов в родительском/главном потоке выполнения для определения
момента завершения дочерних потоков, взамен time.sleep;
блокирует stdout, чтобы избежать конфликтов при выводе;

Для проверки состояния блокировки можно использовать ее метод
locked. Главный поток создает по одной блокировке для каждого до-
чернего потока, помещая их в глобальный список exitmutexes (не забы-
вайте, что функция потока использует глобальную область совместно
с главным потоком).
По завершении каждый поток приобретает свою блокировку в списке,
а главный поток просто ждет, когда будут приобретены все блокировки.
Это значительно более точный подход, чем просто приостанавливать работу
на определенное время, пока выполняются дочерние потоки,
в надежде обнаружить после возобновления, что все они будут завершены.
"""

import _thread as thread
stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(10)]

def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myId, i))
        stdoutmutex.release()
    exitmutexes[myId].acquire()    # signal main thread

for i in range(10):
    thread.start_new_thread(counter, (i, 100))

for mutex in exitmutexes:
    while not mutex.locked(): pass
print('Main thread exiting.')
