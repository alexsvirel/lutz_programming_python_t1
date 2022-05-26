"""
Общесистемные утилиты поддержки многопоточной модели выполнения для графических
интерфейсов.

Реализует единую очередь обработчиков и цикл обработки событий от таймера для
ее проверки, совместно используемые всеми окнами в программе;
Рабочие потоки помещают в очередь свои обработчики завершения и протекания операции
для вызова в главном потоке;
Эта модель не блокирует графический интерфейс – он просто выполняет операции в
порождаемых дочерних потоках и обрабатывает события завершения и продолжения операций;
Рабочие потоки могут перекрываться во времени с главным потоком и с другими рабочими потоками.

Using a queue of callback functions and arguments is more useful than a
simple data queue if there can be many kinds of threads running at the
same time - each kind may have different implied exit actions.
На практике передача функций-обработчиков с аргументами через очереди намного
удобнее, чем передача простых данных, если в программе одновременно могут
действовать разнотипные потоки выполнения, – каждый тип может подразумевать
выполнение различных действий при завершении.

Because GUI API is not completely thread-safe, instead of calling GUI
update callbacks directly after thread main action, place them on a shared
queue, to be run from a timer loop in the main thread, not a child thread;
this also makes GUI update points less random and unpredictable; requires
threads to be split into main action, exit actions, and progress action.
Библиотеки создания графических интерфейсов не полностью поддерживают многопоточную модель.
Поэтому после выполнения основной операции в потоке обработчики, производящие изменение
графического интерфейса, не вызываются напрямую, а помещаются в общую очередь и вызываются
не в дочерних потоках, а в цикле обработки событий от таймера в главном потоке;
Это обеспечивает регулярность и предсказуемость моментов обновления графического интерфейса;
Требуется, чтобы логика потока разбивалась на а) основную операцию, б) завершающие действия
и 3) операцию, возвращающую информацию о протекании процесса.

Assumes threaded action raises an exception on failure, and has a 'progress'
callback argument if it supports progress updates;  also assumes callbacks
are either short-lived or update as they run, and that queue will contain
callback functions (or other callables) for use in a GUI app - requires a
widget in order to schedule and catch 'after' event loop callbacks; to use
this model in non-GUI contexts, could use simple thread timer instead.
Предполагается, что:
- в случае неудачи функция потока возбуждает исключение и принимает в аргументе
‘progress’ функцию обратного вызова (если поддерживает возможность передачи информации
о ходе выполнения операции);
- все обработчики выполняются очень быстро, либо производят обновление графического
интерфейса в процессе работы;
- очередь будет содержать функции обратного вызова или другие вызываемые объекты
для использования в приложениях с графическим интерфейсом (требуется наличие виджетов,
чтобы обеспечить работу цикла на основе метода ‘after’);
Для использования данной модели в сценариях без графического интерфейса можно было бы
использовать простой таймер.
"""

# запустить, даже если нет потоков сейчас, если модуль _threads недоступен в стандартной
# библиотеке,  возбуждает исключение ImportError и блокирует графический интерфейс
try:  #
    import _thread as thread
except ImportError:
    import _dummy_thread as thread  # тот же интерфейс без потоков

import queue
import sys

# общая очередь в глобальной области видимости, совместно используется потоками
threadQueue = queue.Queue(maxsize=0)  # бесконечного размера


#################################################################################
# ГЛАВНЫЙ ПОТОК:
# – периодически проверяет очередь;
# - выполняет действия, помещаемые в очередь, в контексте главного потока;
#
# Один потребитель (GUI) и множество производителей (загрузка, удаление, отправка);
# Простого списка было бы вполне достаточно, если бы операции list.append и list.pop
# были атомарными;
# 4 издание: в процессе обработки каждого события от таймера выполняет до N операций.
# Так сделано потому что обход в цикле всех обработчиков, помещенных в очередь, может
# заблокировать графический интерфейс, а при выполнении единственной операции вызов всех
# обработчиков # может занять продолжительное время или привести к неэффективному
# расходованию ресурсов # процессора на обработку событий от таймера (например,
# информирование о ходе выполнения операций);
# Предполагается, что обработчики выполняются очень быстро или выполняют обновление
# графического интерфейса в процессе работы (вызывают метод update): после вызова обработчика
# планируется очередное событие от таймера и управление возвращается в цикл событий;
# Поскольку этот цикл выполняется в главном потоке, он не препятствует завершению программы;
#################################################################################

def threadChecker(widget, delayMsecs=100, perEvent=1):  # 10 раз/сек, 1/таймер
    for i in range(perEvent):  # передайте другие значения, чтобы повысить скорость
        try:
            (callback, args) = threadQueue.get(block=False)  # выполнить до N обработчиков
        except queue.Empty:
            break  # очередь пуста?
        else:
            callback(*args)  # вызвать обработчик

    widget.after(delayMsecs,  # переустановить таймер и вернуться
                 lambda: threadChecker(widget, delayMsecs, perEvent))  # в цикл событий


