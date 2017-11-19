"""
Ethiopian Transport API
Admin
"""

__author__ = "Dawit Nida (dchonch@gmail.com)"
__date__ = "Date: 18/11/2017"
__version__ = "Version: 1.0.0"
__Copyright__ = "Copyright: @dawitnida"

from django.contrib import admin
from .models import *
from django.contrib.admin.models import LogEntry


class BaseAdmin(admin.ModelAdmin):
    list_display = (
        'uuid', 'slug', 'flag_approved', 'created_by', 'modified_by', 'created_date', 'updated_date')

    class Meta:
        abstract = True


class StationAdmin(BaseAdmin):
    list_display = ('name', 'code', 'long', 'lat', 'is_operational',) + BaseAdmin.list_display
    list_filter = ('name',)
    search_fields = ('name',)

    class Meta:
        model = Station


admin.site.register(Station, StationAdmin)
