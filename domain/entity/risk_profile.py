from domain.entity.product.product import Product


class RiskProfile:
    products: {}

    def __init__(self, products: {}):
        self.products = products

    def set_product(self, name: str, product: Product):
        self.products[name] = product

    def get_products(self):
        return self.products

    def get_product_by(self, name: str):
        return self.products[name]

    def __eq__(self, other):
        return isinstance(other, RiskProfile) and \
               other.products == self.products
