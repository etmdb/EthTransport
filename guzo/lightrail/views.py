"""
Ethiopian Transport API
Views
"""

__author__ = "Dawit Nida (dawit@dawitnida.com)"
__date__ = "Date: 18-11-2017"
__version__ = "Version: 1.0.0"
__Copyright__ = "Copyright: @dawitnida"

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *
from .models import *


# Custom DB Selector #QuickFix for using multiple DB
# DB_SCOPE = 'guzo_prod.db'


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer = GroupSerializer
    serializer_class = serializer


class StationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows station to be viewed or edited.
    """
    queryset = Station.objects.all()
    serializer = StationSerializer
    serializer_class = serializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows service metadata to be viewed or edited.
    """
    queryset = Service.objects.all()
    serializer = ServiceSerializer
    serializer_class = serializer


class TechnicalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows technical to be viewed or edited.
    """
    queryset = Technical.objects.all()
    serializer = TechnicalSerializer
    serializer_class = serializer


class MediaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows media to be viewed or edited.
    """
    queryset = Media.objects.all()
    serializer = MediaSerializer
    serializer_class = serializer


class PriceQuotaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows price quota to be viewed or edited.
    """
    queryset = PriceQuota.objects.all()
    serializer = PriceQuotaSerializer
    serializer_class = serializer
