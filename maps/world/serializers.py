from .models import Country
from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'id',
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

    def create(self, validated_data):
        country = Country(
            name=validated_data['name'],
            translated_name=validated_data['translated_name'],
            area=validated_data['area'],
            pop2005=validated_data['pop2005'],
            fips=validated_data['fips'],
            iso2=validated_data['iso2'],
            iso3=validated_data['iso3'],
            un=validated_data['un'],
            region=validated_data['region'],
            subregion=validated_data['subregion'],
            lat=validated_data['lat'],
            lon=validated_data['lon'],
            phone_code=validated_data['phone_code']
        )
        country.save()
        return country
