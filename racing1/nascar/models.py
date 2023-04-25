from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Base(models.Model):
    now = timezone.datetime
    createdAt = models.DateTimeField("date created", auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    updatedAt = models.DateTimeField("date last updated", auto_now=True, null=True)

    class Meta:
        abstract = True


class Driver(Base):
    name = models.CharField(max_length=32, default="")
    salary = models.IntegerField(default=0)
    starting_position = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
