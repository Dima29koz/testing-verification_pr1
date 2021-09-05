from tkinter import *
import tkinter.ttk as ttk

from GUI.basic_calc import Calc
from GUI.CCsysytem import CC


class GUI:
    def __init__(self):
        window = Tk()
        window.title('Калькулятор')
        notebook = ttk.Notebook(window)
        notebook.pack(fill='both', expand='yes')

        frame1 = ttk.Frame(notebook)
        frame2 = ttk.Frame(notebook)
        frame3 = ttk.Frame(notebook)
        frame1.pack(fill='both', expand=True)
        frame2.pack(fill='both', expand=True)
        frame3.pack(fill='both', expand=True)

        notebook.add(frame1, text='Обычный калькулятор')
        notebook.add(frame2, text='Системы счисления')
        notebook.add(frame3, text='Определитель числа')

        Calc(frame1)
        CC(frame2)
        # add here your code

        window.mainloop()
