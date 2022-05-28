# сервер GUI: читает и отображает текст, полученный от сценария командной строки

from socket import *  # включая socket.error
from tkinter import Tk

from examples.guiStreams import GuiOutput
from examples.launchmodes import PortableLauncher

myport = 50008
sockobj = socket(AF_INET, SOCK_STREAM)       # GUI - сервер, сценарий - клиент
sockobj.bind(('', myport))                   # сервер настраивается перед запуском клиента
sockobj.listen(5)

print('starting')
PortableLauncher('nongui', 'example_10_24.py -gui')()  # запустить сценарий

print('accepting')
conn, addr = sockobj.accept()                # ждать подключения клиента
conn.setblocking(False)                      # неблокирующий сокет (False=0)
print('accepted')

def checkdata():
    try:
        message = conn.recv(1024)            # попытка ввода не блокируется
        #output.write(message + '\n')        # можно также сделать sys.stdout=output
        print(message, file=output)          # если текст получен - вывести в окне
    except error:                            # возбудит socket.error, если нет данных
        print('no data')                     # вывести в sys.stdout
    root.after(1000, checkdata)              # проверять раз в секунду

root = Tk()
output = GuiOutput(root)                     # текст из сокета отображается здесь
checkdata()
root.mainloop()
