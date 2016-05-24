#!/usr/bin/env python
from django.shortcuts import render
from models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy


def homepage(request):
    return render(request, "homepage.html")

def event_display(request, slug):
    return render(request, "event_display.html")




class EventListView(ListView):
   model = Event
   template_name = "event_list.html"
   context_object_name = "events"
   queryset = Event.objects.all().order_by('date_creation') #remplace la fonction get_queryset



class EventCreateView(CreateView):
    model = Event
    template_name = "event_create.html"
    fields = ['title', 'photo', 'begin_date', 'end_date', 'desc', 'categorie', 'addr', 'pro']
    success_url = reverse_lazy('event-list')

    def get_initial(self):
        return {"pro" : self.request.user}


class EventDisplayView(DetailView):
    model = Event
    template_name = "event_display.html"

    def get_context_data(self, **kwargs):
       context = super(EventDisplayView, self).get_context_data(**kwargs)
       context["event"] = self.get_object()
       return context
