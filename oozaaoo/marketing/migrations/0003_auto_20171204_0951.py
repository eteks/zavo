# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_auto_20171204_0517'),
    ]

    operations = [
        migrations.CreateModel(
            name='combined',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combined', models.CharField(max_length=255, verbose_name='COmbined')),
            ],
        ),
        migrations.CreateModel(
            name='modeOfTransport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='modeOfTransportCreation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=255, verbose_name='Mode of Transport')),
            ],
        ),
        migrations.CreateModel(
            name='transportTypeCreation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transportType', models.CharField(max_length=255, verbose_name='Transport Facility')),
                ('modeOfTransport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modeOfTransport', to='marketing.modeOfTransportCreation', verbose_name='Mode of transport')),
            ],
        ),
        migrations.AddField(
            model_name='modeoftransport',
            name='modeOfTransport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modeOftrasnportCreation_modeOfTransport', to='marketing.modeOfTransportCreation', verbose_name='Mode of Transport'),
        ),
        migrations.AddField(
            model_name='modeoftransport',
            name='transportType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transportType_modeOfTransport', to='marketing.transportTypeCreation', verbose_name='Transport Facility'),
        ),
        migrations.AddField(
            model_name='marketing',
            name='modeOfTransport',
            field=models.ManyToManyField(to='marketing.modeOfTransport'),
        ),
    ]