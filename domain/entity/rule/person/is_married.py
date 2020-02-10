from domain.entity.person import Person, MARITAL_STATUS_MARRIED


class IsMarried:
    def execute(self, person=Person):
        if person.marital_status == MARITAL_STATUS_MARRIED:
            return True

        return False
