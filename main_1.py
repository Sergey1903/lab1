# TODO Написать 3 класса с документацией и аннотацией типов
from abc import ABC, abstractmethod

class AbstractObject1(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def print_name(self) -> None:
        pass

    @abstractmethod
    def change_name(self, new_name: str) -> str:
        pass

class AbstractObject2(ABC):
    def __init__(self, color: str, size: int):
        self.color = color
        self.size = size

    @abstractmethod
    def get_color(self) -> str:
        pass

    @abstractmethod
    def increase_size(self) -> int:
        pass

class AbstractObject3(ABC):
    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit

    @abstractmethod
    def convert_unit(self, target_unit: str) -> float:
        pass

    @abstractmethod
    def add_value(self, other_value: float) -> float:
        pass

