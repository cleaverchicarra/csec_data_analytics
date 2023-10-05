from rest_framework import viewsets
from models import CVEItem
from serializers import CVEItemSerializer

class CVEItemViewSet(viewsets.ModelViewSet):
    queryset = CVEItem.objects.all()
    serializer_class = CVEItemSerializer
