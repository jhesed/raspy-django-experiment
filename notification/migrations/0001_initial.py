# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160426221900 on 2016-04-29 21:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('villager_id', models.IntegerField()),
                ('house_coordinates', models.CharField(help_text='i.e. 99,402,20', max_length=50)),
                ('gmap_coordinates', models.CharField(blank=True, max_length=50)),
                ('date_created', models.DateField(auto_now=True)),
            ],
        ),
    ]
