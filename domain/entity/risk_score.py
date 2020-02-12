class RiskScore:
    products = {}

    def __init__(self, products: {}):
        self.products = products

    def get_product_by(self, name: str):
        return self.products.get(name)

    def __eq__(self, other):
        return isinstance(other, RiskScore) and \
               other.products == self.products
