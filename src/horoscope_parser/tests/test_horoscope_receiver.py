from unittest import mock

from datetime import date
from django.test import TestCase

from horoscope_parser.constants import ARIES, ANIMALS_DICT
from horoscope_parser.hs_parser import (
    DailyCommonHoroscopeReceiver,
    DailyCommonHoroscopeParser
)


class DailyCommonHoroscopeReceiverTest(TestCase):

    @mock.patch("horoscope_parser.hs_parser.requests.get")
    def test_request_to_right_url(self, mock_request):
        receiver = DailyCommonHoroscopeReceiver(ARIES)
        receiver.get_horoscope()
        mock_request.called_once_with(ANIMALS_DICT[ARIES]['daily_common_url'])


class DailyCommonHoroscopeParserTest(TestCase):
    def setUp(self):
        self.fake_horoscope = """
            <?xml version="1.0" encoding="windows-1251" ?>
            <rss version="2.0"><channel>
            <title>Ежедневный гороскоп от Hyrax.ru</title>
            <link>http://www.hyrax.ru/</link>
            <description>Астрологический портал посвященный гороскопам.</description>
            <pubDate></pubDate>
            <item>
            <title>ОВЕН (21 марта - 20 апреля) </title>
            <link>http://www.hyrax.ru/horo.shtml?cur&amp;1&amp;1&amp;0</link>
            <description>Сегодняшний день может оказаться очень</description>
            <pubDate>Thu, 20 Apr 2017 00:00:02 +0300</pubDate>
            </item>
            </channel></rss>
        """

    def test_get_parsed_horoscope(self):
        parser = DailyCommonHoroscopeParser(self.fake_horoscope)
        expected_horoscope_data = {
            'name': "ОВЕН (21 марта - 20 апреля) ",
            'description': "Сегодняшний день может оказаться очень",
            'date': date(2017, 4, 20)
        }
        actual_horoscope = parser.get_parsed_horoscope()
        self.assertEqual(expected_horoscope_data, actual_horoscope)
