from __future__ import unicode_literals

from django.db import models

from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from django.contrib.auth.models import User


# Create your models here.

class Categorie(models.Model):
    name = models.CharField(max_length=45)

    def __unicode__(self):
        return "%s" % self.name


class Pro(models.Model):
    name = models.CharField(max_length=45)
    adress = models.CharField(max_length=70)
    siret = models.IntegerField()

    user = models.ForeignKey(User)

    def __unicode__(self):
        return "%s" % self.name


class City(models.Model):
    name = models.CharField(max_length=45)
    cp = models.IntegerField()
    gps_x = models.IntegerField()
    gps_y = models.IntegerField()

    def __unicode__(self):
        return "%s" % self.name

class Administrator(models.Model):
    mail = models.EmailField(max_length=254)

    def __unicode__(self):
        return "%s" % self.mail


class Event(models.Model):
    title = models.CharField(max_length=45)
    date = models.DateTimeField()
    place = models.CharField(max_length=45)
    descriptive = models.TextField()

    categorie = models.ForeignKey(Categorie)
    pro = models.ForeignKey(Pro)
    city = models.ForeignKey(City)

    def __unicode__(self):
        return "%s" % self.title


class Validation_event(models.Model):
    date_validation = models.DateTimeField(auto_now_add=True)
    validation_event = models.BooleanField(default=False)

    administrator = models.ForeignKey(Administrator)
    event = models.ForeignKey(Event)

    def __unicode__(self):
        return "%s" % self.date_validation



class Validation_pro(models.Model):
    date_validation = models.DateTimeField(auto_now_add=True)
    validation_siret = models.BooleanField(default=False)

    pro = models.ForeignKey(Pro)
    administrator = models.ForeignKey(Administrator)

    def __unicode__(self):
        return "%s" % self.date_validation


class Favorite(models.Model):

    user = models.ForeignKey(User)
    categorie = models.ForeignKey(Categorie)

    def __unicode__(self):
        return "%s" % self.categorie


class Participation(models.Model):
    is_present = models.BooleanField(default=False)

    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)

    def __unicode__(self):
        return "%s" % self.is_present

class LozApp(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
