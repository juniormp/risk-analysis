class RiskProfile:
    def __init__(self, products: {}):
        self._products = products

    def get_products(self):
        return self._products

    def __eq__(self, other):
        return isinstance(other, RiskProfile) and \
               other._products == self._products
