#!/usr/bin/env python
from django.shortcuts import render

def homepage(request):
    return render(request, "homepage.html")

def event_display(request):
    return render(request, "eventdisplay.html")

def event_list(request):
    return render(request, "eventlist.html")

def event_create(request):
    return render(request, "eventcreate.html")
