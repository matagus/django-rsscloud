# -*- coding: utf-8 -*-

from django.contrib import admin
from rsscloud.models import UpdatePing


class UpdatePingAdmin(admin.ModelAdmin):
    list_display = ("pinged_at", "created_at", "http_code", "retry_number")
    list_display_links = ("pinged_at", )
    list_filter = ("http_code", "retry_number")
    list_per_page = 15
    ordering = ("-pinged_at", )

admin.site.register(UpdatePing, UpdatePingAdmin)
