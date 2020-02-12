from abc import ABC

PRODUCT_SCORE_ECONOMIC = 'economic'
PRODUCT_SCORE_REGULAR = 'regular'
PRODUCT_SCORE_RESPONSIBLE = 'responsible'
PRODUCT_SCORE_DEFAULT = 'default'
PRODUCT_SCORE_INELIGIBLE = 'ineligible'

VEHICLE_PRODUCT = 'vehicle'
HOME_PRODUCT = 'home'
LIFE_PRODUCT = 'life'
DISABILITY_PRODUCT = 'disability'


class Product(ABC):
    status: str
    risk_score: int

    def __init__(self, status, risk_score):
        self.status = status
        self.risk_score = risk_score

    def add_score_points(self, quantity: int):
        self.risk_score = self.risk_score + quantity

    def deduct_score_points(self, quantity: int):
        self.risk_score = self.risk_score - quantity

    def update_status(self, status: str):
        self.status = status

    def get_score(self):
        return self.risk_score

    def get_status(self):
        return self.status

    def __eq__(self, other):
        return isinstance(other, Product) and \
               other.risk_score == self.risk_score and \
               other.status == self.status
