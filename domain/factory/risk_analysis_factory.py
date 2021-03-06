from domain.entity.house import House
from domain.entity.person import Person
from domain.entity.product.disability_product import DisabilityProduct
from domain.entity.product.home_product import HomeProduct
from domain.entity.product.life_product import LifeProduct
from domain.entity.product.product import VEHICLE_PRODUCT, HOME_PRODUCT, LIFE_PRODUCT, DISABILITY_PRODUCT
from domain.entity.product.vehicle_product import VehicleProduct
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.risk_profile import RiskProfile
from domain.entity.rule.asset_rules import AssetRules
from domain.entity.rule.person_rules import PersonRules
from domain.entity.vehicle import Vehicle
from domain.factory.risk_analysis_rules_factory import RiskAnalysisRulesFactory


class RiskAnalysisFactory:
    def create_risk_analysis_from(self, user_information):
        house = user_information['house']
        vehicle = user_information['vehicle']

        if house is not None:
            house = self.__create_house(user_information['house']['ownership_status'])

        if vehicle is not None:
            vehicle = self.__create_vehicle(user_information['vehicle']['year'])

        person = self.__create_person(user_information, house, vehicle)

        vehicle_product = VehicleProduct()
        home_product = HomeProduct()
        life_product = LifeProduct()
        disability_product = DisabilityProduct()

        risk_profile = self.__create_risk_profile(vehicle_product, home_product, life_product, disability_product)
        rules_list = self.__create_rules_list()

        risk_analysis = self.__create_risk_analysis(person, risk_profile, rules_list)

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

    def __create_risk_profile(self, vehicle_product, home_product, life_product, disability_product):
        return RiskProfile(
            products={
                VEHICLE_PRODUCT: vehicle_product,
                HOME_PRODUCT: home_product,
                LIFE_PRODUCT: life_product,
                DISABILITY_PRODUCT: disability_product
            }
        )

    def __create_risk_analysis(self, person, risk_profile, rules_list):
        return RiskAnalysis(
            person=person,
            risk_profile=risk_profile,
            rules_list=rules_list
        )

    def __create_rules_list(self):
        return RiskAnalysisRulesFactory(PersonRules(), AssetRules()).build_rules_list()
