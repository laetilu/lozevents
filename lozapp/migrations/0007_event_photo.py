# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lozapp', '0006_event_date_creation'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='photo',
            field=models.ImageField(null=True, upload_to='events'),
        ),
    ]
