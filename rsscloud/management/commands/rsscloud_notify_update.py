# -*- coding: utf-8 -*-

from datetime import datetime
from urllib2 import urlopen, HTTPError, URLError
from urllib import urlencode

from django.core.management.base import BaseCommand
from django.conf import settings

from rsscloud.models import UpdatePing

# make it safe
RETRY_COUNT = getattr(settings, "RSSCLOUD_PING_RETRY_COUNT", 3)


class Command(BaseCommand):
    
    help = "Pings to the rsscloud server to tell it"\
        "that we've got new fresh content!"\
        "It must be setted to run as a cron job."

    def handle(self, *args, **options):

        last_ping = UpdatePing.objects.latest()

        # if the last ping wasn't successful
        # and we didn't reach the RETRY_COUNT limit yet...
        if (last_ping.http_code not in (200, 201, 202, 204)) and\
            (last_ping.retry_number < RETRY_COUNT):

            now = datetime.now()

            try:
                req = urlopen(settings.RSSCLOUD_PING_URL,
                    data=urlencode({"url": settings.RSSCLOUD_FEED_URL}))

                res = req.read()

                http_code = req.code
                response_msg = res

            except HTTPError, e:
                http_code = e.code
                response_msg = e.read()

            except URLError, e:
                http_code = None
                response_msg = _("Could not connect")

            finally:
                update_ping = UpdatePing()
                update_ping.created_at = now
                update_ping.pinged_at = now
                update_ping.retry_number = last_ping.retry_number + 1
                update_ping.http_code = http_code
                update_ping.response_msg = response_msg
                update_ping.save()
        
        