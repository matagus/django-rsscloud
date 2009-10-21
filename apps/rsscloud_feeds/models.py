# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class UpdatePing(models.Model):
    """
    Consider it a log for all pings done to the rsscloud server
    in order to notify it when we publish a new blog post
    """
    
    # when it has been created
    created_at = models.DateTimeField(_("Created at"))
    # when it was done
    pinged_at = models.DateTimeField(_("Pinged at"))
    # how many times have we done it (zero means first try)
    retry_number = models.IntegerField(_("Retry number"), default=0)
    # what response code did the rsscloud server give us we had pinged it
    http_code = models.IntegerField(_("HTTP code"), null=True)
    # and what response message
    response_msg = models.CharField(_("Response message"),
        null=True, max_length=255)
    
    class Meta:
        verbose_name = _("Update Ping")
        verbose_name_plural = _("Update Pings")
        ordering = ('created_at', 'pinged_at', 'retry_number',)
        get_latest_by = "pinged_at"

    def __unicode__(self):
        return u"%s (%s)" % (self.http_code, self.retry_number)