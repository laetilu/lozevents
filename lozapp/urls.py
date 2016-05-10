#!/usr/bin/env python

from views import event_display, EventListView, EventCreateView
from django.conf.urls import url, include

urlpatterns = [
    url(r'^list$', EventListView.as_view(), name="event-list"),
    url(r'^create$', EventCreateView.as_view(), name="event-create"),
    url(r'^(?P<slug>[\w-]+)$', event_display, name="event-display"),
]
