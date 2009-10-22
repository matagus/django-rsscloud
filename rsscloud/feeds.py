# -*- coding: utf-8 -*-

from django.utils.feedgenerator import Rss201rev2Feed
from django.conf import settings


class CloudEnabledRss20Feed(Rss201rev2Feed):
    """
    """
    def cloud_attributes(self):

        # port 80 is used by default
        try:
            RSSCLOUD_PORT = settings.RSSCLOUD_PORT
        except AttributeError:
            RSSCLOUD_PORT = "80"
            
        return {
            "domain": settings.RSSCLOUD_URL,
            "port": RSSCLOUD_PORT,
            "path": settings.RSSCLOUD_PATH,
            "protocol": "http-post",
            "registerProcedure": ""
        }

    def add_root_elements(self, handler):
        super(Rss201rev2Feed, self).add_root_elements(handler)
        handler.addQuickElement(u"cloud", attrs=self.cloud_attributes())
