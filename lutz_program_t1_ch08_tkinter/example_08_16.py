"""
Oсновы применения Message (метки)

Демонстрирует, как виджет Message реагирует на растягивание по горизонтали
с применением параметров fill и expand
"""
from tkinter import *

msg = Message(text="Oh by the way, with one's Pink?")
msg.config(bg='pink', font=('times', 16, 'italic'))
msg.pack(fill=X, expand=YES)
mainloop()
