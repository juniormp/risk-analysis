from django.test import TestCase
from domain.entity.risk_analysis import RiskAnalysis
from domain.entity.rule.person.between_thirty_and_forty_years_old import BetweenThirtyAndFortyYearsOld
from tests.person_builder import PersonBuilder
from tests.risk_profile_builder import RiskProfileBuilder


class TestUnderThirtyYearsOld(TestCase):
    def setUp(self):
        risk_profile_builder = RiskProfileBuilder()
        self.risk_profile = risk_profile_builder \
            .with_disability_product() \
            .with_home_product() \
            .with_life_product() \
            .with_vehicle_product() \
            .build()

        self.person_builder = PersonBuilder()
        self.rule = BetweenThirtyAndFortyYearsOld()

    def test_is_truly_when_person_is_between_thirty_and_forty_years_old(self):
        she = self.person_builder.with_age(30).build()
        risk_analysis_she = RiskAnalysis(person=she, risk_profile=self.risk_profile)
        he = self.person_builder.with_age(40).build()
        risk_analysis_he = RiskAnalysis(person=he, risk_profile=self.risk_profile)

        risk_analysis_she = self.rule.execute(risk_analysis=risk_analysis_she)
        risk_analysis_he = self.rule.execute(risk_analysis=risk_analysis_he)

        self.assertEqual(-1, risk_analysis_she.risk_profile.risk_score.product['life'].score)
        self.assertEqual(-1, risk_analysis_she.risk_profile.risk_score.product['disability'].score)
        self.assertEqual(-1, risk_analysis_she.risk_profile.risk_score.product['home'].score)
        self.assertEqual(-1, risk_analysis_she.risk_profile.risk_score.product['vehicle'].score)

        self.assertEqual(-1, risk_analysis_he.risk_profile.risk_score.product['life'].score)
        self.assertEqual(-1, risk_analysis_he.risk_profile.risk_score.product['disability'].score)
        self.assertEqual(-1, risk_analysis_he.risk_profile.risk_score.product['home'].score)
        self.assertEqual(-1, risk_analysis_he.risk_profile.risk_score.product['vehicle'].score)

    def test_is_falsely_when_person_is_not_between_thirty_and_forty_years_old(self):
        she = self.person_builder.with_age(29).build()
        risk_analysis_she = RiskAnalysis(person=she, risk_profile=self.risk_profile)
        he = self.person_builder.with_age(41).build()
        risk_analysis_he = RiskAnalysis(person=he, risk_profile=self.risk_profile)

        risk_analysis_she = self.rule.execute(risk_analysis=risk_analysis_she)
        risk_analysis_he = self.rule.execute(risk_analysis=risk_analysis_he)

        self.assertEqual(0, risk_analysis_she.risk_profile.risk_score.product['life'].score)
        self.assertEqual(0, risk_analysis_she.risk_profile.risk_score.product['disability'].score)
        self.assertEqual(0, risk_analysis_she.risk_profile.risk_score.product['home'].score)
        self.assertEqual(0, risk_analysis_she.risk_profile.risk_score.product['vehicle'].score)

        self.assertEqual(0, risk_analysis_he.risk_profile.risk_score.product['life'].score)
        self.assertEqual(0, risk_analysis_he.risk_profile.risk_score.product['disability'].score)
        self.assertEqual(0, risk_analysis_he.risk_profile.risk_score.product['home'].score)
        self.assertEqual(0, risk_analysis_he.risk_profile.risk_score.product['vehicle'].score)
