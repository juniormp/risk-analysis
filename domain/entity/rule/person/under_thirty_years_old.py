from domain.entity.person import Person


class UnderThirtyYearsOld:
    def execute(self, person=Person):
        if person.age < 30:
            return True

        return False
