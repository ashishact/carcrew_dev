# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 05:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jsonapi', '0005_remove_product_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='Number_of_KMs_Travelled',
            new_name='Number_of_KMs',
        ),
    ]
