from .models import Country
from django.contrib.gis.db.models.functions import AsGeoJSON
from django.contrib.gis.db.models.functions import Centroid


def get_country_border_as_geojson(name):
    """
    Gets a country name and returns its corresponding
    GeoJSON object
    """
    result = Country.objects.annotate(
        json=AsGeoJSON('mpoly')).get(
        name=name).json
    return(result)


def get_country_centroid_as_geojson(name):
    country = Country.objects.get(
        name=name)
    c = AsGeoJSON(Centroid(country.mpoly))
    print(c)
    #return result
