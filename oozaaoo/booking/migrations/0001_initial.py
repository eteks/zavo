# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 12:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactAddress', models.TextField(max_length=200, verbose_name='Contact Address')),
                ('contactMobile', models.CharField(max_length=50, verbose_name='Mobile')),
                ('contactMail', models.EmailField(max_length=254, verbose_name='Email')),
                ('dateDeparture', models.DateField(verbose_name='Date of Departure')),
                ('dateArrival', models.DateField(verbose_name='Date of Arrival')),
                ('duration', models.IntegerField(verbose_name='Duration')),
                ('totalPersons', models.IntegerField(verbose_name='Total number of persons')),
                ('adultPersons', models.IntegerField(verbose_name='No. of adults')),
                ('childPersons', models.IntegerField(verbose_name='No. of Children')),
                ('infantPersons', models.IntegerField(verbose_name='No. of infants')),
                ('accomodationType', models.CharField(choices=[('Hotel', 'Hotel'), ('Resort', 'Resort')], max_length=50, verbose_name='Accomodation type')),
                ('accomodationStar', models.CharField(choices=[('2 Star', '2'), ('3 Star', '3'), ('4 Star', '4'), ('5 Star', '5')], max_length=50, verbose_name='Accomodation in Star Hotel')),
                ('modeOfTransport', models.CharField(choices=[('FLIGHT', (('ECONOMY', 'ECONOMY'), ('BUSINESS CLASS', 'BUSINESS CLASS'))), ('TRAIN', (('AC', 'AC'), ('NON AC', 'NON AC'))), ('BUS', (('SLEEPER', 'SLEEPER'), ('SEMI-SLEEPER', 'SEMI-SLEEPER'))), ('CAR', (('INDIGO', 'INDIGO'), ('INNOVA', 'INNOVA'), ('TEMPO', 'TEMPO'))), ('GROUP', (('MINI BUS', 'MINI BUS'), ('BUS', 'BUS')))], max_length=50, verbose_name='Mode of Transport')),
                ('mealPlan', models.CharField(choices=[('EP', 'EP'), ('CP', 'CP'), ('MAP', 'MAP'), ('AP', 'AP')], max_length=50, verbose_name='Meal Plan')),
                ('modePayment', models.CharField(choices=[('CASH', 'CASH'), ('CHEQUE/DD', 'CHEQUE/DD'), ('NET BANKING', 'NET BANKING')], max_length=20, verbose_name='Mode of Payment')),
                ('notes', models.TextField(verbose_name='Notes, if any')),
                ('package_Name', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='package', to='marketing.Marketing', verbose_name='Package Name')),
            ],
        ),
    ]
