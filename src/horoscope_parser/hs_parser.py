from datetime import datetime
import requests

from bs4 import BeautifulSoup

from .constants import *


class DailyCommonHoroscopeReceiver(object):
    def __init__(self, animal):
        self._animal = animal

    def get_horoscope(self):
        animal_dict = ANIMALS_DICT[self._animal]
        animal_horoscope_url = animal_dict['daily_common_url']
        response = requests.get(animal_horoscope_url)
        return response.content


class DailyCommonHoroscopeParser(object):
    def __init__(self, horoscope_xml):
        self._horoscope_xml = horoscope_xml

    def get_parsed_horoscope(self):
        soup = BeautifulSoup(self._horoscope_xml, 'html.parser')
        horoscope_data = {
            'name': soup.item.title.text,
            'description': soup.item.description.text,
            'date': datetime.strptime(soup.item.pubdate.text,
                                      "%a, %d %b %Y %X %z").date()
        }
        return horoscope_data
