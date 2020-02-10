from django.test import TestCase
from domain.entity.person import Person, MARITAL_STATUS_SINGLE, MARITAL_STATUS_MARRIED
from domain.entity.rule.person.is_married import IsMarried


class TestIsMarried(TestCase):
    def test_is_truly_when_person_is_married(self):
        rule = IsMarried()
        person = Person(
            income=None,
            age=None,
            dependents=None,
            marital_status=MARITAL_STATUS_MARRIED,
            risk_question=None,
            assets=None
        )

        response = rule.execute(person=person)

        self.assertTrue(response)

    def test_is_falsely_when_person_has_no_income(self):
        rule = IsMarried()
        person = Person(
            income=None,
            age=None,
            dependents=None,
            marital_status=MARITAL_STATUS_SINGLE,
            risk_question=None,
            assets=None
        )

        response = rule.execute(person=person)

        self.assertFalse(response)
