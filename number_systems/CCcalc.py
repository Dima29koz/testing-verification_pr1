from decimal import Decimal


def calculate(operand1, base1, operand2, base2, operation):
    return _calc(operand1, base1, operand2, base2, operation)


def _calc(operand1, base1, operand2, base2, operation):
    try:
        if operation == '+':
            result = Decimal(int(operand1, base=base1) + int(operand2, base=base2))
            return result
        if operation == '-':
            result = Decimal(int(operand1, base=base1) - int(operand2, base=base2))
            return result
        if operation == '/':
            result = Decimal(int(operand1, base=base1) / int(operand2, base=base2))
            return result
        if operation == '*':
            result = Decimal(int(operand1, base=base1) * int(operand2, base=base2))
            return result
        else:
            return 'Ошибка!'
    except ValueError:
        return 'Ошибка!'

# class Calc(object):
#     def __init__(self, a, a_, b, b_, c):
#         self.a = a
#         self.a_ = a_
#         self.b = b
#         self.b_ = b_
#         self.c = c
#     def Calc(self):
#         if self.c == '+':
#             return int(self.a, base=self.a_)+int(self.b, base=self.b_)
#         if self.c == '-':
#             return int(self.a, base=self.a_)-int(self.b, base=self.b_)
#         if self.c == '*':
#             return int(self.a, base=self.a_)*int(self.b, base=self.b_)
#         if self.c == '/':
#             return int(self.a, base=self.a_)/int(self.b, base=self.b_)
# def Main(a, a_, b, b_, c):
#     start = Calc(a, a_, b, b_, c)
#     try:
#         print(start.Calc())
#     except ValueError:
#         print('Числовая ошибка!')
#     except Exception:
#         print('Что ты сделал вообще?')
