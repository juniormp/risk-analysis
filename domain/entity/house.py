from domain.entity.asset import Asset


class House(Asset):
    ownership_status = None

    def __init__(self, ownership_status):
        self.ownership_status = ownership_status

    def __eq__(self, other):
        return isinstance(other, House) and \
               other.ownership_status == self.ownership_status
