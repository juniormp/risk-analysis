import pendulum


class DateTimeHelper:
    @staticmethod
    def date_time_right_now():
        return pendulum.now()

    @staticmethod
    def subtract_years(years: int):
        date = DateTimeHelper.date_time_right_now()
        return date.subtract(years=years)

    @staticmethod
    def str_to_date_time(date: str):
        return pendulum.from_format(date, 'YYYY')

