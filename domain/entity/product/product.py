from abc import ABC

PRODUCT_SCORE_ECONOMIC = 'economic'
PRODUCT_SCORE_REGULAR = 'regular'
PRODUCT_SCORE_RESPONSIBLE = 'responsible'
PRODUCT_SCORE_INELIGIBLE = 'ineligible'
PRODUCT_SCORE_DEFAULT = 'default'
PRODUCT_SCORE = [PRODUCT_SCORE_ECONOMIC, PRODUCT_SCORE_ECONOMIC, PRODUCT_SCORE_RESPONSIBLE]


class Product(ABC):
    score = PRODUCT_SCORE

    def __init__(self, status):
        self.score = status

    def __eq__(self, other):
        return isinstance(other, Product) and \
               other.score == self.score
