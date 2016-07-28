# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('Address_Id', models.PositiveIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=1000)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('Address_Street_Name', models.CharField(max_length=1000)),
                ('Landmark', models.CharField(max_length=1000)),
                ('Pin_Code', models.IntegerField()),
                ('City', models.IntegerField()),
                ('State', models.IntegerField()),
                ('Location', models.IntegerField()),
            ],
            options={
                'ordering': ('-Created',),
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('Brand_Id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Brand_Name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('Car_Name', models.CharField(max_length=1000)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Last_updated', models.DateTimeField(auto_now=True)),
                ('Car_Id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Manufacturer_Name', models.IntegerField()),
                ('Model_Name', models.IntegerField()),
                ('Version', models.IntegerField()),
                ('Fuel_Type', models.IntegerField()),
                ('Transmission', models.IntegerField()),
                ('Year', models.DateField()),
            ],
            options={
                'ordering': ('-Created',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Category_Name', models.CharField(max_length=1000)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Last_updated', models.DateTimeField(auto_now=True)),
                ('Category_Id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Parent_Id', models.PositiveIntegerField(unique=True)),
            ],
            options={
                'ordering': ('-Created',),
            },
        ),
        migrations.CreateModel(
            name='CategoryDescription',
            fields=[
                ('Category_Description_Id', models.PositiveIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Last_updated', models.DateTimeField(auto_now=True)),
                ('Category_Image_URL', models.CharField(max_length=1000)),
                ('Category_Description', models.TextField(max_length=1000)),
                ('Category_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jsonapi.Category')),
            ],
            options={
                'ordering': ('-Created',),
            },
        ),
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('Garage_Id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Last_updated', models.DateTimeField(auto_now=True)),
                ('Garage_Name', models.CharField(max_length=1000)),
                ('Year_of_Establishment', models.DateField()),
                ('Email_Id', models.CharField(max_length=1000)),
                ('Opening_Time', models.TimeField()),
                ('Closing_Time', models.TimeField()),
                ('Days_of_Operation', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('-Created',),
            },
        ),
        migrations.CreateModel(
            name='LatLon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.DecimalField(decimal_places=3, max_digits=8)),
                ('Longitude', models.DecimalField(decimal_places=3, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('Manufacturer_Name', models.CharField(max_length=1000)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Last_updated', models.DateTimeField(auto_now=True)),
                ('Manufacturer_Id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Manufacturer_Location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jsonapi.LatLon')),
            ],
            options={
                'ordering': ('-Created',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Product_Name', models.CharField(max_length=255)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Last_updated', models.DateTimeField(auto_now=True)),
                ('Product_Id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Product_Unique_Name', models.CharField(max_length=1000)),
                ('Brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jsonapi.Brand')),
                ('Compatible_Car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jsonapi.Car')),
            ],
            options={
                'ordering': ('-Created',),
            },
        ),
        migrations.AddField(
            model_name='category',
            name='Manufacturer_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jsonapi.Manufacturer'),
        ),
        migrations.AddField(
            model_name='category',
            name='Product_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jsonapi.Product'),
        ),
        migrations.AddField(
            model_name='address',
            name='Manufacturer_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jsonapi.Manufacturer'),
        ),
    ]
