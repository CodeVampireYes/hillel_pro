class Calculator:
    def add(self, a: int | float, b: int | float) -> int | float:
        return a + b

    def subtract(self, a: int | float, b: int | float) -> int | float:
        return a - b


def call_function(obj: object, method_name: str, *args):
    """
    Викликає метод об'єкта за його назвою та передає йому аргументи.

    :param obj: Об'єкт, метод якого буде викликаний.
    :param method_name: Назва методу у вигляді рядка.
    :param args: Довільні аргументи для методу.
    :return: Результат виконання методу.
    """
    method = getattr(obj, method_name, None)
    if callable(method):
        return method(*args)


calc = Calculator()
print(call_function(calc, "add", 10, 5))  # 15
print(call_function(calc, "subtract", 10, 5))  # 5
