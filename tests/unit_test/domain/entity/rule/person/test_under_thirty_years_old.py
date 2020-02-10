from django.test import TestCase
from domain.entity.person import Person
from domain.entity.rule.person.under_thirty_years_old import UnderThirtyYearsOld


class TestUnderThirtyYearsOld(TestCase):
    def test_is_truly_when_person_is_under_thirty_years_old(self):
        rule = UnderThirtyYearsOld()
        person = Person(
            income=None,
            age=29,
            dependents=None,
            marital_status=None,
            risk_question=None,
            assets=None
        )

        response = rule.execute(person=person)

        self.assertTrue(response)

    def test_is_falsely_when_person_is_not_under_thirty_years_old(self):
        rule = UnderThirtyYearsOld()
        person = Person(
            income=None,
            age=30,
            dependents=None,
            marital_status=None,
            risk_question=None,
            assets=None
        )

        response = rule.execute(person=person)

        self.assertFalse(response)
