from domain.entity.product.product import Product, PRODUCT_SCORE_DEFAULT


class LifeProduct(Product):
    def __init__(self):
        super().__init__(status=PRODUCT_SCORE_DEFAULT, score=0)
