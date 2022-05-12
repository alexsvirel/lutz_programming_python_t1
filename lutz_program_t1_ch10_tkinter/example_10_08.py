# распаковывает архивы, созданные сценарием example_10_07.py
# (простейшие архивы текстовых файлов)

import sys
from example_10_07 import marker             # использовать общую строку-разделитель
mlen = len(marker)                    # имена файлов следуют за строкой-разделителем

def unpack(ifile, prefix='new-'):
    for line in open(ifile):                # по всем строкам входного файла
        if line[:mlen] != marker:
            output.write(line)              # действительные строки записать
        else:
            name = prefix + line[mlen:-1]   # или создать новый выходной файл
            print('creating:', name)
            output = open(name, 'w')

if __name__ == '__main__': unpack(sys.argv[1])