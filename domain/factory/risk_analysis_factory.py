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


class RiskAnalysisFactory:
    def create_risk_analysis_from(self, user_information):
        house = self.__create_house(user_information['ownership_status'])
        vehicle = self.__create_vehicle(user_information['year_manufactured'])
        person = self.__create_person(user_information, house, vehicle)

        vehicle_product = VehicleProduct()
        home_product = HomeProduct()
        life_product = LifeProduct()
        disability_product = DisabilityProduct()

        risk_score = self.__create_risk_score(vehicle_product, home_product, life_product, disability_product)
        risk_profile = self.__create_risk_profile(risk_score)
        risk_analysis = self.__create_risk_analysis(person, risk_profile)

        return risk_analysis

    def __create_house(self, ownership_status):
        return House(
            ownership_status=ownership_status
        )

    def __create_vehicle(self, year_manufactured):
        return Vehicle(
            year_manufactured=year_manufactured
        )

    def __create_person(self, user_information, house, vehicle):
        return Person(
            age=user_information['age'],
            income=user_information['income'],
            dependents=user_information['dependents'],
            marital_status=user_information['marital_status'],
            risk_question=user_information['risk_question'],
            assets=[house, vehicle]
        )

    def __create_risk_score(self, vehicle_product, home_product, life_product, disability_product):
        return RiskScore(
            products=[vehicle_product, home_product, life_product, disability_product]
        )

    def __create_risk_profile(self, risk_score):
        return RiskProfile(
            risk_score=risk_score
        )

    def __create_risk_analysis(self, person, risk_profile):
        return RiskAnalysis(
            person=person,
            risk_profile=risk_profile
        )
