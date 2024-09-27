def len(obj: object) -> int:
    """
    Возвращает количество элементов в объекте, если он поддерживает __len__().
    Если метод __len__ отсутствует, подсчитывает элементы через итерацию.

    :param obj: Любой итерируемый объект (строка, список, кортеж, множество и т.д.)
    :return: Длина объекта (количество элементов)
    """
    if hasattr(obj, '__len__'):
        return obj.__len__()
    else:
        count = 0
        for _ in obj:
            count += 1
        return count


def sum(iterable: iter, start: int = 0) -> int:
    """
    Возвращает сумму элементов итерируемого объекта, начиная с значения start.

    :param iterable: Итерируемый объект, содержащий числовые элементы
    :param start: Начальное значение суммы (по умолчанию 0)
    :return: Сумма всех элементов iterable плюс начальное значение start
    """
    total = start
    for item in iterable:
        total += item
    return total


def min(*args: iter) -> object:
    """
    Возвращает минимальное значение из нескольких аргументов или итерируемого объекта.

    :param args: Либо один итерируемый объект, либо несколько отдельных элементов
    :return: Минимальное значение из элементов
    :raises ValueError: Если передан пустой итерируемый объект
    """
    if len(args) == 1:
        iterable = args[0]
        iterator = iter(iterable)
        try:
            minimum = next(iterator)
        except StopIteration:
            raise ValueError("my_min() arg is an empty sequence")
    else:
        iterator = iter(args)
        minimum = next(iterator)

    for item in iterator:
        if item < minimum:
            minimum = item
    return minimum


assert len([1, 2, 3]) == 3
assert len("hello") == 5
assert len((1, 2, 3, 4)) == 4
assert len({1, 2, 3}) == 3
assert len({'a': 1, 'b': 2}) == 2
print("len tests passed!")
assert sum((4, 5, 6), 10) == 25
print("sum tests passed!")
assert min([4, 2, 9, 1]) == 1
print("min tests passed!")
