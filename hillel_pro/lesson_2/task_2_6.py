def create_calculator(operation: str):
    def add_operation(operand1: int | float, operand2: int | float) -> int | float:
        return operand1 + operand2

    def sub_operation(operand1: int | float, operand2: int | float) -> int | float:
        return operand1 - operand2

    def mul_operation(operand1: int | float, operand2: int | float) -> int | float:
        return operand1 * operand2

    def division_operation(operand1: int | float, operand2: int | float) -> int | float | str:
        if operand2 == 0:
            return 'ділити на нуль не можна'
        return operand1 / operand2

    if operation == '+':
        return add_operation
    elif operation == '-':
        return sub_operation
    elif operation == '*':
        return mul_operation
    elif operation == '/':
        return division_operation


result = create_calculator('/')(2, 7)
print(result)
