# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyCommonHoroscope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[(1, 'aries'), (2, 'taurus'), (3, 'gemini'), (4, 'cancer'), (5, 'leo'), (6, 'virgo'), (7, 'libra'), (8, 'scorpio'), (9, 'sagittarius'), (10, 'capricorn'), (11, 'aquarius'), (12, 'pisces')], db_index=True, max_length=254)),
                ('description', models.TextField()),
                ('date', models.DateField(db_index=True)),
            ],
            options={
                'verbose_name': 'Ежедневный гороскоп',
                'verbose_name_plural': 'Ежедневные гороскопы',
            },
        ),
    ]
