def calculate(stack: list):
    if len(stack) == 0:
        return '0'
    if stack[-1] == '':
        stack.pop()
    operators = ['*', '/', '+', '-', '.']
    if stack[-1] in operators:
        return calculate(stack[:-1])

    return _calc(stack)


def _calc(stack: list):
    s = ''.join(stack)
    try:
        return str(eval(s))
    except ZeroDivisionError:
        return '#Деление на 0!'
