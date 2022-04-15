"""
учимся управлять положением виджета в окне
"""
from tkinter import *

Label(text='Hello GUI world!').pack(expand=YES, fill=BOTH)  # метка посредине окна даже при его расширении
mainloop()
