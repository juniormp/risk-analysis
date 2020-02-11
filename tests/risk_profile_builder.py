from domain.entity.product.disability_product import DisabilityProduct
from domain.entity.product.home_product import HomeProduct
from domain.entity.product.life_product import LifeProduct
from domain.entity.product.vehicle_product import VehicleProduct
from domain.entity.risk_profile import RiskProfile
from domain.entity.risk_score import RiskScore


class RiskProfileBuilder:
    risk_profile: RiskProfile
    risk_score: RiskScore

    def __init__(self):
        self.risk_score = RiskScore

    def with_vehicle_product(self):
        self.risk_score.product['vehicle'] = VehicleProduct()
        self.risk_profile = RiskProfile(
            risk_score=self.risk_score
        )

        return self

    def with_home_product(self):
        self.risk_score.product['home'] = HomeProduct()
        self.risk_profile = RiskProfile(
            risk_score=self.risk_score
        )

        return self

    def with_life_product(self):
        self.risk_score.product['life'] = LifeProduct()
        self.risk_profile = RiskProfile(
            risk_score=self.risk_score
        )

        return self

    def with_disability_product(self):
        self.risk_score.product['disability'] = DisabilityProduct()
        self.risk_profile = RiskProfile(
            risk_score=self.risk_score
        )

        return self

    def build(self):
        return self.risk_profile
