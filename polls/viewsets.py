from rest_framework import  viewsets
from polls.models import DustBin
from polls.serializers import DustBinSerializer


# ViewSets define the view behavior.
class DustBinViewSet(viewsets.ModelViewSet):
    queryset = DustBin.objects.all()
    serializer_class = DustBinSerializer
