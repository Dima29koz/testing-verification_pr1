def calculate(stack: list):
    if len(stack) == 0:
        return '0'
    if stack[-1] == '':
        stack.pop()
    operators = ['*', '/', '+', '-', '.']
    if stack[-1] in operators:
        return calculate(stack[:-1])

    return _calc(stack)


def _calc(stack: list) -> str:
    s = ''.join(stack)
    try:
        res = eval(s)
        return str(int(res)) if int(res) == res else ('%1.8f' % res).rstrip('.0')
    except ZeroDivisionError:
        return '#Деление на 0!'
