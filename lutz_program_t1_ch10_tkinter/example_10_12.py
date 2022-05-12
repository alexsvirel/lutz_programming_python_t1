"""
Начальная реализация классов, похожих на файлы, которые можно использовать для
перенаправления потоков ввода и вывода в графические интерфейсы;

входные данные поступают из стандартного диалога (единый интерфейс вывод+ввод или
постоянное поле Entry для ввода были бы удобнее);

кроме того, некорректно берутся строки в запросах входных данных, когда количество
байтов > len(строки);

в GuiInput можно было бы добавить методы __iter__/__next__, для поддержки итераций
по строкам, как в файлах, но это способствовало бы порождению большого количества
всплывающих окон;
"""
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.scrolledtext import ScrolledText


class GuiOutput:
    font = ('courier', 9, 'normal')  # в классе – для всех, self – для одного

    def __init__(self, parent=None):
        self.text = None
        if parent:
            self.popupnow(parent)  # сейчас или при первой записи

    def popupnow(self, parent=None):  # сейчас в родителе, Toplevel потом
        if self.text:
            return
        self.text = ScrolledText(parent or Toplevel())
        self.text.config(font=self.font)
        self.text.pack()

    def write(self, text):
        self.popupnow()
        self.text.insert(END, str(text))
        self.text.see(END)
        self.text.update()  # обновлять после каждой строки

    def writelines(self, lines):  # строки уже включают ‘\n’
        for line in lines:
            self.write(line)  # или map(self.write, lines)


class GuiInput:
    def __init__(self):
        self.buff = ''

    def inputLine(self):
        line = askstring('GuiInput', 'Enter input line + <crlf> (cancel=eof)')
        if line == None:
            return ''  # диалог для ввода каждой строки
        else:  # кнопка cancel означает eof
            return line + '\n'  # иначе добавить символ ‘\n’

    def read(self, bytes=None):
        if not self.buff:
            self.buff = self.inputLine()
        if bytes:  # читать по счетчику байтов,
            text = self.buff[:bytes]  # чтобы не захватить лишние строки
            self.buff = self.buff[bytes:]
        else:
            text = ''  # читать до eof
            line = self.buff
            while line:
                text = text + line
                line = self.inputLine()  # до cancel=eof=’’
        return text

    def readline(self):
        text = self.buff or self.inputLine()  # имитировать методы чтения файла
        self.buff = ''
        return text

    def readlines(self):
        lines = []  # читать все строки
        while True:
            next = self.readline()
            if not next:
                break
            lines.append(next)
        return lines


def redirectedGuiFunc(func, *pargs, **kargs):
    import sys  # отображает потоки функции
    saveStreams = sys.stdin, sys.stdout  # во всплывающие окна
    sys.stdin = GuiInput()  # выводит диалог при необходимости
    sys.stdout = GuiOutput()  # новое окно для каждого вызова
    sys.stderr = sys.stdout
    result = func(*pargs, **kargs)  # это блокирующий вызов
    sys.stdin, sys.stdout = saveStreams
    return result


def redirectedGuiShellCmd(command):
    import os
    input = os.popen(command, 'r')
    output = GuiOutput()

    def reader(input, output):  # показать стандартный вывод
        while True:  # команды оболочки в новом
            line = input.readline()  # окне с виджетом Text;
            if not line:
                break  # вызов readline может
            output.write(line)  # блокироваться

    reader(input, output)


if __name__ == '__main__':  # код самотестирования
    def makeUpper():  # использовать стандартные потоки
        while True:  # ввода-вывода
            try:
                line = input('Line? ')
            except:
                break
            print(line.upper())
        print('end of file')


    def makeLower(input, output):  # использовать файлы
        while True:
            line = input.readline()
            if not line:
                break
            output.write(line.lower())
        print('end of file')


    root = Tk()
    Button(root, text='test streams',
           command=lambda: redirectedGuiFunc(makeUpper)).pack(fill=X)
    Button(root, text='test files ',
           command=lambda: makeLower(GuiInput(), GuiOutput())).pack(fill=X)
    Button(root, text='test popen ',
           command=lambda: redirectedGuiShellCmd('dir *')).pack(fill=X)
    root.mainloop()
