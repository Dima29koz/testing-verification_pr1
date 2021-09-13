import string


def calculate(operand1: str, base1: str, operand2: str, base2: str, operation: str) -> str:
    res = _calc(operand1, base1, operand2, base2, operation)
    if res.startswith('#'):
        return res
    return str(int(float(res))) if int(float(res)) == float(res) else str(res)


def _calc(operand1: str, base1: str, operand2: str, base2: str, operation: str):
    try:
        base1 = int(base1)
        base2 = int(base2)
        if base1 == 0 or base2 == 0:
            raise ValueError
        operand1_10 = int(operand1, base=base1)
        operand2_10 = int(operand2, base=base2)
    except ValueError:
        return '#Ошибка ввода!'
    else:
        try:
            if operation == '+':
                return str(operand1_10 + operand2_10)
            if operation == '-':
                return str(operand1_10 - operand2_10)
            if operation == '/':
                return str(f"{(operand1_10 / operand2_10):.{1}f}")
            if operation == '*':
                return str(operand1_10 * operand2_10)
            else:
                return '#Данное действие не поддерживается!'
        except ZeroDivisionError:
            return '#Деление на ноль!'


def translator(number: str, from_base: str, to_base: str) -> str:
    try:
        from_base = int(from_base)
        to_base = int(to_base)
        number = int(number, base=from_base)
    except ValueError:
        return '#Ошибка ввода!'
    else:
        alphabet = string.digits + string.ascii_uppercase
        if to_base > len(alphabet):
            return f'#Осн. не принадлежит [2:{len(alphabet)}]!'
        try:
            result = ""
            while number > 0:
                number, mod = divmod(number, to_base)
                result += alphabet[mod]
            return result[::-1]
        except ValueError:
            return '#Ошибка!'
