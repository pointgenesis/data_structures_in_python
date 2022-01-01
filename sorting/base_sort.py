from abc import ABC, abstractmethod


class BaseSort(ABC):

    @staticmethod
    @abstractmethod
    def sort(numbers):
        pass
