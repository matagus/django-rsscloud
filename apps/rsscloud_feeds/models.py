# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class UpdatePing(models.Model):
    """
    A POST ping to the rsscloud server to notify it
    when we publish a new blog post
    """
    
    # what response code did the rsscloud server give us we had pinged it
    http_code = models.IntegerField(_("HTTP Code"), default=200)
    # how many times have we done it
    retry_number = models.IntegerField(_("Retry Number"), default=1)
    # and when it has occurred
    created_at = models.DateTimeField(_("Date created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Update Ping")
        verbose_name_plural = _("Update Pings")
        ordering = ('created_at', 'retry_number',)

    def __unicode__(self):
        return u"%s (%s)" % (self.http, self.retry_number) 