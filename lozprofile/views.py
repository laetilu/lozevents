from django.shortcuts import render

def profile_part_display(request, username):
    return render(request, "profile_part_display.html")

def profile_pro_display(request, username):
    return render(request, "profile_pro_display.html")


#voir avec userena
def signup_pro(request):
    return render(request, "signup_pro.html")

def signup_part(request):
    return render(request, "signup_part.html")
