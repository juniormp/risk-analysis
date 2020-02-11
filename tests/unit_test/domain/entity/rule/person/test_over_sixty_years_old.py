from django.test import TestCase
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.rule.person.over_sixty_years_old import OverSixtyYearsOld
from tests.person_builder import PersonBuilder
from tests.risk_profile_builder import RiskProfileBuilder


class TestOverSixtyYearsOld(TestCase):
    def setUp(self):
        risk_profile_builder = RiskProfileBuilder()
        self.risk_profile = risk_profile_builder \
            .with_disability_product() \
            .with_home_product() \
            .with_life_product() \
            .with_vehicle_product() \
            .build()

        self.rule = OverSixtyYearsOld()

    def test_is_truly_when_person_is_over_sixty_years_old(self):
        person_builder = PersonBuilder()
        person = person_builder.with_age(61).build()
        risk_analysis = RiskAnalysis(person=person, risk_profile=self.risk_profile)

        response = self.rule.execute(risk_analysis=risk_analysis)

        self.assertTrue(response)

    def test_is_falsely_when_person_under_sixty_years_old(self):
        person_builder = PersonBuilder()
        person = person_builder.with_age(60).build()
        risk_analysis = RiskAnalysis(person=person, risk_profile=self.risk_profile)

        response = self.rule.execute(risk_analysis=risk_analysis)

        self.assertFalse(response)
