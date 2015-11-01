from rest_framework import viewsets

from models import Business
from serializers import *


class BusinessViewSet(viewsets.ModelViewSet):

    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
