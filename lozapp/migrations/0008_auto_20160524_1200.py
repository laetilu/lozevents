# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-24 10:00
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lozapp', '0007_event_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='poly',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]