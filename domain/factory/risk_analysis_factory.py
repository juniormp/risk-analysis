from domain.entity.house import House
from domain.entity.person import Person
from domain.entity.product.disability_product import DisabilityProduct
from domain.entity.product.home_product import HomeProduct
from domain.entity.product.life_product import LifeProduct
from domain.entity.product.vehicle_product import VehicleProduct
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile
from domain.entity.risk_score import RiskScore
from domain.entity.vehicle import Vehicle
import array as array


class RiskAnalysisFactory:
    def createRiskAnalysis(self, user_information=array):

        house = House(
            user_information['ownership_status']
        )

        vehicle = Vehicle(
            user_information['year_manufactured']
        )

        person = Person(
            age=user_information['age'],
            income=user_information['income'],
            dependents=user_information['dependents'],
            marital_status=user_information['marital_status'],
            risk_question=user_information['risk_question'],
            assets=[house, vehicle]
        )

        vehicle_product = VehicleProduct()
        home_product = HomeProduct()
        life_product = LifeProduct()
        disability_product = DisabilityProduct()

        risk_score = RiskScore(
            product=[vehicle_product, home_product, life_product, disability_product]
        )

        risk_profile = RiskProfile(
            risk_score=risk_score
        )

        risk_analysis = RiskAnalysis(
            person=person,
            risk_profile=risk_profile
        )

        return risk_analysis
