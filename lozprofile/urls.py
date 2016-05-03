#!/usr/bin/env python

from django.conf.urls import url, include

from views import signup_pro, signup_part, profile_pro_display, profile_part_display

urlpatterns = [
    url(r'^pro/signup$', signup_pro),
    url(r'^part/signup$', signup_part),
    url(r'^pro/(?P<username>\w+)$', profile_pro_display),
    url(r'^part/(?P<username>\w+)$', profile_part_display),

    #La connexion (signin) est la meme pour le pro et le particulier
]
