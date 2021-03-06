# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160426221900 on 2016-04-27 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Villager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=50)),
                ('address', models.TextField()),
                ('house_coordinates', models.CharField(max_length=50)),
                ('gmap_coordinates', models.CharField(blank=True, max_length=50)),
                ('date_created', models.DateField()),
            ],
        ),
    ]
