from abc import ABC

PRODUCT_SCORE = ['economic', 'regular', 'responsible']


class Product(ABC):
    score = PRODUCT_SCORE

    def __init__(self, status):
        self.score = status

    def __eq__(self, other):
        return isinstance(other, Product) and \
               other.score == self.score
