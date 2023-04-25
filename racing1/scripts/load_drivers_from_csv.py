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
        python manage.py runscript load_drivers_from_csv
"""
import csv
import os
import sys
from collections import namedtuple
from pathlib import Path

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from nascar.models import Driver

# https://k0nze.dev/posts/python-relative-imports-vscode/


def run():
    user = User.objects.get(pk=1)
    with open(Path.cwd() / "scripts" / "drivers.csv") as f:
        f_csv = csv.reader(f, delimiter="\t")
        headers = next(f_csv)
        Row = namedtuple("Row", headers)
        for row in f_csv:
            print(row)
            row = Row(*row)
            print(row.NAME)
            d = Driver()
            d.name = row.NAME
            d.car_no = row.NO
            d.sponsor = row.SPONSOR
            d.make = row.MAKE
            d.team = row.TEAM
            d.salary = row.SALARY
            d.user = user
            d.save()
