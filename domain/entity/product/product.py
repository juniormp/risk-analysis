from abc import ABC

PRODUCT_SCORE_ECONOMIC = 'economic'
PRODUCT_SCORE_REGULAR = 'regular'
PRODUCT_SCORE_RESPONSIBLE = 'responsible'
PRODUCT_SCORE_DEFAULT = 'default'
PRODUCT_SCORE_INELIGIBLE = 'ineligible'
PRODUCT_SCORE = [PRODUCT_SCORE_ECONOMIC, PRODUCT_SCORE_ECONOMIC, PRODUCT_SCORE_RESPONSIBLE]


class Product(ABC):
    status: str
    score: int

    def __init__(self, status, score):
        self.status = status
        self.score = score

    def add_score_points(self, quantity: int):
        self.score = self.score + quantity

    def deduct_score_points(self, quantity: int):
        self.score = self.score - quantity

    def update_score_status(self, status: str):
        self.status = status

    def get_score(self):
        return self.score

    def __eq__(self, other):
        return isinstance(other, Product) and \
               other.score == self.score and \
               other.status == self.status
