# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _
from django.db.models.signals import post_save

from signals import ping


class AlreadyRegistered(Exception):
    """
    An attempt was made to register a model more than once.
    """
    pass

registry = []

def register(model):
    """
    Sets the given model class up for notifying for updates.
    """
    
    if model in registry:
        raise AlreadyRegistered(
            _('The model %s has already been registered.') % model.__name__)
    
    # otherwise...
    registry.append(model)

    post_save.connect(ping, model)


from planet.models import Post
register(Post)
