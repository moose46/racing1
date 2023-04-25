from django.contrib import admin

from .models import Driver

# Register your models here.


class DriverAdmin(admin.ModelAdmin):
    list_display = ["name", "team", "sponsor", "make", "salary"]
    ordering = ["-salary", "name"]


admin.site.register(Driver, DriverAdmin)
