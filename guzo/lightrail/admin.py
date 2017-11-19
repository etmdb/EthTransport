"""
Ethiopian Transport API
Admin
"""

__author__ = "Dawit Nida (dawit@dawitnida.com)"
__date__ = "Date: 18-11-2017"
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


class OverviewMetadataAdmin(BaseAdmin):
    list_display = ('name', 'locale', 'number_of_lines', 'number_of_stations', 'number_of_stations',
                    'transit_type', 'budget', 'daily_ridership', 'operation_start_date',
                    'operators', 'number_of_vehicles',) + BaseAdmin.list_display
    list_filter = ('name',)
    search_fields = ('name',)

    class Meta:
        model = Station


class TechnicalAdmin(BaseAdmin):
    list_display = ('system_length', 'track_gauge', 'top_speed', 'electrification',) + BaseAdmin.list_display

    class Meta:
        model = Technical


class MediaAdmin(BaseAdmin):
    list_display = ('gallery_type', 'image_data', 'caption', 'overview', 'video_url',) + BaseAdmin.list_display
    list_filter = ('gallery_type',)
    search_fields = ('gallery_type', 'caption', 'overview',)

    class Meta:
        model = Media


class LogEntryAdmin(BaseAdmin):
    list_display = ('id', 'action_time', 'user', 'content_type', 'object_id',
                    'object_repr', 'action_flag', 'change_message',)
    search_fields = ('user',)

    class Meta:
        model = LogEntry


admin.site.register(OverviewMetadata, OverviewMetadataAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Technical, TechnicalAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
