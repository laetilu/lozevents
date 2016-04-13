#!/usr/bin/env python

from views import eventclick, events, homepage, log, logpart, logpro, post, userpart, userpro
from django.conf.urls import url, include


urlpatterns = [
    url(r'^$', homepage),
    url(r'^eventclick$', eventclick),
    url(r'^events$', events),
    url(r'^log$', log),
    url(r'^logpro$', logpro),
    url(r'^logpart$', logpart),
    url(r'^post$', post),
    url(r'^userpro$', userpro),
    url(r'^userpart$', userpart),
]
