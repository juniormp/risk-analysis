from domain.entity.product.product import Product, PRODUCT_SCORE_DEFAULT


class LifeProduct(Product):
    def __init__(self):
        self.status = PRODUCT_SCORE_DEFAULT
        self.score = 0
