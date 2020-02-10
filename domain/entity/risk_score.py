from domain.entity.product.product import Product


class RiskScore:
    product = Product

    def __init__(self, product):
        self.product = product

    def __eq__(self, other):
        return isinstance(other, RiskScore) and \
               other.product == self.product
