class ProductWithGetSet:
    """Клас для представлення продукту з методами сеттера та геттера для ціни."""

    def __init__(self, name: str, price: float):
        """
        Ініціалізація продукту.

        :param name: Назва продукту.
        :param price: Ціна продукту.
        """
        if not name:
            raise ValueError("Name cannot be empty.")
        self.name = name
        self._price = None
        self.set_price(price)

    def get_price(self) -> float:
        """Отримати ціну продукту."""
        return self._price

    def set_price(self, price: float):
        """Встановити ціну продукту."""
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self._price = price

    def __repr__(self) -> str:
        return f'{self.name} - {self._price}'


class ProductWithProperty:
    """Клас для представлення продукту з використанням декоратора @property для ціни."""

    def __init__(self, name: str, price: float):
        """Ініціалізація продукту."""
        if not name:
            raise ValueError("Name cannot be empty.")
        self.name = name
        self._price = None
        self.price = price  # Використовуємо сеттер

    @property
    def price(self) -> float:
        """Отримати ціну продукту."""
        return self._price

    @price.setter
    def price(self, value: float):
        """Встановити ціну продукту."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    def __repr__(self) -> str:
        return f'{self.name} - {self._price}'


class PriceDescriptor:
    """Дескриптор для контролю доступу до ціни продукту."""

    def __get__(self, instance, owner):
        """Отримати ціну продукту."""
        return instance._price

    def __set__(self, instance, value):
        """Встановити ціну продукту."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        instance._price = value


class ProductWithDescriptor:
    """Клас для представлення продукту з використанням дескриптора для ціни."""

    price = PriceDescriptor()

    def __init__(self, name: str, price: float):
        """Ініціалізація продукту."""
        if not name:
            raise ValueError("Name cannot be empty.")
        self.name = name
        self._price = None
        self.price = price

    def __repr__(self) -> str:
        return f'{self.name} - {self.price}'


# Testing the classes
product = ProductWithGetSet('Test', 100.0)
print(product)
product.set_price(200.0)
print(product)

product_prop = ProductWithProperty('Sample', 150.0)
print(product_prop)
product_prop.price = 250.0
print(product_prop)

product_desc = ProductWithDescriptor('Example', 300.0)
print(product_desc)
product_desc.price = 400.0
print(product_desc)
