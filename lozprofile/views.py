from django.shortcuts import render
from userena.views import signup, signin


def sign_up(request):
    #if user is authenticated, redirect to user's profile page
    #otherwise use userena signup view, with my own form,SignupFormExtra, instead of userena's

    if request.user.is_authenticated():
        username = request.user.username
        return HttpResponseRedirect('/')
    else:
        return signup(request,signup_form=SignupFormPart)
# def profile_part_display(request, username):
#     return render(request, "profile_part_display.html")
#
# def profile_pro_display(request, username):
#     return render(request, "profile_pro_display.html")
#
#
# #voir avec userena
# def signup_pro(request):
#     return render(request, "signup_pro.html")
#
# def signup_part(request):
#     return render(request, "signup_part.html")
#
# def login(request):
#     return render(request, "login.html")
