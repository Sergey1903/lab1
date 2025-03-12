class Vehicle:
    """
    Базовый класс для всех транспортных средств.

    Атрибуты:
    - brand (str): Марка транспортного средства.
    - model (str): Модель транспортного средства.
    - year (int): Год выпуска.
    """

    def __init__(self, brand: str, model: str, year: int):
        """
        Инициализирует транспортное средство.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        """
        self._brand = brand  # Инкапсуляция: марка автомобиля не должна изменяться после создания
        self._model = model  # Инкапсуляция: модель тоже неизменяема
        self.year = year

    @property
    def brand(self) -> str:
        """Возвращает марку автомобиля."""
        return self._brand

    @property
    def model(self) -> str:
        """Возвращает модель автомобиля."""
        return self._model

    def start_engine(self) -> str:
        """Метод для запуска двигателя."""
        return f"{self.brand} {self.model}: двигатель запущен."

    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        return f"{self.brand} {self.model} ({self.year} г.)"

    def __repr__(self) -> str:
        """Возвращает строку для воссоздания объекта."""
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, year={self.year})"


class Car(Vehicle):
    """
    Дочерний класс для легковых автомобилей.

    Дополнительные атрибуты:
    - passengers (int): Количество пассажиров.
    """

    def __init__(self, brand: str, model: str, year: int, passengers: int):
        """
        Инициализирует легковой автомобиль.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param passengers: Количество пассажиров.
        """
        super().__init__(brand, model, year)
        self.passengers = passengers

    def start_engine(self) -> str:
        """
        Перегруженный метод запуска двигателя.

        Причина перегрузки: в легковых автомобилях часто указывают количество посадочных мест.
        """
        return f"{self.brand} {self.model} ({self.passengers} мест): двигатель запущен."

    def __repr__(self) -> str:
        """Возвращает строку для воссоздания объекта."""
        return (f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, "
                f"year={self.year}, passengers={self.passengers})")


class Truck(Vehicle):
    """
    Дочерний класс для грузовых автомобилей.

    Дополнительные атрибуты:
    - load_capacity (float): Грузоподъёмность в тоннах.
    """

    def __init__(self, brand: str, model: str, year: int, load_capacity: float):
        """
        Инициализирует грузовик.

        :param brand: Марка грузовика.
        :param model: Модель грузовика.
        :param year: Год выпуска грузовика.
        :param load_capacity: Грузоподъёмность в тоннах.
        """
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

    def load_cargo(self, weight: float) -> str:
        """
        Метод для загрузки груза.

        :param weight: Вес груза в тоннах.
        :return: Сообщение о загрузке.
        """
        if weight > self.load_capacity:
            return f"Перегруз! Максимальная грузоподъёмность {self.load_capacity} тонн."
        return f"Загружено {weight} тонн в {self.brand} {self.model}."

    def __repr__(self) -> str:
        """Возвращает строку для воссоздания объекта."""
        return (f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}, "
                f"year={self.year}, load_capacity={self.load_capacity})")


# Тестирование
if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2022, 5)
    truck = Truck("Volvo", "FH16", 2021, 18.0)

    print(car)  # Toyota Camry (2022 г.)
    print(truck)  # Volvo FH16 (2021 г.)

    print(car.start_engine())  # Toyota Camry (5 мест): двигатель запущен.
    print(truck.start_engine())  # Volvo FH16: двигатель запущен.

    print(truck.load_cargo(10))  # Загружено 10 тонн в Volvo FH16.
    print(truck.load_cargo(20))  # Перегруз! Максимальная грузоподъёмность 18.0 тонн.

    print(repr(car))  # Car(brand='Toyota', model='Camry', year=2022, passengers=5)
    print(repr(truck))  # Truck(brand='Volvo', model='FH16', year=2021, load_capacity=18.0)

