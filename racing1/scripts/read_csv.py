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

files = Path.cwd() / "scripts"
print(Path.cwd())
all = Driver.objects.all()
for d in all:
    print(d)


def run():
    user = User.objects.get(pk=1)
    with open(
        "C:\\Users\\me\\Documents\\VisualCodeSource\\racing1\\racing1\\scripts\\drivers.csv"
    ) as f:
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
