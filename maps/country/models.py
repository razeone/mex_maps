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
