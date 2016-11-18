from .models import Country
from django.contrib.gis.db.models.functions import AsGeoJSON
from django.contrib.gis.db.models.functions import Centroid


def get_capitalized_country_name(name):
    splitted_name = name.split()
    capitalized_name = [word.capitalize() for word in splitted_name]
    return(' '.join(capitalized_name))


def get_country_border_as_geojson(name):
    """
    Gets a country name and returns its corresponding
    GeoJSON object
    """
    try:
        result = Country.objects.annotate(
            json=AsGeoJSON('mpoly')).get(
            name=name).json
        return(result)
    except Country.DoesNotExist as error:
        raise Country.DoesNotExist(error)


def get_country_centroid_as_geojson(name):
    """
    Gets a country centroid as GeoJSON
    hint: nested geofunction calls
    """
    try:
        result = Country.objects.annotate(
            json=AsGeoJSON(Centroid('mpoly'))).get(
            name=name)
        return(result)
    except Country.DoesNotExist as error:
        raise Country.DoesNotExist(error)
