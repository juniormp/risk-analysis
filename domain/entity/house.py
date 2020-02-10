from domain.entity.asset import Asset

OWNERSHIP_STATUS_MORTGAGED = 'mortgaged'
OWNERSHIP_STATUS_OWNED = 'owned'


class House(Asset):
    ownership_status = None

    def __init__(self, ownership_status):
        self.ownership_status = ownership_status

    def __eq__(self, other):
        return isinstance(other, House) and \
               other.ownership_status == self.ownership_status
