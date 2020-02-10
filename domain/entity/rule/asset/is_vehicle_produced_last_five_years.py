from domain.entity.vehicle import Vehicle
import pendulum


class VehicleProducedLastFiveYears:
    def execute(self, vehicle=Vehicle):
        time_right_now = pendulum.now()
        five_years_ago = time_right_now.subtract(years=5)
        if vehicle.year_manufactured.year > five_years_ago.year:
            return True

        return False
