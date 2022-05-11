# упаковывает текстовые файлы в единый файл, добавляя строки-разделители
# (простейшая архивация)

import sys, glob
marker = ':' * 20 + 'textpak=>'      # надеемся, что это уникальная строка

def pack(ofile, ifiles):
    output = open(ofile, 'w')
    for name in ifiles:
        print('packing:', name)
        input = open(name, 'r').read()        # открыть следующий входной файл
        if input[-1] != '\n': input += '\n'   # гарантировать наличие \n в конце
        output.write(marker + name + '\n')    # записать строку-разделитель
        output.write(input)                   # и содержимое входного файла

if __name__ == '__main__':
    ifiles = []
    for patt in sys.argv[2:]:               # в Windows не выполняется автоматическая
        ifiles += glob.glob(patt)           # подстановка по шаблону
    pack(sys.argv[1], ifiles)               # упаковать файлы, перечисленные в командной строке