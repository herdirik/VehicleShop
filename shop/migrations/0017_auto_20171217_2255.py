# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 22:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20171217_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='photo',
            field=models.ImageField(blank=True, default='vehicle_image/def_car.png', null=True, upload_to='vehicle_image'),
        ),
    ]
