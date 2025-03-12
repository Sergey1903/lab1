from abc import ABC, abstractmethod


class Furniture(ABC):
    """
    Абстрактный класс для представления мебели.

    Пример:
    >>> table = Furniture("wood", 10.5)  # TypeError, так как нельзя создать экземпляр абстрактного класса
    """

    def __init__(self, material: str, weight: float):
        """
        Инициализация объекта мебели.

        :param material: Материал, из которого изготовлена мебель.
        :param weight: Вес мебели в килограммах, должен быть положительным.
        :raises ValueError: Если вес неположительный.
        """
        if weight <= 0:
            raise ValueError("Вес должен быть положительным")

        self.material = material
        self.weight = weight

    @abstractmethod
    def assemble(self) -> None:
        """
        Метод для сборки мебели.
        """
        ...

    @abstractmethod
    def move(self, new_location: str) -> None:
        """
        Метод для перемещения мебели в новое место.

        :param new_location: Новое местоположение мебели.
        """
        ...


class Tree(ABC):
    """
    Абстрактный класс для представления дерева.

    Пример:
    >>> oak = Tree(5.2, 10)  # TypeError, так как нельзя создать экземпляр абстрактного класса
    """

    def __init__(self, height: float, age: int):
        """
        Инициализация объекта дерева.

        :param height: Высота дерева в метрах, должна быть положительной.
        :param age: Возраст дерева в годах, должен быть неотрицательным.
        :raises ValueError: Если высота неположительная или возраст отрицательный.
        """
        if height <= 0:
            raise ValueError("Высота должна быть положительной")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")

        self.height = height
        self.age = age

    @abstractmethod
    def grow(self, years: int) -> None:
        """
        Метод для роста дерева.

        :param years: Количество лет, на которое дерево растёт.
        """
        ...

    @abstractmethod
    def photosynthesize(self) -> None:
        """
        Метод для фотосинтеза.
        """
        ...


class SocialNetwork(ABC):
    """
    Абстрактный класс для представления социальной сети.

    Пример:
    >>> fb = SocialNetwork("Facebook", 3000000000)  # TypeError, так как нельзя создать экземпляр абстрактного класса
    """

    def __init__(self, name: str, user_count: int):
        """
        Инициализация социальной сети.

        :param name: Название социальной сети.
        :param user_count: Количество пользователей, должно быть неотрицательным.
        :raises ValueError: Если количество пользователей отрицательное.
        """
        if user_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")

        self.name = name
        self.user_count = user_count

    @abstractmethod
    def register_user(self, username: str) -> None:
        """
        Метод для регистрации нового пользователя.

        :param username: Имя пользователя.
        """
        ...

    @abstractmethod
    def post_message(self, message: str) -> None:
        """
        Метод для публикации сообщения.

        :param message: Текст сообщения.
        """
        ...
