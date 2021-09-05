from tkinter import *

from number_systems.CCcalc import calc
from number_systems.CCOld_CCNew import trancCC

a = ''
_a = 0
b = ''
_b = 0
c = ''

num = ''
old = 0
new = 0

class Calcul:
    def __init__(self, canvas):
        self._gue_CC(canvas)

    def _gue_CC(self, canvas):
        def _click():
            global a
            a = txt1.get()
            global _a
            _a = int(txt2.get())
            global b
            b = txt3.get()
            global _b
            _b = int(txt4.get())
            global c
            c = txt5.get()
            label1['text']=str(calc(a, _a, b, _b, c))+' в 10'

        def _click1():
            global num
            num = txt6.get()
            global old
            old = int(txt7.get())
            global new
            new = int(txt8.get())
            label2['text'] = str(trancCC(num, old, new)) + ' в ' + str(new)

        txt1 = Entry(canvas)
        txt1.grid(row=0, column=0)
        txt1.get()
        txt2 = Entry(canvas)
        txt2.grid(row=1, column=0)
        txt3 = Entry(canvas)
        txt3.grid(row=0, column=2)
        txt4 = Entry(canvas)
        txt4.grid(row=1, column=2)
        txt5 = Entry(canvas)
        txt5.grid(row=0, column=1)
        label = Label(canvas, text='')
        label.grid(row=3, column=0)
        txt6 = Entry(canvas)
        txt6.grid(row=4, column=0)
        txt7 = Entry(canvas)
        txt7.grid(row=4, column=1)
        txt8 = Entry(canvas)
        txt8.grid(row=4, column=2)
        label1 = Label(canvas, text='0')
        label1.grid(row=0, column=3)
        label2 = Label(canvas, text=' ')
        label2.grid(row=4, column=3)
        button1 = Button(canvas, text='Вычислить', command=_click)
        button1.grid(row=1, column=1, sticky="nsew")
        button2 = Button(canvas, text='Вычислить', command=_click1)
        button2.grid(row=5, column=1, sticky="nsew")
