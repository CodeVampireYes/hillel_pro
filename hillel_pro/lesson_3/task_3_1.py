class Fraction:
    """
        Класс для работы с дробями.

        Атрибуты:
            a (int): Числитель дроби.
            b (int): Знаменатель дроби.

        Методы:
            __init__(a: int, b: int) -> None:
                Инициализирует объект класса Fraction с числителем a и знаменателем b.

            __mul__(other: 'Fraction') -> 'Fraction':
                Оператор умножения для дробей. Возвращает новую дробь, которая является результатом умножения двух дробей.

            __add__(other: 'Fraction') -> 'Fraction':
                Оператор сложения для дробей. Возвращает новую дробь, которая является результатом сложения двух дробей.

            __sub__(other: 'Fraction') -> 'Fraction':
                Оператор вычитания для дробей. Возвращает новую дробь, которая является результатом вычитания одной дроби из другой.

            __truediv__(other: 'Fraction') -> 'Fraction':
                Оператор деления для дробей. Возвращает новую дробь, которая является результатом деления одной дроби на другую.

            __repr__() -> str:
                Возвращает строковое представление дроби в формате "a/b".
        """
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __add__(self, other: 'Fraction') -> 'Fraction':
        new_a = (self.a * other.b) + (other.a * self.b)
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        new_a = self.a * other.b - self.b * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        new_a = self.a * other.b
        new_b = self.b * other.a
        return Fraction(new_a, new_b)

    def __repr__(self) -> str:
        return f'{self.a}/{self.b}'


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
print(f_a / f_b)
