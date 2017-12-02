"""
Ethiopian Transport API
URL Configuration for guzo project
"""

__author__ = "Dawit Nida (dawit@dawitnida.com)"
__date__ = "Date: 18-11-2017"
__version__ = "Version: 1.0.0"
__Copyright__ = "Copyright: @dawitnida"

from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import url, include
from rest_framework import routers
from guzo.lightrail import views

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
router.register(r'stations', views.StationViewSet)
router.register(r'service', views.ServiceViewSet)
router.register(r'technical', views.TechnicalViewSet)
router.register(r'media', views.MediaViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]

from graphene_django.views import GraphQLView

# Register GraphQL endpoint
urlpatterns += [
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
]

# OAuth2 provider

urlpatterns = [
    url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Addis Ababa Light Rail API Documentation')

urlpatterns += [
    url(r'^api/endpoints/$', schema_view)
]
