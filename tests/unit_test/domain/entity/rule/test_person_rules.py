from django.test import TestCase
from domain.entity.rule.person.between_thirty_and_forty_years_old import BetweenThirtyAndFortyYearsOld
from domain.entity.rule.person.has_house import HasHouse
from domain.entity.rule.person.has_income import HasIncome
from domain.entity.rule.person.has_income_above_two_hundred import HasIncomeAboveTwoHundred
from domain.entity.rule.person.has_vehicle import HasVehicle
from domain.entity.rule.person.is_married import IsMarried
from domain.entity.rule.person.is_over_sixty_years_old import IsOverSixtyYearsOld
from domain.entity.rule.person.under_thirty_years_old import UnderThirtyYearsOld
from domain.entity.rule.person.has_dependents import HasDependents
from domain.entity.rule.person_rules import PersonRules


class TestPersonRules(TestCase):
    def setUp(self):
        self.between_thirty_and_forty_years_old = BetweenThirtyAndFortyYearsOld()
        self.has_dependents = HasDependents()
        self.has_house = HasHouse()
        self.has_income = HasIncome()
        self.has_income_above_two_hundred = HasIncomeAboveTwoHundred()
        self.has_vehicle = HasVehicle()
        self.is_married = IsMarried()
        self.over_sixty_years_old = IsOverSixtyYearsOld()
        self.under_thirty_years_old = UnderThirtyYearsOld()

        self.person_rules_list = [
            self.between_thirty_and_forty_years_old,
            self.has_dependents,
            self.has_house,
            self.has_income,
            self.has_income_above_two_hundred,
            self.has_vehicle,
            self.is_married,
            self.over_sixty_years_old,
            self.under_thirty_years_old
        ]

    def test_return_the_list_of_persons_rules(self):
        person_rules = PersonRules(
            self.between_thirty_and_forty_years_old,
            self.has_dependents,
            self.has_house,
            self.has_income,
            self.has_income_above_two_hundred,
            self.has_vehicle,
            self.is_married,
            self.over_sixty_years_old,
            self.under_thirty_years_old
        )

        response = person_rules.get_rules_list()

        self.assertEqual(self.person_rules_list, response)
