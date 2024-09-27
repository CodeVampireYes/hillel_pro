import re

class User:
    """
    Клас для представлення користувача з атрибутами:
        first_name (str): Ім'я користувача.
        last_name (str): Прізвище користувача.
        email (str): Email-адреса користувача.
    """

    def __init__(self, first_name: str, last_name: str, email: str):
        """
        Ініціалізує об'єкт User.

        Аргументи:
            first_name (str): Ім'я користувача.
            last_name (str): Прізвище користувача.
            email (str): Email-адреса користувача.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @property
    def first_name(self) -> str:
        """Повертає ім'я користувача."""
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        """Встановлює ім'я користувача."""
        self._first_name = value

    @property
    def last_name(self) -> str:
        """Повертає прізвище користувача."""
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        """Встановлює прізвище користувача."""
        self._last_name = value

    @property
    def email(self) -> str:
        """Повертає email-адресу користувача."""
        return self._email

    @email.setter
    def email(self, value: str):
        """Встановлює email-адресу користувача, перевіряючи формат."""
        if not self.validate_email(value):
            raise ValueError("Невірний формат email-адреси.")
        self._email = value

    @staticmethod
    def validate_email(email: str) -> bool:
        """Перевіряє, чи є email-адреса у правильному форматі.

        Аргументи:
            email (str): Email-адреса для перевірки.

        Повертає:
            bool: True, якщо формат правильний, інакше False.
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None
