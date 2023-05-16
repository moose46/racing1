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
import os
import sys
from collections import namedtuple
from pathlib import Path

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from nascar.models import Track

# https://k0nze.dev/posts/python-relative-imports-vscode/
file_path = Path.home() / "scripts" / "results"


def run():
    print(file_path)
    user = User.objects.get(pk=1)
    for f in file_path.glob("*.csv"):
        race_track = f.stem.split("_")[1]
        print(race_track)
    # with open(Path.cwd() / "scripts" / "tracks.csv") as f:
    #     f_csv = csv.reader(f, delimiter=",")
    #     headers = next(f_csv)
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
