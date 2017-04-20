from .models import DailyCommonHoroscope


class DailyCommonHoroscopeDBSaver(object):
    def __init__(self, horoscope_data):
        self._horoscope_data = horoscope_data

    def save(self):
        horoscope, created = DailyCommonHoroscope.objects.get_or_create(
            **self._horoscope_data
        )
        return horoscope
