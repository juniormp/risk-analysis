import array

from domain.entity.asset import Asset
from domain.entity.person import Person


class PersonBuilder:
    person: Person

    def __init__(self):
        self.person = Person

    def with_age(self, age: int):
        self.person.age = age

        return self

    def with_dependents(self, dependents: int):
        self.person.dependents = dependents

        return self

    def with_income(self, income: int):
        self.person.income = income

        return self

    def with_marital_status(self, marital_status: str):
        self.person.marital_status = marital_status

        return self

    def with_risk_question(self, risk_question: array):
        self.person.risk_question = risk_question

        return self

    def with_house_asset(self, asset: Asset):
        self.person.assets.append(asset)

        return self

    def build(self):
        return self.person
