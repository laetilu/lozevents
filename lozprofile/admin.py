from django.contrib import admin

from models import ProfilePro, ProfilePart
from lozapp.models import Categorie, Event, Address



admin.site.register(ProfilePart)
admin.site.register(ProfilePro)
admin.site.register(Event)
admin.site.register(Categorie)
admin.site.register(Address)
