# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-21 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('manufacturerName', models.CharField(max_length=200)),
                ('manufacturerLat', models.DecimalField(decimal_places=6, max_digits=10)),
                ('manufacturerLon', models.DecimalField(decimal_places=6, max_digits=10)),
                ('supplierName', models.CharField(max_length=200)),
                ('dateOfPurchase', models.DateTimeField(auto_now_add=True)),
                ('availability', models.BooleanField(default=False)),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
                ('skuNo', models.IntegerField()),
                ('metaDescription', models.TextField()),
                ('category', models.IntegerField(choices=[(1, b'ENGINE'), (2, b'BRAKES'), (3, b'TRANSMISSION'), (4, b'SUSPENSION'), (5, b'BODY'), (6, b'ELECTRICAL'), (7, b'HEATING VENTILATION & A')])),
                ('subcategory', models.IntegerField(choices=[(1, b'FILTERS')])),
                ('imageUrl', models.URLField(default=b'default.jpg')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]