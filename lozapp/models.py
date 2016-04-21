from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=45)
    date = models.DateTimeField()
    place = models.CharField(max_length=45)
    descriptive = models.TextField()

    categorie = models.ForeignKey(Categorie)
    pro = models.ForeignKey(Pro)
    city = models.ForeignKey(City)

    def __unicode__(self):
        return "%s" % self.titre


class Validation_event(models.Model):
    date_validation = models.DateTimeField(auto_now_add=True)
    validation_event = models.BooleanField(default=False)

    administrator = models.ForeignKey(Administrator)
    event = models.ForeignKey(Event)

# class Administrator(models.Model):
#     mail = models.EmailField(max_length=254)
#     password =

class Validation_pro(models.Model):
    date_validation = models.DateTimeField(auto_now_add=True)
    validation_siret = models.BooleanField(default=False)

    pro = models.ForeignKey(Pro)
    administrator = models.ForeignKey(Administrator)

class Pro(models.Model):
    name = models.CharField(max_length=45)
    adress = models.CharField(max_length=70)
    siret = models.IntegerField()

    user = models.ForeignKey(User)

class City(models.Model):
    name = models.CharField(max_length=45)
    cp = models.IntegerField()
    gps_x = models.IntegerField()
    gps_y = models.IntegerField()

class Favorite(models.Model):

    user = models.ForeignKey(User)
    categorie = models.ForeignKey(Categorie)

class Participation(models.Model):
    is_present = models.BooleanField(default=False)

    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)

class Categorie(models.Model):
    name = models.CharField(max_length=45)
