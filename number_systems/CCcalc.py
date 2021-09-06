import string


def calculate(operand1, base1, operand2, base2, operation) -> str:
    return _calc(operand1, base1, operand2, base2, operation)


def _calc(operand1, base1, operand2, base2, operation):
    try:
        base1 = int(base1)
        base2 = int(base2)
        operand1_10 = int(operand1, base=base1)
        operand2_10 = int(operand2, base=base2)
    except ValueError:
        return 'Ошибка!'
    else:
        try:
            if operation == '+':
                return str(operand1_10 + operand2_10)
            if operation == '-':
                return str(operand1_10 - operand2_10)
            if operation == '/':
                return str(operand1_10 / operand2_10)
            if operation == '*':
                return str(operand1_10 * operand2_10)
            else:
                return 'Ошибка!'
        except ZeroDivisionError:
            return 'Ошибка!'


def translator(number: str, from_base: str, to_base: str) -> str:
    try:
        from_base = int(from_base)
        to_base = int(to_base)
    except ValueError:
        return 'Ошибка!'
    else:
        alphabet = string.digits + string.ascii_uppercase
        if to_base > len(alphabet):
            return 'Ошибка!'
        try:
            number = int(number, base=from_base)
            result = ""
            while number > 0:
                number, mod = divmod(number, to_base)
                result += alphabet[mod]
            return result[::-1]
        except ValueError:
            return 'Ошибка!'
