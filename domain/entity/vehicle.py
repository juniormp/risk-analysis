from domain.entity.asset import Asset


class Vehicle(Asset):
    year_manufactured = None

    def __init__(self, year_manufactured):
        self.year_manufactured = year_manufactured

    def __eq__(self, other):
        return isinstance(other, Vehicle) and \
               other.year_manufactured == self.year_manufactured
