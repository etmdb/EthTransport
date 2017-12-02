"""
Ethiopian Transport API
GraphQl schema
"""

__author__ = "Dawit Nida (dawit@dawitnida.com)"
__date__ = "Date: 21-11-2017"
__version__ = "Version: 1.0.0"
__Copyright__ = "Copyright: @dawitnida"

from guzo.lightrail.models import *
from graphene import Node, Schema, ObjectType
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType

"""
Represents the types of services.
"""


class ServiceNode(DjangoObjectType):
    class Meta:
        model = Service
        interfaces = (Node,)


"""
Represents the types of Stations.
"""


class StationNode(DjangoObjectType):
    class Meta:
        model = Station
        interfaces = (Node,)


class Query(ObjectType):
    service = Node.Field(ServiceNode)
    all_services = DjangoConnectionField(ServiceNode)

    station = Node.Field(StationNode)
    all_stations = DjangoConnectionField(StationNode)


schema = Schema(query=Query)
