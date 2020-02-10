from django.test import TestCase
from domain.entity.person import Person
from domain.entity.rule.person.over_sixty_years_old import OverSixtyYearsOld


class TestOverSixtyYearsOld(TestCase):
    def test_is_truly_when_person_is_over_sixty_years_old(self):
        rule = OverSixtyYearsOld()
        person = Person(
            income=None,
            age=61,
            dependents=None,
            marital_status=None,
            risk_question=None,
            assets=None
        )

        response = rule.execute(person=person)

        self.assertTrue(response)

    def test_is_falsey_when_person_is_not_over_sixty_years_old(self):
        rule = OverSixtyYearsOld()
        person = Person(
            income=None,
            age=60,
            dependents=None,
            marital_status=None,
            risk_question=None,
            assets=None
        )

        response = rule.execute(person=person)

        self.assertFalse(response)
