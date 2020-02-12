from abc import ABC, abstractmethod


class AbstractUseCase(ABC):
    @abstractmethod
    def execute(self, user_information):
        pass
