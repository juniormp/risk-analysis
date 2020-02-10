from domain.entity.product.product import Product, PRODUCT_SCORE


class DisabilityProduct(Product):
    def __init__(self):
        self.score = PRODUCT_SCORE[0]

    def __eq__(self, other):
        return isinstance(other, DisabilityProduct) and \
               other.score == self.score
