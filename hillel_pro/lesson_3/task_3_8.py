class Price:
    """
    Клас для представлення ціни.

    Атрибути:
        amount (float): Значення ціни.

    Методи:
        __repr__(): Повертає рядкове представлення об'єкта Price.
        __add__(other): Додає дві ціни.
        __sub__(other): Віднімає одну ціну від іншої.
        __eq__(other): Перевіряє, чи дві ціни рівні.
        __lt__(other): Перевіряє, чи є ця ціна меншою за іншу.
        __gt__(other): Перевіряє, чи є ця ціна більшою за іншу.
    """
    def __init__(self, amount: float):
        self.amount = amount

    def __repr__(self) -> str:
        return f'{self.amount}'

    def __add__(self, other: 'Price') -> 'Price':
        return Price(round(self.amount + other.amount, 2))

    def __sub__(self, other: 'Price') -> 'Price':
        return Price(round(self.amount - other.amount, 2))

    def __eq__(self, other: 'Price') -> bool:
        return self.amount == other.amount

    def __lt__(self, other: 'Price') -> bool:
        return self.amount < other.amount

    def __gt__(self, other: 'Price') -> bool:
        return self.amount > other.amount


price1 = Price(1.9258)
price2 = Price(2.908)
price3 = price2 + price1
print(price3)
