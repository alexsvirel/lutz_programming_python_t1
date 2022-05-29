# графический интерфейс: перенаправляет стандартный вывод порождаемой
# программы в окно GUI
# GUI reader side: route spawned program standard output to a GUI window

# from example_10_12 import redirectedGuiShellCmd             # использует GuiOutput
from example_10_12 import *
redirectedGuiShellCmd('python -u examples/pipe-nongui.py')  # -u: без буферизации
# ключ -u командной строки интерпретатора # Python, используемый здесь,
# принудительно отключает буферизацию потока стандартного вывода запускаемой
# программы, поэтому мы получаем печатаемый текст немедленно и нам не приходится
# ждать завершения дочерней программы