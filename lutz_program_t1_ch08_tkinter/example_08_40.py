"""
Развлечения с кнопками и картинками
"""
from tkinter import *           # Импортировать базовый набор виджетов
from glob import glob           # Модуль glob позволяет получить список
                                # всех файлов с расширением .gif в каталоге
                                # иными словами, всех GIF-файлов, которые там хранятся.
import example_08_22            # Прикрепить дистанционный пример с флажками
import random                   # Выбрать случайную картинку из спитска всех GIF-файлов

gifdir = 'D:/Python/lutz/Programming_Python/PP4E-Examples-1.4/Examples/PP4E/Gui/gifs/' # каталог с GIF файлами

def draw():
    """
    Чтобы изменить отображаемое изображение (и имя GIF-файла в мет-
ке в верхней части окна), сценарий просто вызывает метод config
виджета с новыми значениями параметров – такое изменение дина-
мически изменяет вид графического элемента.
    """
    name, photo = random.choice(images)
    lbl.config(text=name)
    pix.config(image=photo)

root=Tk()
lbl = Label(root, text="none", bg='blue', fg='red')
pix = Button(root, text="Press me", command=draw, bg='white')
lbl.pack(fill=BOTH)
pix.pack(pady=10)

example_08_22.Demo(root, relief=SUNKEN, bd=2).pack(fill=BOTH)

files = glob(gifdir + "*.gif")                      # имеющиеся GIF-файлы
images = [(x, PhotoImage(file=x)) for x in files]   # загрузить и сохранить
print(files)
root.mainloop()



