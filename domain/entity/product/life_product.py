from domain.entity.product.product import Product, PRODUCT_SCORE_DEFAULT


class LifeProduct(Product):
    def __init__(self):
        self.score = PRODUCT_SCORE_DEFAULT

    def __eq__(self, other):
        return isinstance(other, LifeProduct) and \
               other.score == self.score
