# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class UpdatePing(models.Model):
    """
    A POST ping to the rsscloud server to notify it
    when we publish a new blog post
    """
    
    # when it has been created
    created_at = models.DateTimeField(_("Date created"), auto_now_add=True)
    # when it will run
    scheduled_for = models.DateTimeField(_("Scheduled for"))
    # how many times have we done it (zero means never)
    retry_number = models.IntegerField(_("Retry Number"), default=0)
    # what response code did the rsscloud server give us we had pinged it
    # None when it's an future ping
    http_code = models.IntegerField(_("HTTP Code"), null=True)
    # and what response message
    response_msg = models.CharField(_("Response Message"),
        null=True, max_length=255)
    
    class Meta:
        verbose_name = _("Update Ping")
        verbose_name_plural = _("Update Pings")
        ordering = ('created_at', 'retry_number',)

    def __unicode__(self):
        return u"%s (%s)" % (self.http_code, self.retry_number)