from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import CountryViewSet
from .views import GetGeoJSONByCountry

country_list = CountryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    url(r'^countries/$', country_list, name='country-view'),
    url(r'^countries/border_as_geojson/(?P<country>[^0-9]+)/$',
        GetGeoJSONByCountry.as_view()),
    # url(r'^customers/$', customer_list, name='customer-view'),
    # url(r'^customers/(?P<pk>[0-9]+)/$', customer_detail, name='customer-detail'),
    # url(r'^groups/$', group_list, name='group-view'),
    # url(r'^groups/(?P<pk>[0-9]+)/$', group_detail, name='group-detail'),
    # url(r'^subgroups/$', subgroup_list, name='subgroup-view'),
    # url(r'^subgroups/(?P<pk>[0-9]+)/$', subgroup_detail, name='subgroup-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)