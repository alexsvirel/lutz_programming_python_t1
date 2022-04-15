"""
Настройка виджетов с помощью классов
Пример просто отображает одну кнопку, при нажатии на которую программа выводит
сообщение и завершается. Но на этот раз мы сами создали виджет кнопки.

Класс HelloButton наследует все свойства и методы класса Button, а также добавляет метод callback
и логику в конструкторе, устанавливая параметру command значение self.callback – связанный метод экземпляра.

При нажатии на кнопку теперь вызывается не просто функция, а метод callback
нового класса виджета. Аргумент **config собирает в словарь все дополнительные именованные аргументы,
которые затем передаются конструктору Button.

Конструкция **config в вызове конструктора Button распаковывает словарь в список именованных аргументов
(в действительности в этом нет необходимости, благодаря поддержке устаревшей формы вызова со словарем).
Это просто альтернативный способ передачи параметров настройки после создания виджета
(вместо передачи аргументов конструктору).

Внимание - расширение у файла .py так нужно чтобы в файле example_07_19.pyw можно было импортировать класс
"""
from tkinter import *


class HelloButton(Button):
    def __init__(self, parent=None, **config):  # регистрирует метод callback
        Button.__init__(self, parent, **config)  # и добавляет себя в интерфейс
        self.pack()
        self.config(command=self.callback)

    def callback(self):  # действие по умолчанию при нажатии
        print('Goodbye world...')  # переопределить в подклассах
        self.quit()


if __name__ == '__main__':
    HelloButton(text='Hello subclass world').mainloop()
