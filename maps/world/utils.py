from .models import Country
from django.contrib.gis.db.models.functions import AsGeoJSON
from django.contrib.gis.db.models.functions import Centroid


def get_capitalized_country_name(name):
    """
    This is necesary to allow upper and lower case in the APIs
    """
    splitted_name = name.split()
    capitalized_name = [word.capitalize() for word in splitted_name]
    return(' '.join(capitalized_name))


def get_country_border_as_geojson(name):
    """
    Gets a country name and returns its corresponding
    GeoJSON object
    """
    if(name[0].islower()):
        name = get_capitalized_country_name(name)
    try:
        country = Country.objects.annotate(
            json=AsGeoJSON('mpoly')).get(
            name=name).json
        return(country)
    except Country.DoesNotExist as error:
        raise Country.DoesNotExist(error)


def get_country_centroid_as_geojson(name):
    """
    Gets a country centroid as GeoJSON
    hint: nested geofunction calls
    """
    if(name[0].islower()):
        name = get_capitalized_country_name(name)
    try:
        country = Country.objects.annotate(
            json=AsGeoJSON(Centroid('mpoly'))).get(
            name=name).json
        return(country)
    except Country.DoesNotExist as error:
        raise Country.DoesNotExist(error)
