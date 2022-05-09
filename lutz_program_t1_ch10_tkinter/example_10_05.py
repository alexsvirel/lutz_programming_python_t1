#!/usr/local/bin/python
"""
##############################################################################
Инструмент запуска;

использует шаблоны GuiMaker, стандартный диалог завершения GuiMixin;
это просто библиотека классов:
чтобы вывести графический интерфейс, запустите сценарий mytools;
##############################################################################
"""
from tkinter import *
from example_10_02 import GuiMixin  # импортировать quit, а не done
from example_10_03 import *  # конструктор меню/панели инструментов

class ShellGui(GuiMixin, GuiMakerWindowMenu): # фрейм + конструктор + подмешиваемые методы
    """
    Класс ShellGui знает, как с помощью интерфейсов GuiMaker и GuiMixin создать
    окно для выбора, которое выводит имена утилит в меню, в списке с прокруткой
    и на панели инструментов. Он также предоставляет переопределяемый метод forToolBar,
    позволяющий подклассам указывать, какие утилиты должны добавляться на панель инструментов,
    а какие – нет (на панели инструментов может быстро закончиться свободное место).
    Однако он умышленно оставлен в неведении относительно имен утилит, которые должны
    быть выведены в указанных местах, и операций, которые должны быть выполнены при
    выборе имен утилит.
    Вместо этого класс ShellGui использует подклассы ListMenuGui и DictMenuGui,
    чтобы получить список имен утилит через их методы fetchCommands и управлять
    операциями по именам с помощью их методов runCommand.
    """
    def start(self):  #
        self.setMenuBar()  # для компонентов использовать GuiMaker
        self.setToolBar()
        self.master.title("Shell Tools Listbox")
        self.master.iconname("Shell Tools")

    def handleList(self, event):  # двойной щелчок на списке
        label = self.listbox.get(ACTIVE)  # получить выбранный текст
        self.runCommand(label)  # и выполнить операцию

    def makeWidgets(self):  # добавить список в середину
        sbar = Scrollbar(self)  # связать sbar со списком
        list = Listbox(self, bg='white')  # или использ. Tour.ScrolledList
        sbar.config(command=list.yview)
        list.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)  # первым добавлен = посл. обрезан
        list.pack(side=LEFT, expand=YES, fill=BOTH)  # список обрез-ся первым
        for (label, action) in self.fetchCommands():  # добавляется в список,
            list.insert(END, label)  # в меню и на панель инстр.
        list.bind('< Double - 1 >', self.handleList)  # установить обработчик
        self.listbox = list

    def forToolBar(self, label):  # поместить на панель инстр.?
        return True  # по умолчанию = все

    def setToolBar(self):
        self.toolBar = []
        for (label, action) in self.fetchCommands():
            if self.forToolBar(label):
                self.toolBar.append((label, action, dict(side=LEFT)))
        self.toolBar.append(('Quit', self.quit, dict(side=RIGHT)))

    def setMenuBar(self):
        toolEntries = []
        self.menuBar = [
            ('File', 0, [('Quit', -1, self.quit)]),  # имя раскрывающегося меню
            ('Tools', 0, toolEntries)  # список элементов меню
        ]  # метка,клавиша,обработчик
        for (label, action) in self.fetchCommands():
            toolEntries.append((label, -1, action))  # добавить приложения в меню


##############################################################################
# делегирование операций шаблонным подклассам с разным способом хранения # перечня утилит,
# которые в свою очередь делегируют операции подклассам, реализующим запуск утилит.
# Подклассы ListMenuGui и DictMenuGuiлишь предоставляют интерфейс к наборам утилит,
# представленным # в виде списков и словарей, – они по-прежнему не знают, какие имена
# утилит будут реально отображены в графическом интерфейсе. Это сделано умышленно:
# так как отображаемые наборы утилит определяются подклассами более низкого уровня,
# мы получаем возможность использовать класс ShellGui для отображения различных наборов утилит.
##############################################################################

class ListMenuGui(ShellGui):
    def fetchCommands(self): # myMenu устанавливается в подклассе
        return self.myMenu # список кортежей (метка, обработчик)

    def runCommand(self, cmd):
        for (label, action) in self.myMenu:
            if label == cmd: action()


class DictMenuGui(ShellGui):
    def fetchCommands(self):
        return self.myMenu.items()

    def runCommand(self, cmd):
        self.myMenu[cmd]()

