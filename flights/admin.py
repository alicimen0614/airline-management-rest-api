from django.contrib import admin
from flights import models

admin.site.register(models.Airplane)
admin.site.register(models.Flight)
admin.site.register(models.Reservation)

