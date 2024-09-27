class Person:
    """
        Клас представляє людину з іменем і віком.

        Атрибути:
        ----------
        name : str
            Ім'я людини.
        age : int
            Вік людини.

         Методи:
        ----------
         __init__(name: str, age: int):
            Ініціалізує новий об'єкт класу Person.
        __lt__(other: 'Person') -> bool:
            Порівнює вік двох об'єктів (менше).
        __eq__(other: 'Person') -> bool:
            Перевіряє рівність віку двох об'єктів.
        __gt__(other: 'Person') -> bool:
            Порівнює вік двох об'єктів (більше).
        __repr__() -> str:
            Повертає строкове представлення об'єкта.
        """
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __lt__(self, other: 'Person') -> bool:
        return bool(self.age < other.age)

    def __eq__(self, other: 'Person') -> bool:
        return bool(self.age == other.age)

    def __gt__(self, other: 'Person') -> bool:
        return bool(self.age > other.age)

    def __repr__(self):
        return f'{self.name}, {self.age}'


people = [
    Person('Artur', 27),
    Person('Mariia', 24),
    Person('Oleksandr', 26),
    Person('Ivan', 20)
]


print(people[0] > people[1])

sorted_people = sorted(people)
print(sorted_people)
