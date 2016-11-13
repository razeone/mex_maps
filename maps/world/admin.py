from django.contrib.gis import admin
from .models import Country

admin.site.register(Country, admin.GeoModelAdmin)
