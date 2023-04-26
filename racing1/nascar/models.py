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


class Driver(Base):
    name = models.CharField(max_length=32, default="", null=False)
    car_no = models.IntegerField(default=99)
    sponsor = models.CharField(max_length=64, default="N/A")
    make = models.CharField(max_length=32, default="N/A")
    team = models.CharField(max_length=64, default="N/A")
    salary = models.IntegerField(default=3000)
    starting_position = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    class Meta:
        unique_together = ["name", "team"]
        ordering = ["name"]


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
