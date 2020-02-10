from domain.entity.house import House, OWNERSHIP_STATUS_MORTGAGED


class IsHouseMortgaged:
    def execute(self, house=House):
        if house.ownership_status == OWNERSHIP_STATUS_MORTGAGED:
            return True

        return False
