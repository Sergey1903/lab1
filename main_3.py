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


class Library:
    """
    Класс, представляющий библиотеку.

    Атрибуты:
    - books: список книг, хранящихся в библиотеке.
    """

    def __init__(self, books=None):
        """
        Инициализация библиотеки.

        :param books: Список книг. Если не передан, инициализируется пустым списком.
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает следующий доступный идентификатор для добавления новой книги.

        :return: Идентификатор для новой книги.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по её идентификатору.

        :param book_id: Идентификатор книги.
        :return: Индекс книги в списке.
        :raises ValueError: Если книги с таким идентификатором нет в библиотеке.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError(f"Книги с запрашиваемым id {book_id} не существует")


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
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
