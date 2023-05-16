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
import os
import sys
import logging
from collections import namedtuple
from pathlib import Path

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from nascar.models import Track

# https://k0nze.dev/posts/python-relative-imports-vscode/
file_path = Path.cwd() / "scripts" / "results" / "2022"
logging.basicConfig(
    filename="log_file.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)


def run():
    logging.info(file_path)
    user = User.objects.get(pk=1)
    for race_results in file_path.glob("*.csv"):
        # results = f.stem.split("_")[1]
        logging.info(race_results)
        with open(race_results) as f:
            reader = csv.reader(f, delimiter="\t")
            rawResult = namedtuple("rawResult", next(reader), rename=True)
            logging.info(f"rawResults={rawResult}")
            race_header_fields = next(reader)
            logging.info(f"race_header_fields={race_header_fields}")
            result = rawResult(*race_header_fields)
            logging.info(f"race_header_fields={race_header_fields}")
            race_details = namedtuple("race_details", race_header_fields)
            # logging.info(f"race_track={race_details.TRACK}")
    #     # TRACK,OWNER,MILES,CONFIG,CITY,STATE
    #     Row = namedtuple("Row", headers)

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
