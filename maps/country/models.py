from django.contrib.gis.db import models
from django.utils.functional import cached_property

# Create your models here.
from world.models import Country


class CountryGeo(models.Model):
    country = models.OneToOneField(
        Country,
        on_delete=models.CASCADE)
    capital = models.CharField(max_length=100)
    capital_geom = models.PointField()

    @cached_property
    def __str__(self):
        return self.country.name

    @cached_property
    def get_country_border_as_geojson(self):
        query_text = '''select ST_AsGEOJSON(ST_Centroid(mpoly))
                     from world_country where name='''
        return self.objects.raw()
