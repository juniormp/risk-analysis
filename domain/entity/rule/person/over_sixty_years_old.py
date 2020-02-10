from domain.entity.person import Person


class OverSixtyYearsOld:
    def execute(self, person=Person):
        if person.age > 60:
            return True

        return False
