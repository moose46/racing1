"""
    Reads drivers.csv file and imports drivers into the drivers table.
    If there are duplicates, it will stop, and throw up
    must have django-extensions installed and in entered into the INSTALLED_APPS settings file.
    
        INSTALLED_APPS = [
            "nascar.apps.NascarConfig",
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            "django_extensions",
        ]

    to run:
        python manage.py runscript load_results_from_csv
"""
import csv
import logging
import os
import sys
from collections import namedtuple
from pathlib import Path

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from nascar.models import Driver, Race, Results, Track

# https://k0nze.dev/posts/python-relative-imports-vscode/
file_path = Path.cwd() / "scripts" / "results" / "2022"
logging.basicConfig(
    filename="log_load_results.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)


def run():
    logging.info(file_path)
    user = User.objects.get(pk=1)
    for race_results in file_path.glob("*.csv"):
        # results = f.stem.split("_")[1]
        # logging.info(race_results)
        # Get the race details from the first header in the race results file
        # TRACK, DATE
        # Mid Ohio, 07/10/1946
        with open(race_results) as f:
            reader = csv.reader(f, delimiter="\t")
            RaceInfo = namedtuple("RaceInfo", next(reader), rename=True)
            race_info = None
            # RaceResults = namedtuple("RaceResults", next(reader), rename=True)
            for row in reader:
                race_info = RaceInfo(*row)
                logging.info(f"RaceInfo={race_info}")
                race = Race()
                race.race_date = race_info.DATE
                race.track = track_info
                race.save()
                break
            # Now get the race results data
            RaceResults = namedtuple("RaceResults", next(reader), rename=True)
            for row in reader:
                race_results = RaceResults(*row)

                logging.info(f"{race_results}")
                # print(race_results)

                r = Results()
                r.user = user
                r.car = race_results.CAR
                logging.critical(f"{race_results.DRIVER}")
                r.driver = Driver.objects.get(name=race_results.DRIVER)
                r.start_pos = race_results.START
                r.finish_pos = race_results.POS
                r.manufacturer = race_results.MANUFACTURER
                r.race = Race.objects.get(name=race_info.DATE)
                r.save()
    #     for row in f_csv:
    #         print(row)
    #         row = Row(*row)
    #         print(row.TRACK)
    #         d = Track()
    #         d.name = row.TRACK
    #         d.owner = row.OWNER
    #         d.track_length = row.MILES
    #         d.configuration = row.CONFIG
    #         d.city = row.CITY
    #         d.state = row.STATE
    #         d.user = user
    #         d.save()
