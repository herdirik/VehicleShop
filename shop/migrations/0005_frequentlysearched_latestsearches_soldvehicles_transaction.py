# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 16:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrequentlySearched',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='LatestSearches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='SoldVehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.PositiveIntegerField(max_length=4)),
                ('description', models.CharField(max_length=255)),
                ('km', models.PositiveIntegerField()),
                ('engine', models.FloatField()),
                ('transmission', models.CharField(max_length=10)),
                ('fuel', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('searched_counter', models.IntegerField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Brand')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
                ('firm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Firm')),
                ('photo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Photo')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer_user', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller_user', to=settings.AUTH_USER_MODEL)),
                ('sold_vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.Vehicle')),
            ],
        ),
    ]
