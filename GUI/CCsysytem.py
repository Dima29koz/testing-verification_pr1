from tkinter import *
from functools import partial

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
    def _control_type(event, field: Entry):
        """Проверяет что вводимые данные являются числом"""
        data: str = field.get()
        if not data.isdigit() and data != '':
            result = ''
            for i in field.get():
                if i.isdigit():
                    result += i
            field.delete(0, END)
            field.insert(0, result)

    def _cc_calculate(self, frame):
        def _click():
            if '.' in str(operand1.get()):
                label1['text'] = 'Ошибка дробей!'
                return
            if '.' in str(operand2.get()):
                label1['text'] = 'Ошибка дробей!'
                return
            try:
                operation = op[box1.curselection()[0]]
            except IndexError:
                label1['text'] = 'Выбирите действие!'
            else:
                result = calculate(operand1.get(), base1.get(), operand2.get(), base2.get(), operation)
                if result == 'Ошибка!':
                    label1['text'] = 'Ошибка!'
                else:
                    label1['text'] = '= ' + result + ' в 10'

        inputs = Frame(frame)
        inputs.pack(fill='both', expand=True)
        inputs1 = Frame(inputs)
        inputs1.pack(side=LEFT, fill='both', expand=True)
        inputs2 = Frame(inputs)
        inputs2.pack(side=LEFT, fill='both', expand=True)
        res = Frame(frame)
        res.pack(fill='both', expand=True)

        l_operand1 = Label(inputs1, text='Число 1')
        l_operand1.pack(side=TOP, fill='both', expand=True)
        operand1 = Entry(inputs1)
        operand1.pack(side=TOP, fill='both', expand=True)
        l_operand2 = Label(inputs1, text='Число 2')
        l_operand2.pack(side=TOP, fill='both', expand=True)
        operand2 = Entry(inputs1)
        operand2.pack(side=TOP, fill='both', expand=True)

        l_base1 = Label(inputs2, text='осн')
        l_base1.pack(side=TOP, fill='both', expand=True)
        base1 = Entry(inputs2, width=5)
        base1.bind("<Any-KeyRelease>", partial(self._control_type, field=base1))
        base1.pack(side=TOP, fill='both', expand=True)
        l_base2 = Label(inputs2, text='осн')
        l_base2.pack(side=TOP, fill='both', expand=True)
        base2 = Entry(inputs2, width=5)
        base2.bind("<Any-KeyRelease>", partial(self._control_type, field=base2))
        base2.pack(side=TOP, fill='both', expand=True)

        box1 = Listbox(inputs, selectmode=SINGLE, height=4, width=2, highlightthickness=7, selectbackground="green")
        box1.pack(side=LEFT, fill='both', expand=True)
        op = ['+', '-', '*', '/']
        for elem in op:
            box1.insert(END, elem)

        button1 = Button(res, text='Вычислить', command=_click, bd=5)
        button1.pack(side=LEFT, fill='both', expand=True)

        label1 = Label(res, text='= 0')
        label1.pack(side=LEFT, fill='both', expand=True)

    def _cc_translate(self, frame):
        def _click():
            if '.' in str(number.get()):
                label2['text'] = 'Ошибка дробей!'
                return
            result = translator(number.get(), from_base.get(), to_base.get())
            if result == 'Ошибка!':
                label2['text'] = 'Ошибка!'
            else:
                label2['text'] = '= ' + result + ' в ' + str(to_base.get())

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

        l_number = Label(inputs1, text='Число')
        l_number.pack(fill='both', expand=True)
        number = Entry(inputs1)
        number.pack(fill='both', expand=True)
        l_from_base = Label(inputs2, text='c. осн')
        l_from_base.pack(fill='both', expand=True)
        from_base = Entry(inputs3, width=5)
        from_base.bind("<Any-KeyRelease>", partial(self._control_type, field=from_base))
        from_base.pack(fill='both', expand=True)
        l_to_base = Label(inputs2, text='н. осн')
        l_to_base.pack(fill='both', expand=True)
        to_base = Entry(inputs3, width=5)
        to_base.bind("<Any-KeyRelease>", partial(self._control_type, field=to_base))
        to_base.pack(fill='both', expand=True)

        button2 = Button(res, text='Вычислить', command=_click, bd=5)
        button2.pack(side=LEFT, fill='both', expand=True)

        label2 = Label(res, text='= 0')
        label2.pack(side=LEFT, fill='both', expand=True)
