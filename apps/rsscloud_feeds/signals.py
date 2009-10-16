# -*- coding: utf-8 -*-

from urllib2 import urlopen
from urllib import urlencode
from datetime import datetime, timedelta

from django.utils.translation import ugettext as _
from django.conf import settings

from rsscloud_feeds.models import UpdatePing

# make it safe
RETRY_SECONDS = getattr(settings, "RSSCLOUD_PING_RETRY_SECONDS", 60)
RETRY_COUNT = getattr(settings, "RSSCLOUD_PING_RETRY_COUNT", 3)

def ping(sender, instance):
    #try:
        #req = urlopen(settings.RSSCLOUD_PING_URL,
            #data=urlencode({"url": settings.RSSCLOUD_FEED_URL}))
        #res = req.read()
    #except :
        #pass

    # schedule a ping
    update_ping = UpdatePing()
    update_ping.created_at = datetime.now()
    update_ping.scheduled_for = datetime.now() + timedelta(0, RETRY_SECONDS)
    # for future pings retry_number is zero
    update_ping.retry_number = 0
    update_ping.http_code = None
    update_ping.response_msg = None
    update_ping.save()
    

