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
# class Driver2(models.Model):
#     now = timezone.datetime
#     createdAt = models.DateTimeField("date created", auto_now_add=True, null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     updatedAt = models.DateTimeField("date last updated", auto_now=True, null=True)
#     name = models.CharField(max_length=32, default="")
#     car_no = models.IntegerField(default=99)
#     sponsor = models.CharField(max_length=64, default="")
#     make = models.CharField(max_length=32, default="Toyota")
#     team = models.CharField(max_length=64, default="")
#     salary = models.IntegerField(default=0)
#     starting_position = models.IntegerField(default=0)

#     def __str__(self) -> str:
#         return str(self.name)


# import django


# sys.path.append("C:\\Users\\me\\Documents\\VisualCodeSource\\racing1\\racing1")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "racing1.settings")
# django.setup()


# from django.contrib.auth.models import User

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
