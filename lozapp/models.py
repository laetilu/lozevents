from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.contrib.gis.db import models

# Create your models here.



class Address(models.Model): #REGARDER GEODJANGO
    street = models.CharField(max_length=45)
    zipcode = models.CharField(max_length=5)
    city =  models.CharField(max_length=100)
    poly = models.PointField(null=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return "%s %s" % (self.city, self.street)

class Categorie(models.Model):
    name = models.CharField(max_length=45)

    def __unicode__(self):
        return "%s" % self.name


class Event(models.Model):


    title = models.CharField(max_length=45)
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    desc = models.TextField()
    slug = AutoSlugField(populate_from='title', null = True)
    date_creation = models.DateTimeField(auto_now_add=True)

    photo = models.ImageField(upload_to='events', null = True)

    categorie = models.ForeignKey(Categorie)

    pro = models.ForeignKey("lozprofile.ProfilePro")

    addr = models.ForeignKey(Address)

    is_validated = models.BooleanField(default=False)

    participant = models.ManyToManyField(User)

    def __unicode__(self):
        return "%s" % self.title
