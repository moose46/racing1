from django.contrib import admin

from .models import Driver

# Register your models here.


class DriverAdmin(admin.ModelAdmin):
    list_display = ["name", "team", "sponsor", "make", "salary"]


admin.site.register(Driver, DriverAdmin)
