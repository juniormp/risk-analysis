from abc import abstractmethod, ABC

PRODUCT_STATUS_ECONOMIC = 'economic'
PRODUCT_STATUS_REGULAR = 'regular'
PRODUCT_STATUS_RESPONSIBLE = 'responsible'


class ProductStatus(ABC):
    name: str

    @abstractmethod
    def apply_condition(self, score: int):
        pass
