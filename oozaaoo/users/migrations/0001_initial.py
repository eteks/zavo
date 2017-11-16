# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 12:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[(b'SuperAdmin', b'SuperAdmin'), (b'Admin', b'Admin'), (b'Marketing', b'Marketing'), (b'Operations', b'Operations'), (b'Co-ordination', b'Co-ordination'), (b'Finance', b'Finance')], max_length=50, verbose_name=b'User type')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]