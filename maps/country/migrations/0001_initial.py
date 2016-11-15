# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 23:46
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryGeo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital', models.CharField(max_length=100)),
                ('capital_geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='world.Country')),
            ],
        ),
    ]