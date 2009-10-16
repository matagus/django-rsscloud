# -*- coding: utf-8 -*-

from django.contrib import admin
from rsscloud_feeds.models import UpdatePing


class UpdatePingAdmin(admin.ModelAdmin):
    list_display = ("scheduled_for", "created_at", "http_code", "retry_number")
    list_display_links = ("scheduled_for", )
    list_filter = ("http_code", "retry_number")
    list_per_page = 15
    ordering = ("-scheduled_for", )

admin.site.register(UpdatePing, UpdatePingAdmin)
