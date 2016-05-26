from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from lozapp.models import Categorie, Address

from userena.models import UserenaBaseProfile
from django.utils.translation import ugettext as _

class ProfilePart(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile_part')
    address = models.ForeignKey(Address, null=True)
    favorite_categories = models.ManyToManyField(Categorie)


class ProfilePro(ProfilePart):
    company_name = models.CharField(max_length=200)
    siret = models.IntegerField()
    number = models.IntegerField()
    def __unicode__(self):
        return "%s" % self.company_name
