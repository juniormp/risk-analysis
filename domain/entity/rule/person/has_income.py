from domain.entity.person import Person


class HasIncome:
    def execute(self, person=Person):
        if person.income > 0:
            return True

        return False
