def translator(number, from_base, to_base):
    try:
        n = int(number, from_base) if isinstance(number, str) else number
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while n > 0:
            n, m = divmod(n, to_base)
            result += alphabet[m]
        return result[::-1]
    except ValueError:
        return 'Ошибка!'

# class TrancNew(object):
#     def __init__(self, num, to_base, from_base):
#         self.num = num
#         self.to_base = to_base
#         self.from_base = from_base
#     def convert_base(self):
#         n = int(self.num, self.from_base) if isinstance(self.num, str) else self.num
#         alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         res = ""
#         while n > 0:
#             n, m = divmod(n, self.to_base)
#             res += alphabet[m]
#         return res[::-1]
# def Main(num, from_base, to_base):
#     start = TrancNew(num, to_base, from_base)
#     try:
#         print(start.convert_base())
#     except ValueError:
#         print('Числовая ошибка!')
#     except Exception:
#         print('Что ты сделал вообще?')
