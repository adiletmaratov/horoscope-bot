from django.db import models
from .constants import *


ANIMALS_CHOICES = (
    (1, ARIES),
    (2, TAURUS),
    (3, GEMINI),
    (4, CANCER),
    (5, LEO),
    (6, VIRGO),
    (7, LIBRA),
    (8, SCORPIO),
    (9, SAGITTARIUS),
    (10, CAPRICORN),
    (11, AQUARIOU),
    (12, PISCES),
)


class DailyCommonHoroscope(models.Model):
    name = models.CharField(max_length=254, choices=ANIMALS_CHOICES,
                            db_index=True)
    description = models.TextField()
    date = models.DateField(db_index=True)

    class Meta:
        verbose_name = "Ежедневный гороскоп"
        verbose_name_plural = "Ежедневные гороскопы"
