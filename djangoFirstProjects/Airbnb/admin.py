from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.City)
admin.site.register(models.Property, models.PropertyAdmin)
admin.site.register(models.Reservation)

