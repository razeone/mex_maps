from django.conf.urls import url
from django.conf.urls import include

# We need to check that gives us the format_suffix_patterns
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from .views import CountryViewSet
from .views import GetGeoJSONByCountry
from .views import GetCentroidByCountry

router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^countries/get_border_as_geojson/(?P<country>[^0-9]+)/$',
        GetGeoJSONByCountry.as_view()),
    url(r'^countries/get_centroid_as_geojson/(?P<country>[^0-9]+)/$',
        GetCentroidByCountry.as_view())
]

#urlpatterns = format_suffix_patterns(urlpatterns)
