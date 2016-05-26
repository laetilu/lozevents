#!/usr/bin/env python

from django.conf.urls import url, include
from views import *
from forms import SignupFormExtra


urlpatterns = [
    url(r'^', include('userena.urls')),
    # url(r'^accounts/signup/$', 'accounts.views.sign_up'),
    url(r'^signin$', 'userena.views.signin', {'template_name': 'signin.html'}, name="lozsignin"),
    url(r'^signout$', 'userena.views.signout', name="lozsignout"),
    url(r'^signup$', 'userena.views.signup', {'template_name': 'signup.html', 'success_url': '/', 'signup_form': SignupFormExtra}, name="lozsignup"),

    # url(r'^login$', login, name="login"),
    # url(r'^pro/signup$', signup_pro, name="sign-up-pro"),
    # url(r'^part/signup$', signup_part, name="sign-up-part"),
    # url(r'^pro/(?P<username>\w+)$', profile_pro_display, name="profile-pro-display" ),
    # url(r'^part/(?P<username>\w+)$', profile_part_display,name="profile-part-display" ),

    #La connexion (signin) est la meme pour le pro et le particulier
]
