"всегда выводит 200 - благодаря синхронизации доступа к глобальному ресурсу"

import threading, time
count = 0

def adder(addlock):                 # совместно используемый объект блокировки
    global count
    with addlock:
        count = count + 1           # блокировка приобретается/освобождается автоматически
    time.sleep(0.5)
    with addlock:
        count = count + 1           # в каждый конкретный момент времени
                                    # только 1 поток может изменить значение переменной
addlock = threading.Lock()
threads = []
for i in range(100):
    thread = threading.Thread(target=adder, args=(addlock,))
    thread.start()
    threads.append(thread)

for thread in threads: thread.join()
print(count)