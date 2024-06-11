from django.contrib import admin

from .models import Driver, Race, Team, Track

# Register your models here.


class DriverAdmin(admin.ModelAdmin):
    list_display = ["name", "sponsor", "make", "salary", "team_old"]
    ordering = ["-salary", "name"]


admin.site.register(Driver, DriverAdmin)


class TrackAdmin(admin.ModelAdmin):
    list_display = ["name", "configuration", "track_length"]


admin.site.register(Track, TrackAdmin)


class RaceAdmin(admin.ModelAdmin):
    list_display = ["track", "race_date"]


admin.site.register(Race, RaceAdmin)
admin.site.register(Team)
