"порождает потоки выполнения, пока не будет нажата клавиша 'q'"

import _thread

def child(tid):
    print('Привет от потока', tid)

def parent():
    i = 0
    while True:
        i += 1
        _thread.start_new_thread(child, (i,))
        if input() == 'q': break

parent()