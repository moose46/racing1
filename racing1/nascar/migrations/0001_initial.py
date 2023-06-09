# Generated by Django 4.2 on 2023-04-26 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Driver",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "createdAt",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="date created"
                    ),
                ),
                (
                    "updatedAt",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="date last updated"
                    ),
                ),
                ("name", models.CharField(default="", max_length=32)),
                ("car_no", models.IntegerField(default=99)),
                ("sponsor", models.CharField(default="", max_length=64)),
                ("make", models.CharField(default="Toyota", max_length=32)),
                ("team", models.CharField(default="", max_length=64)),
                ("salary", models.IntegerField(default=0)),
                ("starting_position", models.IntegerField(default=0)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "unique_together": {("name", "team")},
            },
        ),
    ]
