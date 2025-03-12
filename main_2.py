BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book

class Book:
    """
    Класс, представляющий книгу.

    Атрибуты:
    - id: идентификатор книги (int)
    - name: название книги (str)
    - pages: количество страниц (int)
    """

    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация экземпляра книги.

        :param id_: Идентификатор книги, должен быть положительным.
        :param name: Название книги, не может быть пустым.
        :param pages: Количество страниц, должно быть положительным.
        :raises ValueError: Если переданы некорректные данные.
        """
        if id_ <= 0:
            raise ValueError("ID книги должен быть положительным")
        if not name:
            raise ValueError("Название книги не может быть пустым")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")

        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.

        :return: Строка в формате 'Книга "название_книги"'.
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно создать такой же экземпляр книги.

        :return: Строка в формате 'Book(id_=значение, name='значение', pages=значение)'.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
