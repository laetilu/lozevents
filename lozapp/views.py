#!/usr/bin/env python
from django.shortcuts import render

def homepage(request):
    return render(request, "homepage.html")

def eventclick(request):
    return render(request, "eventclick.html")

def events(request):
    return render(request, "events.html")

def log(request):
    return render(request, "log.html")

def logpart(request):
    return render(request, "logpart.html")

def logpro(request):
    return render(request, "logpro.html")

def post(request):
    return render(request, "post.html")

def userpro(request):
    return render(request, "userpro.html")

def userpart(request):
    return render(request, "userpart.html")
# Create your views here.
