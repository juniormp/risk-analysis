from domain.entity.person import Person


class BetweenThirtyAndFortyYearsOld:
    def execute(self, person=Person):
        conditions = [person.age >= 30, person.age <= 40]
        if all(conditions):
            return True

        return False
