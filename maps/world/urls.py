from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import CountryViewSet
from .views import GetGeoJSONByCountry
from .views import GetCentroidByCountry

country_list = CountryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    url(r'^countries/$', country_list, name='country-view'),
    url(r'^countries/get_border_as_geojson/(?P<country>[^0-9]+)/$',
        GetGeoJSONByCountry.as_view()),
    url(r'^countries/get_centroid_as_geojson/(?P<country>[^0-9]+)/$',
        GetCentroidByCountry.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)