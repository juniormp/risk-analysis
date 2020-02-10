from django.test import TestCase
from domain.entity.person import Person
from domain.entity.rule.person.has_dependents import HasDependents


class TestHasDependents(TestCase):
    def test_is_truly_when_person_has_dependents(self):
        rule = HasDependents()
        person = Person(
            income=None,
            age=None,
            dependents=1,
            marital_status=None,
            risk_question=None,
            assets=None
        )

        response = rule.execute(person=person)

        self.assertTrue(response)

    def test_is_falsely_when_person_has_no_dependents(self):
        rule = HasDependents()
        person = Person(
            income=None,
            age=None,
            dependents=0,
            marital_status=None,
            risk_question=None,
            assets=None
        )

        response = rule.execute(person=person)

        self.assertFalse(response)
