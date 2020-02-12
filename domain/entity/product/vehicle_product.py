from domain.entity.product.product import Product, PRODUCT_SCORE_DEFAULT


class VehicleProduct(Product):
    def __init__(self):
        super().__init__(status=PRODUCT_SCORE_DEFAULT, risk_score=0)
