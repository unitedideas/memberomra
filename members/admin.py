from django.contrib import admin
from .models import *


@admin.register(Race, Rider, RiderClass, Position, Series, Year, Club, PositionValues)
class PersonAdmin(admin.ModelAdmin):
    pass
