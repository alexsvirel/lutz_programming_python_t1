"""
содаем новое поведение кнопки наследуемой из другого класса
в примере example_07_18.py создана кнопка при нажатии на которую программа завершается
здесь мы импортируем ту кнопку и переопределим метод callback так что при нажатии на
кнопку программа не завершается в стандартный поток вывода передает свое сообщение
"""
from example_07_18 import HelloButton


class MyButton(HelloButton):  # наследуем класс кнопки MyButton от кнопки HelloButton
    def callback(self):  # переопределяем метод обработчика
        print('Ignoring press...')  # только печатаем и ничего больше


if __name__ == '__main__':
    MyButton(None, text='Hello subclass world').mainloop()
