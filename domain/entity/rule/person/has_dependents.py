from domain.entity.person import Person


class HasDependents:
    def execute(self, person=Person):
        if person.dependents > 0:
            return True

        return False
