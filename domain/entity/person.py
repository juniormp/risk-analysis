MARITAL_STATUS_MARRIED = 'married'
MARITAL_STATUS_SINGLE = 'single'
MARITAL_STATUS = [MARITAL_STATUS_SINGLE, MARITAL_STATUS_MARRIED]


class Person:
    age = None
    income = None
    dependents = None
    marital_status = None
    risk_question = None
    assets = []

    def __init__(self, age, income, dependents, marital_status, risk_question, assets):
        self.age = age
        self.income = income
        self.dependents = dependents
        self.marital_status = marital_status
        self.risk_question = risk_question
        self.assets = assets

    def __eq__(self, other):
        return isinstance(other, Person) and \
               other.age == self.age and \
               other.income == self.income and \
               other.dependents == self.dependents and \
               other.marital_status == self.marital_status and \
               other.risk_question == self.risk_question and \
               other.assets == self.assets
