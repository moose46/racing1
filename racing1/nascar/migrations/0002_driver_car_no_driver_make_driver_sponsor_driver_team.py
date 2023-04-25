# Generated by Django 4.2 on 2023-04-25 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nascar", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="driver",
            name="car_no",
            field=models.IntegerField(default=99),
        ),
        migrations.AddField(
            model_name="driver",
            name="make",
            field=models.CharField(default="Toyota", max_length=32),
        ),
        migrations.AddField(
            model_name="driver",
            name="sponsor",
            field=models.CharField(default="", max_length=64),
        ),
        migrations.AddField(
            model_name="driver",
            name="team",
            field=models.CharField(default="", max_length=64),
        ),
    ]
