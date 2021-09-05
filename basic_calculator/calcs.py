import decimal
from decimal import Decimal


def calculate(stack: list):
    if stack[-1] == '':
        stack.pop()

    operators = ['*', '/', '+', '-']
    if stack[-1] in operators:
        return calculate(stack[:-1])

    for operator in operators:
        while operator in stack:
            try:
                stack = _calc(stack, operator)
            except decimal.DivisionByZero:
                return '#Деление на 0'
    return stack[0]


def _calc(stack: list, current_operator: str):
    operation_idx = stack.index(current_operator)

    operand1 = Decimal(stack[operation_idx - 1])
    operand2 = Decimal(stack[operation_idx + 1])
    operation = current_operator
    result = 0
    for _ in range(3):
        stack.pop(operation_idx - 1)
    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        try:
            result = operand1 / operand2
        except decimal.DivisionByZero:
            raise
    if operation == '*':
        result = operand1 * operand2

    stack.insert(operation_idx - 1, str(result))
    return stack
