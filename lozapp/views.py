#!/usr/bin/env python
from django.shortcuts import render

def homepage(request):
    return render(request, "homepage.html")

def event_display(request, slug):
    return render(request, "event_display.html")

def event_list(request):
    return render(request, "event_list.html")

def event_create(request):
    return render(request, "event_create.html")
