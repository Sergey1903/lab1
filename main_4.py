class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс бумажной книги."""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга '{self.name}' ({self.pages} стр.). Автор: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """Класс аудиокниги."""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = float(value)

    def __str__(self):
        return f"Аудиокнига '{self.name}' ({self.duration} ч.). Автор: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


# Тестирование
if __name__ == "__main__":
    paper_book = PaperBook("Война и мир", "Лев Толстой", 1225)
    audio_book = AudioBook("1984", "Джордж Оруэлл", 12.5)

    print(paper_book)  # Бумажная книга 'Война и мир' (1225 стр.). Автор: Лев Толстой
    print(audio_book)  # Аудиокнига '1984' (12.5 ч.). Автор: Джордж Оруэлл

    print(repr(paper_book))  # PaperBook(name='Война и мир', author='Лев Толстой', pages=1225)
    print(repr(audio_book))  # AudioBook(name='1984', author='Джордж Оруэлл', duration=12.5)

