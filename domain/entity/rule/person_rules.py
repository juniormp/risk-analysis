from domain.entity.rule.person.between_thirty_and_forty_years_old import BetweenThirtyAndFortyYearsOld
from domain.entity.rule.person.has_dependents import HasDependents
from domain.entity.rule.person.has_house import HasHouse
from domain.entity.rule.person.has_income import HasIncome
from domain.entity.rule.person.has_income_above_two_hundred import HasIncomeAboveTwoHundred
from domain.entity.rule.person.has_vehicle import HasVehicle
from domain.entity.rule.person.is_married import IsMarried
from domain.entity.rule.person.is_over_sixty_years_old import IsOverSixtyYearsOld
from domain.entity.rule.person.under_thirty_years_old import UnderThirtyYearsOld


class PersonRules:
    def __init__(self,
                 between_thirty_and_forty_years_old: BetweenThirtyAndFortyYearsOld,
                 has_dependents: HasDependents,
                 has_house: HasHouse,
                 has_income: HasIncome,
                 has_income_above_two_hundred: HasIncomeAboveTwoHundred,
                 has_vehicle: HasVehicle,
                 is_married: IsMarried,
                 over_sixty_years_old: IsOverSixtyYearsOld,
                 under_thirty_years_old: UnderThirtyYearsOld):
        self.between_thirty_and_forty_years_old = between_thirty_and_forty_years_old
        self.has_dependents = has_dependents
        self.has_house = has_house
        self.has_income = has_income
        self.has_income_above_two_hundred = has_income_above_two_hundred
        self.has_vehicle = has_vehicle
        self.is_married = is_married
        self.over_sixty_years_old = over_sixty_years_old
        self.under_thirty_years_old = under_thirty_years_old

    def get_rules_list(self):
        return [
            self.between_thirty_and_forty_years_old,
            self.has_dependents,
            self.has_house,
            self.has_income,
            self.has_income_above_two_hundred,
            self.has_vehicle,
            self.is_married,
            self.over_sixty_years_old,
            self.under_thirty_years_old
        ]
