from django.test import TestCase
from domain.entity.house import House
from domain.entity.person import Person
from domain.entity.rule.person.has_asset import HasAsset


class TestHasAsset(TestCase):
    def test_is_truly_when_person_has_asset(self):
        rule = HasAsset()
        house = House(
            ownership_status="owned"
        )
        person = Person(
            income=None,
            age=None,
            dependents=None,
            marital_status=None,
            risk_question=None,
            assets=[house]
        )

        response = rule.execute(person=person)

        self.assertTrue(response)

    def test_is_falsely_when_person_has_no_asset(self):
        rule = HasAsset()
        person = Person(
            income=None,
            age=None,
            dependents=None,
            marital_status=None,
            risk_question=None,
            assets=[]
        )

        response = rule.execute(person=person)

        self.assertFalse(response)
