from django.test import TestCase
from domain.entity.rule.person.has_income import HasIncome
from domain.entity.rule.person_rules import PersonRules


class TestPersonRules(TestCase):
    def setUp(self):
        self.has_income = HasIncome()
        self.person_rules_list = [
            self.has_income
        ]

    def test_return_the_list_of_persons_rules(self):
        person_rules = PersonRules(self.has_income)

        response = person_rules.get_rules_list()

        self.assertEqual(self.person_rules_list, response)
