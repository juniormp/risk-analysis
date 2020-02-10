from django.test import TestCase
from domain.entity.person import Person
from domain.entity.rule.person.between_thirty_and_forty_years_old import BetweenThirtyAndFortyYearsOld


class TestUnderThirtyYearsOld(TestCase):
    def test_is_truly_when_person_is_between_thirty_and_forty_years_old(self):
        rule = BetweenThirtyAndFortyYearsOld()
        she = Person(
            income=None,
            age=30,
            dependents=None,
            marital_status=None,
            risk_question=None,
            assets=None
        )
        he = Person(
            income=None,
            age=40,
            dependents=None,
            marital_status=None,
            risk_question=None,
            assets=None
        )

        response_she = rule.execute(person=she)
        response_he = rule.execute(person=he)

        self.assertTrue(response_she)
        self.assertTrue(response_he)

    def test_is_falsely_when_person_is_not_between_thirty_and_forty_years_old(self):
        rule = BetweenThirtyAndFortyYearsOld()
        she = Person(
            income=None,
            age=29,
            dependents=None,
            marital_status=None,
            risk_question=None,
            assets=None
        )
        he = Person(
            income=None,
            age=41,
            dependents=None,
            marital_status=None,
            risk_question=None,
            assets=None
        )

        response_she = rule.execute(person=she)
        response_he = rule.execute(person=he)

        self.assertFalse(response_she)
        self.assertFalse(response_he)
