from domain.entity.product.product import Product, PRODUCT_SCORE_ECONOMIC


class VehicleProduct(Product):
    def __init__(self):
        super().__init__(status=PRODUCT_SCORE_ECONOMIC, risk_score=0)
