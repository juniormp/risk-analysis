from domain.entity.product.product import Product, HOME_PRODUCT, VEHICLE_PRODUCT, DISABILITY_PRODUCT, LIFE_PRODUCT


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

    def to_array(self):
        return {
            VEHICLE_PRODUCT: self.get_product_by(VEHICLE_PRODUCT).get_status(),
            DISABILITY_PRODUCT: self.get_product_by(DISABILITY_PRODUCT).get_status(),
            HOME_PRODUCT: self.get_product_by(HOME_PRODUCT).get_status(),
            LIFE_PRODUCT: self.get_product_by(LIFE_PRODUCT).get_status()
        }
