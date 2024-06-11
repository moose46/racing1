import datetime
from ast import mod

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Base(models.Model):
    now = timezone.datetime
    createdAt = models.DateTimeField("date created", auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField("date last updated", auto_now=True, null=True)

    class Meta:
        abstract = True


class Team(Base):
    team_name = models.CharField(max_length=32, null=False)
    owner = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.team_name


class Driver(Base):
    CAR_MAKE_CHOICES = {
        "CHEVROLET": "Chevrolet",
        "TOYOTA": "Toyota",
        "FORD": "Ford",
    }
    # team_name = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, default="", null=False)
    car_no = models.IntegerField(default=99)
    sponsor = models.CharField(max_length=64, default="N/A")
    make = models.CharField(
        max_length=32, default=CAR_MAKE_CHOICES["CHEVROLET"], choices=CAR_MAKE_CHOICES
    )
    team_old = models.CharField(max_length=64, default="N/A")
    salary = models.IntegerField(default=3000)
    # starting_position = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    class Meta:
        unique_together = [
            "name",
            "team_old",
        ]
        ordering = ["name"]


class Track(Base):
    """TRACK,OWNER,MILES,CONFIG,CITY,STATE

    Args:
            Base (_type_): _description_
    """

    name = models.CharField(max_length=64, default="N/A", null=False)
    owner = models.CharField(max_length=64, default="N/A")
    track_length = models.FloatField(default=0.0, null=False)
    configuration = models.CharField(max_length=32, default="Oval", null=False)
    city = models.CharField(max_length=64, null=False, default="N/A")
    state = models.CharField(max_length=64, null=False, default="N/A")

    class Meta:
        models.UniqueConstraint(fields=["name"], name="unique_track_name")

    def __str__(self) -> str:
        return f"{self.name} {self.track_length} - {self.configuration}"


class Race(Base):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    race_date = models.DateField(null=False, auto_now_add=False, auto_now=False)
    models.UniqueConstraint(fields=["track", "race_date"], name="unique_race_date")

    def __str__(self) -> str:
        return f"{self.track} - {self.race_date}"


class Results(Base):
    """_summary_
    POS	DRIVER	CAR	MANUFACTURER	LAPS	START	LED	PTS	BONUS	PENALTY

    Args:
            Base (_type_): _description_
    """

    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    finish_pos = models.IntegerField(null=False, default=0)
    start_pos = models.IntegerField(null=False, default=0)
    car = models.IntegerField(null=False, default=0)
    manufacturer = models.CharField(null=False, max_length=32, default="N/A")


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
