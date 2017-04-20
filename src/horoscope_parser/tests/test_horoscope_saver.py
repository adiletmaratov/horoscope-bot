from datetime import date
from django.test import TestCase

from horoscope_parser.handlers import DailyCommonHoroscopeCollectorManager
from horoscope_parser.hs_saver import DailyCommonHoroscopeDBSaver
from horoscope_parser.models import DailyCommonHoroscope


class DailyCommonHoroscopeDBSaverTest(TestCase):

    def test_db_save(self):
        fake_horoscope_data = {
            'name': 'something',
            'description': 'some prediction here',
            'date': date.today()
        }
        saver = DailyCommonHoroscopeDBSaver(fake_horoscope_data)
        saver.save()
        self.assertEqual(1, DailyCommonHoroscope.objects.count())
        manager = DailyCommonHoroscopeCollectorManager()
        manager.collect_horoscopes()
