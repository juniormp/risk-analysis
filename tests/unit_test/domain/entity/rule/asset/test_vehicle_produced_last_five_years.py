from django.test import TestCase
from domain.entity.rule.asset.is_vehicle_produced_last_five_years import VehicleProducedLastFiveYears
from domain.entity.vehicle import Vehicle
from freezegun import freeze_time
import datetime


class TestVehicleProducedLastFiveYears(TestCase):
    @freeze_time("2020-01-01")
    def test_is_truly_when_vehicle_was_produced_last_five_years(self):
        rule = VehicleProducedLastFiveYears()
        vehicle = Vehicle(
            year_manufactured=datetime.datetime(2015, 1, 1)
        )

        response = rule.execute(vehicle=vehicle)

        self.assertTrue(response)

    @freeze_time("2020-01-01")
    def test_is_falsely_when_vehicle_was_not_produced_last_five_years(self):
        rule = VehicleProducedLastFiveYears()
        vehicle = Vehicle(
            year_manufactured=datetime.datetime(2013, 12, 31)
        )

        response = rule.execute(vehicle=vehicle)

        self.assertFalse(response)
