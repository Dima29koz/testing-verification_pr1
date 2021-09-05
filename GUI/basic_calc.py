from copy import copy
from tkinter import *
from functools import partial

from basic_calculator.calcs import calculate


class Calc:
    def __init__(self, canvas):
        self._activeStr = ''
        self.stack = []
        self._gui_calc(canvas)
        self.label_input = Label(canvas, text='0', width=50)
        self.label_input.grid(row=0, column=0, columnspan=4)
        self.label_result = Label(canvas, text='=', width=50, anchor='e')
        self.label_result.grid(row=2, column=0, columnspan=4)

    def _gui_calc(self, canvas):
        buttons = (
            ('AC', '<-', '%', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('switch', '0', '.', '=')
        )

        for row_idx, row in enumerate(buttons):
            for col_idx, btn in enumerate(row):
                button = Button(canvas, text=btn,
                                command=partial(self._click, btn))
                button.grid(row=row_idx + 4, column=col_idx, sticky="nsew")

    def _click(self, text):
        if text == 'switch':
            pass  # todo
        if text == 'AC':
            self.stack.clear()
            self._activeStr = ''
        elif text == '<-':
            if len(self._activeStr) > 0:
                self._activeStr = self._activeStr[:-1]
            else:
                if len(self.stack) > 0:
                    self._activeStr = self.stack.pop()
                    self._activeStr = self._activeStr[:-1]
        elif '0' <= text <= '9':
            if self._activeStr in ['/', '*', '-', '+']:
                self.stack.append(self._activeStr)
                self._activeStr = ''
            self._activeStr += text
        elif text == '.':
            if self._activeStr in ['/', '*', '-', '+']:
                self.stack.append(self._activeStr)
                self._activeStr = ''
            if self._activeStr.find('.') == -1:
                self._activeStr += text
        elif text == '%':
            self._activeStr = str(calculate([self._activeStr, '/', '100']))
        elif text in ['/', '*', '-', '+']:
            if self._activeStr:
                if self._activeStr not in ['/', '*', '-', '+']:
                    self.stack.append(self._activeStr)
                    self._activeStr = text
                else:
                    self._activeStr = text
            else:
                if text == '-':
                    self._activeStr = text
        elif text == '=':
            self.stack.append(self._activeStr)
            self._activeStr = calculate(self.stack)
            self.stack.clear()

        input_str = ''.join(self.stack) + self._activeStr
        self.label_input.configure(text=input_str if input_str else '0')

        tmp_stack = copy(self.stack)
        if self._activeStr:
            tmp_stack.append(self._activeStr)
        if tmp_stack:
            result_str = calculate(tmp_stack)
        else:
            result_str = ''
        if result_str.startswith('#'):
            self.label_result.configure(text=result_str)
        else:
            self.label_result.configure(text='=' + result_str if result_str else '=')
