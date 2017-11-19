from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *
from .models import *


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


class OverviewMetadataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows overview metadata to be viewed or edited.
    """
    queryset = OverviewMetadata.objects.all()
    serializer = OverviewMetadataSerializer
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
