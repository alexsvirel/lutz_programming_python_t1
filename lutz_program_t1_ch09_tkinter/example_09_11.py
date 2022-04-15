"""
Сохранение в файл, удаление и вставка текста и поиск строки

За счет наследования добавляет в ScrolledText типичные инструменты редактирования;
аналогичного результата можно было бы добиться, применив прием композиции (встраивания);
ненадежно!
"""
from tkinter import *
from tkinter.simpledialog import askstring
from tkinter.filedialog import asksaveasfilename

from lutz_program_t1_ch08_tkinter.examples.quitter import Quitter
from example_09_10 import ScrolledText
