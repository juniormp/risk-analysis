from domain.entity.product.disability_product import DisabilityProduct
from domain.entity.product.home_product import HomeProduct
from domain.entity.product.life_product import LifeProduct
from domain.entity.product.product import VEHICLE_PRODUCT, HOME_PRODUCT, LIFE_PRODUCT, DISABILITY_PRODUCT
from domain.entity.product.vehicle_product import VehicleProduct
from domain.entity.risk_profile import RiskProfile


class RiskProfileBuilder:
    def __init__(self):
        self.__risk_profile = RiskProfile

    def with_vehicle_product(self):
        self.__risk_profile.set_product_into_list(name=VEHICLE_PRODUCT, product=VehicleProduct())

        return self

    def with_home_product(self):
        self.__risk_profile.set_product_into_list(name=HOME_PRODUCT, product=HomeProduct())

        return self

    def with_life_product(self):
        self.__risk_profile.set_product_into_list(name=LIFE_PRODUCT, product=LifeProduct())

        return self

    def with_disability_product(self):
        self.__risk_profile.set_product_into_list(name=DISABILITY_PRODUCT, product=DisabilityProduct())

        return self

    def build(self):
        return self.__risk_profile
