from .models import Country
from .serializers import CountrySerializer
from .utils import get_country_border_as_geojson
from .utils import get_country_centroid_as_geojson

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import json


class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Country.objects.all().order_by('-name')
    serializer_class = CountrySerializer


class GetGeoJSONByCountry(APIView):
    """
    Class based view to retrieve GeoJSON border for a given country name
    """
    permission_classes = (AllowAny,)

    def get(self, request, country):
        try:
            result = json.loads(get_country_border_as_geojson(country))
            return Response(result, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            error_result = {'error': 'Not found'}
            return Response(error_result, status=status.HTTP_404_NOT_FOUND)



#@api_view(['GET'])
def get_geojson_centroid_by_country(request):
    if request.method == 'GET':
        get_country_centroid_as_geojson()
        return Response()
