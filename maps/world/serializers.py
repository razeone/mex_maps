from .models import Country
from rest_framework import serializers


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = (
            'url',
            'name',
            'translated_name',
            'area',
            'pop2005',
            'fips',
            'iso2',
            'iso3',
            'un',
            'region',
            'subregion',
            'lat',
            'lon',
            'phone_code')
