# -*- coding: utf-8 -*-

from urllib2 import urlopen, HTTPError, URLError
from urllib import urlencode
from datetime import datetime

from django.utils.translation import ugettext as _
from django.conf import settings

from rsscloud_feeds.models import UpdatePing


# make it safe
INSTANT_PING = getattr(settings, "RSSCLOUD_INSTANT_PING", True)


def ping(sender, instance, **kwargs):

    now = datetime.now()

    update_ping = UpdatePing()
    update_ping.created_at = now
    update_ping.pinged_at = now
    # it's our first try. no retries have been done yet.
    update_ping.retry_number = 0

    if INSTANT_PING:
        try:
            req = urlopen(settings.RSSCLOUD_PING_URL,
                data=urlencode({"url": settings.RSSCLOUD_FEED_URL}))

            res = req.read()

            update_ping.http_code = req.code
            update_ping.response_msg = res

        except HTTPError, e:
            update_ping.http_code = e.code
            update_ping.response_msg = e.read()       

        except URLError, e:
            update_ping.http_code = None
            update_ping.response_msg = _("Could not connect")

    else:
        # if ping is not instantaneous, we must simulate a failed ping
        # in order to make rsscloud_notify_update command make another ping
        update_ping.http_code = None
        update_ping.response_msg = None

    update_ping.save()
        
          


