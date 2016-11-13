from .models import Country
from rest_framework import viewsets
from .serializers import CountrySerializer


class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Country.objects.all().order_by('-name')
    serializer_class = CountrySerializer
