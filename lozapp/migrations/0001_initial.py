# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 10:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=45)),
                ('zipcode', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('begin_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('desc', models.TextField()),
                ('is_validated', models.BooleanField(default=False)),
                ('addr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lozapp.Address')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lozapp.Categorie')),
                ('participant', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
