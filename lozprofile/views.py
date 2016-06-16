from django.shortcuts import render
from userena.views import signup, signin
from models import LozProfile

from django.views.generic import DetailView

from userena import settings as userena_settings
from lozapp.forms import SearchEventForm


def profile_detail(request, username,
   template_name=userena_settings.USERENA_PROFILE_DETAIL_TEMPLATE,
   extra_context=None, **kwargs):
   user = get_object_or_404(get_user_model(), username__iexact=username)
   profile = get_user_profile(user=user)
   if not profile.can_view_profile(request.user):
       raise PermissionDenied
   if not extra_context: extra_context = dict()
   extra_context['profile'] = profile
   extra_context["search_form"] = SearchEventForm()

   extra_context['hide_email'] = userena_settings.USERENA_HIDE_EMAIL
   return ExtraContextTemplateView.as_view(template_name=template_name,
                                           extra_context=extra_context)(request)
