from tkinter import *
from functools import partial

from basic_calculator.calcs import calculate


class Calc:
    def __init__(self, canvas):
        self._activeStr = ''
        self._gui_calc(canvas)
        self.label_input = Label(canvas, text='0', width=50)
        self.label_input.grid(row=0, column=0, columnspan=4, rowspan=2)

    def _gui_calc(self, canvas):
        buttons = (
            ('AC', '<-', '%', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('switch', '0', '.', '=')
        )
        stack = []

        for row_idx, row in enumerate(buttons):
            for col_idx, btn in enumerate(row):
                button = Button(canvas, text=btn,
                                command=partial(self._click, btn, stack))
                button.grid(row=row_idx + 3, column=col_idx, sticky="nsew")

    def _click(self, text, stack: list):
        if text == 'switch':
            pass  # todo
        if text == 'AC':
            stack.clear()
            self._activeStr = ''
        elif text == '<-':
            if len(self._activeStr) > 0:
                self._activeStr = self._activeStr[:-1]
            else:
                if len(stack) > 0:
                    self._activeStr = stack.pop()
        elif '0' <= text <= '9':
            if self._activeStr in ['/', '*', '-', '+']:
                stack.append(self._activeStr)
                self._activeStr = ''
            self._activeStr += text
        elif text == '.':
            if self._activeStr in ['/', '*', '-', '+']:
                stack.append(self._activeStr)
                self._activeStr = ''
            if self._activeStr.find('.') == -1:
                self._activeStr += text
        elif text == '%':
            self._activeStr = str(calculate([self._activeStr, '/', '100']))
        elif text in ['/', '*', '-', '+']:
            if self._activeStr:
                if self._activeStr not in ['/', '*', '-', '+']:
                    stack.append(self._activeStr)
                    self._activeStr = text
                else:
                    self._activeStr = text
            else:
                if text == '-':
                    self._activeStr = text
        elif text == '=':
            stack.append(self._activeStr)
            self._activeStr = calculate(stack)
            stack.clear()

        input_str = ''.join(stack) + self._activeStr
        self.label_input.configure(text=input_str if input_str else '0')

        # # btn_text_to_action = {}
        # if text == 'AC':
        #     stack.clear()
        #     self._activeStr = ''
        #     self.label_input.configure(text='0')
        # elif text == '<-':
        #     if len(self._activeStr) > 1:
        #         self._activeStr = self._activeStr[:-1]
        #         self.label_input.configure(text=self._activeStr)
        #     else:
        #         self.label_input.configure(text='0')
        # elif '0' <= text <= '9':
        #     self._activeStr += text
        #     self.label_input.configure(text=self._activeStr)
        # elif text == '.':
        #     if self._activeStr.find('.') == -1:
        #         self._activeStr += text
        #         self.label_input.configure(text=self._activeStr)
        # else:
        #     if len(stack) >= 2:
        #         stack.append(self._activeStr)
        #         self.label_input.configure(text=str(calculate(stack)))
        #         stack.clear()
        #         stack.append(self.label_input['text'])
        #         self._activeStr = ''
        #         if text != '=':
        #             stack.append(text)
        #     else:
        #         if text != '=':
        #             stack.append(self.label_input['text'])
        #             stack.append(text)
        #             self._activeStr = ''
        #             # label.configure(text='0')
