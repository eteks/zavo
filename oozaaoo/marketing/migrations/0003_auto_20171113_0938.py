# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 09:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_auto_20171113_0930'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Marketing',
            new_name='TourPackage',
        ),
    ]
