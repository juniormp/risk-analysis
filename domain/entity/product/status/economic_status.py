from domain.entity.product.status.product_status import ProductStatus, PRODUCT_STATUS_ECONOMIC


class EconomicStatus(ProductStatus):
    def __init__(self):
        self.name = PRODUCT_STATUS_ECONOMIC

    def apply_condition(self, score: int):
        return score <= 0
