from copy import copy
from functools import partial
from tkinter import *

from basic_calculator.calcs import calculate


class Calc:
    def __init__(self, canvas):
        self._activeStr = ''
        self.stack = []
        self._gui_calc(canvas)
        self.label_input = Label(canvas, text='0', width=50)
        self.label_input.grid(row=0, column=0, columnspan=4)
        self.label_result = Label(canvas, text='', width=50, anchor='e')
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
                button = Button(canvas, text=btn, bd=5, command=partial(self._click, btn))
                button.grid(row=row_idx + 4, column=col_idx, sticky="nsew", padx=2, pady=2)

    def _click(self, text):
        if text == 'switch':
            pass
        if text == 'AC':
            self.stack.clear()
            self._activeStr = ''
        elif text == '<-':
            if len(self._activeStr) > 0:
                self._activeStr = self._activeStr[:-1]
                if len(self._activeStr) == 0:
                    self._activeStr = self.stack.pop() if self.stack else ''
            else:
                if len(self.stack) > 0:
                    self._activeStr = self.stack.pop()
                    self._activeStr = self._activeStr[:-1]
        elif '0' <= text <= '9':
            if self._activeStr in ['/', '*', '-', '+']:
                self.stack.append(self._activeStr)
                self._activeStr = ''
            if self._activeStr == '0':
                self._activeStr = text
            else:
                self._activeStr += text
        elif text == '.':
            if self._activeStr in ['/', '*', '-', '+']:
                self.stack.append(self._activeStr)
                self._activeStr = ''
            if self._activeStr.find('.') == -1:
                self._activeStr += text
        elif text == '%':
            if self._activeStr and self._activeStr not in ['/', '*', '-', '+']:
                self._activeStr = calculate([self._activeStr, '/', '100'])
        elif text in ['/', '*', '-', '+']:
            if self._activeStr:
                if self._activeStr not in ['/', '*', '-', '+']:
                    self.stack.append(self._activeStr)
                self._activeStr = text
            else:
                if text == '-':
                    self._activeStr = text
        elif text == '=':
            self.stack.append(self._activeStr)
            res = calculate(self.stack)
            self._activeStr = res if not res.startswith('#') else ''
            self.stack.clear()

        self.label_input.configure(text=self.get_input_str())
        self.label_result.configure(text=self.get_dyn_res())

    def get_input_str(self) -> str:
        input_str = ''.join(self.stack) + self._activeStr
        return input_str if input_str else '0'

    def get_dyn_res(self) -> str:
        if not self.stack and not self._activeStr:
            return ''
        tmp_stack = copy(self.stack)
        if self._activeStr:
            tmp_stack.append(self._activeStr)

        result_str = calculate(tmp_stack) if tmp_stack else ''

        if result_str.startswith('#'):
            return result_str[1:]
        else:
            return '= ' + result_str if result_str else '='
