# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 13:16
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0006_remove_users_mobilenumber'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='users',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_type',
        ),
        migrations.AddField(
            model_name='users',
            name='mobileNumber',
            field=models.CharField(default=b'0', max_length=10, verbose_name=b'Mobile Number'),
        ),
        migrations.AddField(
            model_name='users',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default='0', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]