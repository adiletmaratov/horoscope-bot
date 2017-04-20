import logging

from horoscope_parser.hs_parser import (
    DailyCommonHoroscopeReceiver, DailyCommonHoroscopeParser
)
from horoscope_parser.hs_saver import DailyCommonHoroscopeDBSaver
from .constants import ANIMALS_DICT


logger = logging.getLogger(__name__)


class DailyCommonHoroscopeCollectorManager(object):
    def collect_horoscopes(self):
        for animal in ANIMALS_DICT:
            collector = DailyCommonHoroscopeCollector(animal)
            collector.collect()


class DailyCommonHoroscopeCollector(object):
    def __init__(self, animal):
        self._animal = animal

    def collect(self):
        logger.info("Start receiving horoscopes for {}...".format(self._animal))
        receiver = DailyCommonHoroscopeReceiver(self._animal)
        horoscope_xml = receiver.get_horoscope()
        logger.info("Done receiving horoscopes for {}...".format(self._animal))
        logger.info("Start parsing...")
        parser = DailyCommonHoroscopeParser(horoscope_xml)
        horoscope_data = parser.get_parsed_horoscope()
        logger.info("Finished parsing...")
        logger.info("Saving to database...")
        db_saver = DailyCommonHoroscopeDBSaver(horoscope_data)
        db_saver.save()
        logger.info("Finished saving to database...")
        logger.info("Finished horoscopes for {}...".format(self._animal))
