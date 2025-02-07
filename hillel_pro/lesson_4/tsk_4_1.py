class MyClass:
    def __init__(self, value: str) -> None:
        """
        Ініціалізує об'єкт класу MyClass.

        :param value: Значення, яке буде використовуватися в об'єкті.
        """
        self.value = value

    def say_hello(self) -> str:
        """
        Повертає вітальне повідомлення з використанням значення 'value'.

        :return: Повідомлення у форматі 'Hello, {value}'.
        """
        return f"Hello, {self.value}"


def analyze_object(obj: object) -> None:
    """
    Аналізує об'єкт: виводить його тип, список атрибутів і методів,
    а також тип кожного атрибута.

    :param obj: Об'єкт для аналізу.
    """
    type_obj = type(obj)
    print(f"Тип об'єкта: {type_obj}\n")
    attributes = dir(obj)
    filtr_attributes = [attr for attr in attributes if not attr.startswith('__')]
    print("Атрибути і методи:")
    for attr in filtr_attributes:
        value = getattr(obj, attr)
        print(f'- {attr}: {type(value)}')


obj = MyClass("World")
analyze_object(obj)
