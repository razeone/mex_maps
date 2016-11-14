from django.contrib.gis.db import models


class World(models.Model):
    """
    It's impossible to understand geospatial analysis without a 
    world/planet object
    """
    name = models.CharField('Name your world', max_length=100)


class Country(models.Model):
    """
    Regular Django fields corresponding to the attributes in the
    world borders shapefile.
    """
    name = models.CharField(max_length=50)
    translated_name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()
    phone_code = models.CharField(max_length=5, null=True)
    world = models.ForeignKey(World, on_delete=models.CASCADE)

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def get_lan_long(self):
        return {
            'lat': self.lat,
            'lon': self.lon
        }

    def get_geom(self):
        return self.mpoly
