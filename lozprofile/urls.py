#!/usr/bin/env python

from django.conf.urls import url, include

from views import signup_pro, signup_part, profile_pro_display, profile_part_display, login

urlpatterns = [
    url(r'^login$', login, name="login"),
    url(r'^pro/signup$', signup_pro, name="sign-up-pro"),
    url(r'^part/signup$', signup_part, name="sign-up-part"),
    url(r'^pro/(?P<username>\w+)$', profile_pro_display, name="profile-pro-display" ),
    url(r'^part/(?P<username>\w+)$', profile_part_display,name="profile-part-display" ),

    #La connexion (signin) est la meme pour le pro et le particulier
]
