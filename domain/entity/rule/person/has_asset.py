from domain.entity.person import Person


class HasAsset:
    def execute(self, person=Person):
        for asset in person.assets:
            return True

        return False
