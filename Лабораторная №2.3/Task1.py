class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if isinstance(value, int) and value > 0:
            self._pages = value
        else:
            raise ValueError("Страницы должны быть положительным числом")

    def __str__(self):
        return f"{super().__str__()}, {self.pages} страницы"


def __repr__(self):
    return f"PaperBook('{self.name}', '{self.author}', {self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if isinstance(value, float) and value > 0.0:
            self._duration = value
        else:
            raise ValueError("Продолжительность должна быть формата числа с плавающей запятой")

    def __str__(self):
        return f"{super().__str__()}, {self.duration} часов"

    def __repr__(self):
        return f"AudioBook('{self.name}', '{self.author}', {self.duration})"
