# обработчики: перезагружаются перед каждым вызовом

def message1():                 # изменить себя
    print('нука вот давай!')       # можно было бы вывести диалог...

def message2(self):
    print('ни за что и никада вот')            # изменить себя
    self.method1()              # обращение к экземпляру ‘Hello’...