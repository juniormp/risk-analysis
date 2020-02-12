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
    def get_rules_list(self):
        return [
            BetweenThirtyAndFortyYearsOld(),
            HasDependents(),
            HasHouse(),
            HasIncome(),
            HasIncomeAboveTwoHundred(),
            HasVehicle(),
            IsMarried(),
            IsOverSixtyYearsOld(),
            UnderThirtyYearsOld()
        ]