#################################################################################
# НОВЫЙ ПОТОК
# – выполняет задание, помещает в очередь а) обработчик завершения и б) обработчик,
# возвращающий информацию о протекании процесса;
# - вызывает функцию основной операции с аргументами,
# - затем планирует вызов функций on* с контекстом. Запланированные вызовы добавляются
# в очередь и выполняются в главном потоке, чтобы # избежать параллельного обновления
# графического интерфейса;
# - позволяет программировать основные операции вообще без учета того, что они будут
# выполняться в потоках;
#
# Не вызывайте обработчики в # потоках: они могут обновлять графический интерфейс в потоке,
# поскольку передаваемая функция будет вызвана в потоке;
# Обработчик ‘progress’ просто должен добавлять в очередь функцию обратного вызова с
# передаваемыми ей аргументами;
#
# Не обновляйте текущие счетчики здесь: обработчик завершения # будет извлечен из очереди
# и выполнен функцией threadChecker в главном потоке;
#################################################################################

def threaded(action, args, context, onExit, onFail, onProgress):
    try:
        if not onProgress:  # ждать завершения этого потока
            action(*args)  # предполагается, что в случае неудачи будет возбуждено исключение
        else:
            def progress(*any):
                threadQueue.put((onProgress, any + context))

            action(progress=progress, *args)
    except:
        threadQueue.put((onFail, (sys.exc_info(),) + context))
    else:
        threadQueue.put((onExit, context))


def startThread(action, args, context, onExit, onFail, onProgress=None):
    thread.start_new_thread(
        threaded, (action, args, context, onExit, onFail, onProgress))


#################################################################################
# Счетчик или флаг с поддержкой многопоточной модели выполнения: удобно использовать,
# чтобы избежать выполнения перекрывающихся во времени операций, когда потоки изменяют
# другие общие данные, помимо тех, которые изменяются обработчиками, помещаемыми в очередь
#################################################################################

class ThreadCounter:
    def __init__(self):
        self.count = 0
        self.mutex = thread.allocate_lock()  # или Threading.semaphore

    def incr(self):
        self.mutex.acquire()  # или с помощью self.mutex:
        self.count += 1
        self.mutex.release()

    def decr(self):
        self.mutex.acquire()
        self.count -= 1
        self.mutex.release()

    def __len__(self): return self.count  # True/False, если используется как флаг


#################################################################################
# реализация самотестирования: разбивает поток на
# - основную операцию,
# - операцию завершения и
# - операцию информирования о ходе выполнения задания
#################################################################################

if __name__ == '__main__':  # самотестирование при запуске в виде сценария
    import time
    from tkinter.scrolledtext import ScrolledText  # или PP4E.Gui.Tour.scrolledtext


    def onEvent(i):  # реализация порождения потоков (code that spawns thread)
        myname = 'thread-%s' % i
        startThread(
            action=threadaction,
            args=(i, 3),
            context=(myname,),
            onExit=threadexit,
            onFail=threadfail,
            onProgress=threadprogress)


    # основная операция, выполняется новым потоком (thread's main action)
    def threadaction(id, reps, progress):  # то, что делает поток (what the thread does)
        for i in range(reps):
            time.sleep(1)
            if progress: progress(i)  # обработчик progress: в очередь
            # (progress callback: queued)
        if id % 2 == 1: raise Exception  # ошибочный номер: неудача
        # (odd numbered: fail)


    # обработчики завершения/информирования о ходе выполнения задания передаются
    # главному потоку через очередь
    # thread exit/progress callbacks: dispatched off queue in main thread
    def threadexit(myname):
        text.insert('end', '%s\texit\n' % myname)
        text.see('end')


    def threadfail(exc_info, myname):
        text.insert('end', '%s\tfail\t%s\n' % (myname, exc_info[0]))
        text.see('end')


    def threadprogress(count, myname):
        text.insert('end', '%s\tprog\t%s\n' % (myname, count))
        text.see('end')
        text.update()  # допустимо: выполняется в главном потоке


    # создать графический интерфейс и запустить цикл обработки событий от
    # таймера в главном потоке
    # порождать группу рабочих потоков в ответ на каждый щелчок мышью:
    # выполнение их может перекрываться во времени
    # make enclosing GUI and start timer loop in main thread
    # spawn batch of worker threads on each mouse click: may overlap
    text = ScrolledText()
    text.pack()
    threadChecker(text)  # запустить цикл обработки поток
    text.bind('<Button-1>',  # в 3.x функция list необходима для получени
              lambda event: list(map(onEvent, range(6))))  # всех результатов map,
    # для range - нет
    text.mainloop()  # pop-up window, enter tk event loop вход в цикл событий
