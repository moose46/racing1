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
        python manage.py runscript load_tracks_from_csv
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
from nascar.models import Race, Track

# https://k0nze.dev/posts/python-relative-imports-vscode/

# https://k0nze.dev/posts/python-relative-imports-vscode/
file_path = Path.cwd() / "scripts" / "results" / "2022"
logging.basicConfig(
    filename="log_load_races.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)


def run():
    user = User.objects.get(pk=1)
    for race in file_path.glob("*.csv"):
        logging.info(f"race={race}")
        with open(race) as f:
            reader = csv.reader(f, delimiter="\t")
            RaceInfo = namedtuple("RaceInfo", next(reader), rename=True)
            for row in reader:
                data = RaceInfo(*row)
                logging.info(f"{data}")
                # for row in reader:
                logging.info(f"data.DATE={data.DATE}")
                logging.info(f"data.TRACK={data.TRACK}")

                race = Race.objects.get(race_date=data.DATE)
                logging.info(f"get race={race}")
                race = Race()
                race.user = user
                race.track = Track.objects.get(name=data.TRACK)
                race.race_date = data.DATE
                race.save()
                logging.info(f"{race}")
                break  # Just read the header
