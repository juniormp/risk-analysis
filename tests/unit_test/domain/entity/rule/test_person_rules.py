from django.test import TestCase

from domain.entity.rule.person.between_thirty_and_forty_years_old import BetweenThirtyAndFortyYearsOld
from domain.entity.rule.person.has_asset import HasAsset
from domain.entity.rule.person.has_income import HasIncome
from domain.entity.rule.person.is_married import IsMarried
from domain.entity.rule.person.over_sixty_years_old import OverSixtyYearsOld
from domain.entity.rule.person.under_thirty_years_old import UnderThirtyYearsOld
from domain.entity.rule.person.has_dependents import HasDependents
from domain.entity.rule.person_rules import PersonRules


class TestPersonRules(TestCase):
    def setUp(self):
        self.has_income = HasIncome()
        self.has_asset = HasAsset()
        self.over_sixty_years_old = OverSixtyYearsOld()
        self.under_under_thirty_years_old = UnderThirtyYearsOld()
        self.between_thirty_and_forty_years_old = BetweenThirtyAndFortyYearsOld()
        self.has_dependents = HasDependents()
        self.is_married = IsMarried()
        self.person_rules_list = [
            self.has_income,
            self.has_asset,
            self.over_sixty_years_old,
            self.under_under_thirty_years_old,
            self.between_thirty_and_forty_years_old,
            self.has_dependents,
            self.is_married
        ]

    def test_return_the_list_of_persons_rules(self):
        person_rules = PersonRules(
            self.has_income,
            self.has_asset,
            self.over_sixty_years_old,
            self.under_under_thirty_years_old,
            self.between_thirty_and_forty_years_old,
            self.has_dependents,
            self.is_married
        )

        response = person_rules.get_rules_list()

        self.assertEqual(self.person_rules_list, response)
