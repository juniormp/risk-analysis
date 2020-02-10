from django.test import TestCase

from domain.entity.house import House
from domain.entity.person import Person
from domain.entity.rule.person.has_income import HasIncome
from domain.entity.vehicle import Vehicle


class TestHasIncome(TestCase):
    def test_is_truly_when_person_has_income(self):
        rule = HasIncome()
        person = Person(
            income=100.00,
            age=None,
            dependents=None,
            marital_status=None,
            risk_question=None,
            assets=None
        )

        response = rule.execute(person=person)

        self.assertTrue(response)

    def test_is_falsely_when_person_has_no_income(self):
        rule = HasIncome()
        person = Person(
            income=0,
            age=None,
            dependents=None,
            marital_status=None,
            risk_question=None,
            assets=None
        )

        response = rule.execute(person=person)

        self.assertFalse(response)
