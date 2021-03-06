from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .load import run
from .models import Country
from .utils import get_country_border_as_geojson
from .utils import get_capitalized_country_name
from .utils import get_country_centroid_as_geojson
import zipfile

# Create your tests here.


class CountryTestCase(TestCase):
    """
    Here's where we write tests for particular functions and methods
    """

    def setUp(self):
        polygon_wkt = (
            "MULTIPOLYGON(((-61.686668 17.0244410000001,-61.73806 16.989719,"
            "-61.82917 16.996944,-61.876114 17.016941,-61.880562 17.019722,"
            "-61.883614 17.023609,-61.885834 17.028053,-61.887222 "
            "17.0330540000001,-61.891113 17.094166,-61.887222 17.105274,"
            "-61.884171 17.109722,-61.832779 17.163887,-61.826393 "
            "17.167221,-61.794449 17.16333,-61.784172 17.158333,-61.744171 "
            "17.137218,-61.674171 17.093609,-61.67028 17.090275,"
            "-61.668892 17.084999,-61.666389 17.04583,-61.667503 "
            "17.040554,-61.682503 17.027496,-61.686668 17.0244410000001))"
            ",((-61.729172 17.608608,-61.731117 17.547222,-61.73278 "
            "17.541111,-61.738892 17.5405540000001,-61.751945 "
            "17.549442,-61.815559 17.583885,-61.834724 17.588608,"
            "-61.839447 17.586666,-61.842781 17.582775,-61.847504 "
            "17.5808300000001,-61.853058 17.583054,-61.856674 "
            "17.592499,-61.873894 17.688889,-61.875282 17.698608,"
            "-61.873062 17.703888,-61.850281 17.7227750000001,-61.845558 "
            "17.724998,-61.839172 17.7247200000001,-61.787224 17.700554,"
            "-61.783615 17.69722,-61.74334 17.653053,-61.74028 17.649166,"
            "-61.73806 17.6447220000001,-61.731674 17.624996,-61.729172 17."
            "608608)))")
        country = Country.objects.create(
            name="My Country",
            area=191919,
            translated_name="Mi País",
            pop2005=1000,
            un=19191919,
            fips="MC",
            iso2="MC",
            iso3="MCN",
            region=999999,
            subregion=99999,
            lat=19.89,
            lon=-99.09,
            phone_code="52",
            mpoly=polygon_wkt)
        country.save()

    def test_load_run(self):
        """
        Test that we can load the data from zipfile
        """
        zip_ref = zipfile.ZipFile('world/data/TM_WORLD_BORDERS-0.3.zip', 'r')
        zip_ref.extractall('world/data/')
        zip_ref.close()
        if run(verbose=False):
            self.assertEquals(True, True)

    def test_get_country(self):
        """
        Test that we can get the created country
        """
        c = Country.objects.get(name="My Country")
        self.assertEquals(c.translated_name, "Mi País")

    def test_get_country_border_as_geojson(self):
        """
        Test to get a GeoJSON object from created country
        """
        result = get_country_border_as_geojson("My Country")
        empty_json = {"error": "Not good"}
        self.assertJSONNotEqual(result, empty_json)

    def test_get_country_border_as_geojson_except(self):
        """
        Test to raise an exception from an unexistent country
        """
        with self.assertRaises(Country.DoesNotExist):
            get_country_border_as_geojson("My County")

    def test_get_capitalized_country_name(self):
        """
        Test that we can get a capitalized name for the country
        """
        result = get_capitalized_country_name("mexico es un pais")
        self.assertEquals(result, "Mexico Es Un Pais")

    def test_get_country_centroid_as_geojson(self):
        """
        Test that we can generate a GeoJSON point from mpoly field
        within a given country
        """
        result = get_country_centroid_as_geojson("My Country")
        empty_json = {"error": "Not good"}
        self.assertJSONNotEqual(result, empty_json)


class CountryAPITestCase(APITestCase):
    """
    Here's where we put tests for API REST endpoints
    """

    def setUp(self):
        polygon_wkt = (
            "MULTIPOLYGON(((-61.686668 17.0244410000001,-61.73806 16.989719,"
            "-61.82917 16.996944,-61.876114 17.016941,-61.880562 17.019722,"
            "-61.883614 17.023609,-61.885834 17.028053,-61.887222 "
            "17.0330540000001,-61.891113 17.094166,-61.887222 17.105274,"
            "-61.884171 17.109722,-61.832779 17.163887,-61.826393 "
            "17.167221,-61.794449 17.16333,-61.784172 17.158333,-61.744171 "
            "17.137218,-61.674171 17.093609,-61.67028 17.090275,"
            "-61.668892 17.084999,-61.666389 17.04583,-61.667503 "
            "17.040554,-61.682503 17.027496,-61.686668 17.0244410000001))"
            ",((-61.729172 17.608608,-61.731117 17.547222,-61.73278 "
            "17.541111,-61.738892 17.5405540000001,-61.751945 "
            "17.549442,-61.815559 17.583885,-61.834724 17.588608,"
            "-61.839447 17.586666,-61.842781 17.582775,-61.847504 "
            "17.5808300000001,-61.853058 17.583054,-61.856674 "
            "17.592499,-61.873894 17.688889,-61.875282 17.698608,"
            "-61.873062 17.703888,-61.850281 17.7227750000001,-61.845558 "
            "17.724998,-61.839172 17.7247200000001,-61.787224 17.700554,"
            "-61.783615 17.69722,-61.74334 17.653053,-61.74028 17.649166,"
            "-61.73806 17.6447220000001,-61.731674 17.624996,-61.729172 17."
            "608608)))")
        country = Country.objects.create(
            name="My Country",
            area=191919,
            translated_name="Mi País",
            pop2005=1000,
            un=19191919,
            fips="MC",
            iso2="MC",
            iso3="MCN",
            region=999999,
            subregion=99999,
            lat=19.89,
            lon=-99.09,
            phone_code="52",
            mpoly=polygon_wkt)
        country.save()

    def test_create_country_serializer(self):
        """
        Ensure that we can get all countries JSON
        """
        url = '/countries/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Country.objects.count(), 1)
        self.assertEqual(Country.objects.get().name, 'My Country')

    def test_get_border_as_geojson(self):
        """
        Ensure we can get GeoJSON for a given country
        """
        url = '/countries/get_border_as_geojson/My%20Country/'
        response = self.client.get(url, format='json')
        empty_json = {"error": "Not good"}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type'], 'MultiPolygon')
        self.assertNotEqual(response.data, empty_json)

    def test_get_centroid_as_geojson(self):
        """
        Ensure we can get a centroid JSON for a given country
        """
        url = '/countries/get_centroid_as_geojson/My%20Country/'
        response = self.client.get(url, format='json')
        empty_json = {"error": "Not good"}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type'], 'Point')
        self.assertNotEqual(response.data, empty_json)
