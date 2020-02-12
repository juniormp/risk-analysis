from unittest import TestCase

from domain.entity.house import House, OWNERSHIP_STATUS_MORTGAGED
from domain.entity.person import MARITAL_STATUS_SINGLE
from domain.entity.product.product import PRODUCT_SCORE_INELIGIBLE
from domain.entity.product.status.product_status_builder import ProductStatusBuilder
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.rule.asset.is_house_mortgaged import IsHouseMortgaged
from domain.entity.rule.asset.is_vehicle_produced_last_five_years import VehicleProducedLastFiveYears
from domain.entity.rule.asset_rules import AssetRules
from domain.entity.rule.person.between_thirty_and_forty_years_old import BetweenThirtyAndFortyYearsOld
from domain.entity.rule.person.has_dependents import HasDependents
from domain.entity.rule.person.has_house import HasHouse
from domain.entity.rule.person.has_income import HasIncome
from domain.entity.rule.person.has_income_above_two_hundred import HasIncomeAboveTwoHundred
from domain.entity.rule.person.has_vehicle import HasVehicle
from domain.entity.rule.person.is_married import IsMarried
from domain.entity.rule.person.is_over_sixty_years_old import IsOverSixtyYearsOld
from domain.entity.rule.person.under_thirty_years_old import UnderThirtyYearsOld
from domain.entity.rule.person_rules import PersonRules
from domain.entity.vehicle import Vehicle
from domain.factory.risk_analysis_rules_factory import RiskAnalysisRulesFactory
from domain.service.risk_analysis_service import RiskAnalysisService
from tests.person_builder import PersonBuilder
from tests.risk_profile_builder import RiskProfileBuilder


class TestRiskAnalysis(TestCase):
    def setUp(self):
        risk_profile_builder = RiskProfileBuilder()
        self.risk_profile = risk_profile_builder \
            .with_disability_product() \
            .with_home_product() \
            .with_life_product() \
            .with_vehicle_product() \
            .build()
        self.house = House(ownership_status=OWNERSHIP_STATUS_MORTGAGED)
        self.vehicle = Vehicle(year_manufactured=2019)

        self.person = PersonBuilder() \
            .with_age(29).with_marital_status(MARITAL_STATUS_SINGLE).with_dependents(1).with_income(230).build()

        self.risk_analysis = RiskAnalysis(person=self.person, risk_profile=self.risk_profile)

    def test_foo(self):
        asset_rules = AssetRules()
        person_rules = PersonRules()
        risk_analysis_rules_factory = RiskAnalysisRulesFactory(person_rules, asset_rules)
        product_status_builder = ProductStatusBuilder()
        risk_analysis_service = RiskAnalysisService(risk_analysis_rules_factory, product_status_builder)

        rules_list = risk_analysis_service.build_rules_list()
        risk_analysis_service.apply_rules_on(self.risk_analysis, rules_list)
        risk_analysis_service.foo(risk_score=self.risk_analysis.risk_profile.get_risk_score())

        self.assertEqual(PRODUCT_SCORE_INELIGIBLE,
                         self.risk_analysis.get_products_in_risk_analysis()['home'].get_status())
        self.assertEqual(PRODUCT_SCORE_INELIGIBLE,
                         self.risk_analysis.get_products_in_risk_analysis()['vehicle'].get_status())
