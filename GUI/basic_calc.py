from tkinter import *
from functools import partial

from basic_calculator.calcs import calculate


class Calc:
    def __init__(self, canvas):
        self._activeStr = ''
        self._gui_calc(canvas)

    def _gui_calc(self, canvas):
        buttons = (
            ('AC', '<-', '%', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('switch', '0', '.', '=')
        )
        stack = []
        label = Label(canvas, text='0', width=50)
        label.grid(row=0, column=0, columnspan=4, rowspan=2)

        for row_idx, row in enumerate(buttons):
            for col_idx, btn in enumerate(row):
                button = Button(canvas, text=btn,
                                command=partial(self._click, btn, label, stack))
                button.grid(row=row_idx + 3, column=col_idx, sticky="nsew")

    def _click(self, text, label: Label, stack):
        # btn_text_to_action = {}
        if text == 'AC':
            stack.clear()
            self._activeStr = ''
            label.configure(text='0')
        elif text == '<-':
            if len(self._activeStr) > 1:
                self._activeStr = self._activeStr[:-1]
                label.configure(text=self._activeStr)
            else:
                label.configure(text='0')
        elif '0' <= text <= '9':
            self._activeStr += text
            label.configure(text=self._activeStr)
        elif text == '.':
            if self._activeStr.find('.') == -1:
                self._activeStr += text
                label.configure(text=self._activeStr)
        else:
            if len(stack) >= 2:
                stack.append(label['text'])
                label.configure(text=str(calculate(stack)))
                stack.clear()
                stack.append(label['text'])
                self._activeStr = ''
                if text != '=':
                    stack.append(text)
            else:
                if text != '=':
                    stack.append(label['text'])
                    stack.append(text)
                    self._activeStr = ''
                    # label.configure(text='0')
