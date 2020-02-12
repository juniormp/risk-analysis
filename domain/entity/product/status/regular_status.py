from domain.entity.product.status.product_status import ProductStatus, PRODUCT_STATUS_REGULAR


class RegularStatus(ProductStatus):
    def __init__(self):
        self.name = PRODUCT_STATUS_REGULAR

    def apply_condition(self, score: int):
        return score == 1 and score == 2
