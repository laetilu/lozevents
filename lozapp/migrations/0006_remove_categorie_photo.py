# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-17 13:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lozapp', '0005_categorie_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='photo',
        ),
    ]
