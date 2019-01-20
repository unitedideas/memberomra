from django.contrib import admin
from .models import *

admin.site.register(RiderClass)
# admin.site.register(Year)
admin.site.register(Series)
admin.site.register(Race)
# admin.site.register(PositionValues)
admin.site.register(Position)
admin.site.register(Club)


class RiderAdmin(admin.ModelAdmin):
    list_display = ['lastName', 'firstName', 'phoneNumber', 'email', 'memberNumber', 'plateNumber', 'membershipYear']


admin.site.register(Rider, RiderAdmin)
