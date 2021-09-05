from decimal import Decimal

def calc(a, _a, b, _b, c):
    return _calc(a, _a, b, _b, c)

def _calc(a, _a, b, _b, c):
    if c == '+':
        result = Decimal(int(a, base=_a) + int(b, base=_b))
    if c == '-':
        result = Decimal(int(a, base=_a) - int(b, base=_b))
    if c == '/':
        result = Decimal(int(a, base=_a) / int(b, base=_b))
    if c == '*':
        result = Decimal(int(a, base=_a) * int(b, base=_b))
    return result


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