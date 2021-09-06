from tkinter import *

from number_systems.CCcalc import calculate, translator


class CC:
    def __init__(self, canvas):
        self._gui_number_systems(canvas)

    def _gui_number_systems(self, canvas):
        frame1 = Frame(canvas)
        frame2 = Frame(canvas)

        frame1.grid(pady=10, sticky='nsew')
        frame2.grid(pady=10, sticky='nsew')

        self._cc_calculate(frame1)
        self._cc_translate(frame2)

    @staticmethod
    def _cc_calculate(frame):
        def _click():
            try:
                operation = op[box1.curselection()[0]]
            except IndexError:
                label1['text'] = 'Выбирите действие!'
            else:
                result = calculate(operand1.get(), base1.get(), operand2.get(), base2.get(), operation)
                if result == 'Ошибка!':
                    label1['text'] = 'Ошибка!'
                else:
                    label1['text'] = result + ' в 10'

        inputs = Frame(frame)
        inputs.pack(fill='both', expand=True)
        inputs1 = Frame(inputs)
        inputs1.pack(side=LEFT, fill='both', expand=True)
        inputs2 = Frame(inputs)
        inputs2.pack(side=LEFT, fill='both', expand=True)
        res = Frame(frame)
        res.pack(fill='both', expand=True)

        l_operand1 = Label(inputs1, text='число1')
        l_operand1.pack(side=TOP, fill='both', expand=True)
        operand1 = Entry(inputs1)
        operand1.pack(side=TOP, fill='both', expand=True)
        l_operand2 = Label(inputs1, text='число2')
        l_operand2.pack(side=TOP, fill='both', expand=True)
        operand2 = Entry(inputs1)
        operand2.pack(side=TOP, fill='both', expand=True)

        l_base1 = Label(inputs2, text='осн')
        l_base1.pack(side=TOP, fill='both', expand=True)
        base1 = Entry(inputs2, width=5)
        base1.pack(side=TOP, fill='both', expand=True)
        l_base2 = Label(inputs2, text='осн')
        l_base2.pack(side=TOP, fill='both', expand=True)
        base2 = Entry(inputs2, width=5)
        base2.pack(side=TOP, fill='both', expand=True)

        box1 = Listbox(inputs, selectmode=SINGLE, height=4, width=2)
        box1.pack(side=LEFT, fill='both', expand=True)
        op = ['+', '-', '*', '/']
        for elem in op:
            box1.insert(END, elem)

        button1 = Button(res, text='Вычислить', command=_click)
        button1.pack(side=LEFT, fill='both', expand=True)

        label1 = Label(res, text='0')
        label1.pack(side=LEFT, fill='both', expand=True)

    @staticmethod
    def _cc_translate(frame):
        def _click():
            result = translator(number.get(), from_base.get(), to_base.get())
            if result == 'Ошибка!':
                label2['text'] = 'Ошибка!'
            else:
                label2['text'] = result + ' в ' + str(to_base.get())

        inputs = Frame(frame)
        inputs.pack(fill='both', expand=True)
        inputs1 = Frame(inputs)
        inputs1.pack(side=LEFT, fill='both', expand=True)
        inputs2 = Frame(inputs)
        inputs2.pack(side=LEFT, fill='both', expand=True)
        inputs3 = Frame(inputs)
        inputs3.pack(side=LEFT, fill='both', expand=True)
        res = Frame(frame)
        res.pack(fill='both', expand=True)

        l_number = Label(inputs1, text='число')
        l_number.pack(fill='both', expand=True)
        number = Entry(inputs1)
        number.pack(fill='both', expand=True)
        l_from_base = Label(inputs2, text='осн')
        l_from_base.pack(fill='both', expand=True)
        from_base = Entry(inputs3, width=5)
        from_base.pack(fill='both', expand=True)
        l_to_base = Label(inputs2, text='н. осн')
        l_to_base.pack(fill='both', expand=True)
        to_base = Entry(inputs3, width=5)
        to_base.pack(fill='both', expand=True)

        button2 = Button(res, text='Вычислить', command=_click)
        button2.pack(side=LEFT, fill='both', expand=True)

        label2 = Label(res, text=' ')
        label2.pack(side=LEFT, fill='both', expand=True)
