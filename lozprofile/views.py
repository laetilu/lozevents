from django.shortcuts import render

def profile_part_display(request):
    return render(request, "profilepart.html")

def profile_pro_display(request):
    return render(request, "profilepro.html")


#voir avec userena
def signup_pro(request):
    return render(request, "userpro.html")

def signup_part(request):
    return render(request, "userpart.html")
