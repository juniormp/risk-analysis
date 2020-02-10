from domain.entity.product.product import Product, PRODUCT_SCORE


class HomeProduct(Product):
    def __init__(self):
        self.score = PRODUCT_SCORE[0]

    def __eq__(self, other):
        return isinstance(other, HomeProduct) and \
               other.score == self.score
