# -*- coding: utf-8 -*-

from django.utils.feedgenerator import Rss201rev2Feed
from django.conf import settings


class CloudEnabledRss20Feed(Rss201rev2Feed):
    """
    """
    def cloud_attributes(self):
        return {
            "domain": settings.RSSCLOUD_URL,
            "port": settings.RSSCLOUD_PORT,
            "path": settings.RSSCLOUD_PATH,
            "registerProcedure": settings.RSSCLOUD_REGPROC,
            "protocol": settings.RSSCLOUD_PROTOCOL
        }

    def add_root_elements(self, handler):
        super(Rss201rev2Feed, self).add_root_elements(handler)
        handler.addQuickElement(u"cloud", attrs=self.cloud_attributes())
