# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 11:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=50, verbose_name=b'Email ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='mobileNumber',
            field=models.CharField(default=django.utils.timezone.now, max_length=10, verbose_name=b'Mobile Number'),
            preserve_default=False,
        ),
    ]
