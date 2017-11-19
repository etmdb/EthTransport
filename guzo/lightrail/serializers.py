""" 
Ethiopian Transport API
Serializers
"""

__author__ = "Dawit Nida (dchonch@gmail.com)"
__date__ = "Date: 18/11/2017"
__version__ = "Version: 1.0.0"
__Copyright__ = "Copyright: @dawitnida"

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import *


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('uuid', 'created_date', 'updated_date', 'slug',)
        read_only_fields = ('uuid', 'created_date', 'updated_date',)

    def to_representation(self, instance):
        representation = super(BaseSerializer, self).to_representation(instance)
        representation['created_date'] = instance.created_date.strftime('%Y-%m-%d %H:%M:%S')
        representation['updated_date'] = instance.updated_date.strftime('%Y-%m-%d %H:%M:%S')
        return representation


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'is_staff',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        name_ = ('url', 'name')
        fields = ('url', 'name')


class OverviewMetadataSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = OverviewMetadata
        fields = BaseSerializer.Meta.fields + ('url', 'locale', 'name', 'number_of_lines', 'number_of_stations',
                                               'transit_type', 'budget', 'daily_ridership', 'operation_start_date',
                                               'operators', 'number_of_vehicles',)


class StationSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Station
        fields = BaseSerializer.Meta.fields + ('url', 'code', 'name', 'is_operational', 'long', 'lat',)


class TechnicalSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Technical
        fields = BaseSerializer.Meta.fields + ('url', 'system_length', 'track_gauge', 'top_speed', 'electrification',)


class MediaSerializer(BaseSerializer):
    overview = OverviewMetadata

    class Meta(BaseSerializer.Meta):
        model = Media
        fields = BaseSerializer.Meta.fields + ('url', 'gallery_type', 'image_data', 'caption', 'overview', 'video_url',)
