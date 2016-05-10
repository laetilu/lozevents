#!/usr/bin/env python

from views import event_display, event_list, event_create
from django.conf.urls import url, include

urlpatterns = [
    url(r'^list$', event_list, name="event-list"),
    url(r'^create$', event_create, name="event-create"),
    url(r'^(?P<slug>[\w-]+)$', event_display, name="event-display"),
]
