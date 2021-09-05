from decimal import Decimal


def calculate(stack: list):
    operators = ['*', '/', '+', '-']
    for operator in operators:
        while operator in stack:
            stack = _calc(stack, operator)
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
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2

    stack.insert(operation_idx - 1, str(result))
    return stack
