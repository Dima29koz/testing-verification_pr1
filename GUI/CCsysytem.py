from tkinter import *

from number_systems.CCcalc import calculate
from number_systems.CCOld_CCNew import translator

operand1 = ''
base1 = 0
operand2 = ''
base2 = 0
operation = ''

number = ''
from_base = 0
to_base = 0


class CC:
    def __init__(self, canvas):
        self._gue_CC(canvas)

    def _gue_CC(self, canvas):
        def _click1():
            global operand1
            operand1 = txt1.get()
            global base1
            base1 = int(txt2.get())
            global operand2
            operand2 = txt3.get()
            global base2
            base2 = int(txt4.get())
            global operation
            operation = txt5.get()
            if calculate(operand1, base1, operand2, base2, operation) == 'Ошибка!':
                label1['text'] = 'Ошибка!'
            else:
                label1['text'] = str(calculate(operand1, base1, operand2, base2, operation)) + ' в 10'

        def _click2():
            global number
            number = txt6.get()
            global from_base
            from_base = int(txt7.get())
            global to_base
            to_base = int(txt8.get())
            if translator(number, from_base, to_base) == 'Ошибка!':
                label2['text'] = 'Ошибка!'
            else:
                label2['text'] = str(translator(number, from_base, to_base)) + ' в ' + str(to_base)

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
        _label = Label(canvas, text='')
        _label.grid(row=3, column=0)
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
        button1 = Button(canvas, text='Вычислить', command=_click1)
        button1.grid(row=1, column=1, sticky="nsew")
        button2 = Button(canvas, text='Вычислить', command=_click2)
        button2.grid(row=5, column=1, sticky="nsew")
