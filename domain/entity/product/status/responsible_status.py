from domain.entity.product.status.product_status import ProductStatus, PRODUCT_STATUS_RESPONSIBLE


class ResponsibleStatus(ProductStatus):
    def __init__(self):
        self.name = PRODUCT_STATUS_RESPONSIBLE

    def set_condition(self, score: int):
        return [score >= 3]
