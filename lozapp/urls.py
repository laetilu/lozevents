#!/usr/bin/env python
from views import eventclick, events, homepage, log, logpart, logpro, post, userpart, userpro

urlpatterns = [
    url(r'^$', homepage),
    url(r'^$', eventclick),
    url(r'^$', events),
    url(r'^$', log),
    url(r'^$', logpro),
    url(r'^$', logpart),
    url(r'^$', post),
    url(r'^$', userpro),
    url(r'^$', userpart),
]
