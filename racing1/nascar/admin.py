from django.contrib import admin

from .models import Driver, Race, Track

# Register your models here.


class DriverAdmin(admin.ModelAdmin):
    list_display = ["name", "team", "sponsor", "make", "salary"]
    ordering = ["-salary", "name"]


class TrackAdmin(admin.ModelAdmin):
    list_display = ["name", "configuration", "track_length"]


admin.site.register(Driver, DriverAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Race)
