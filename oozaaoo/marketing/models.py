# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.functional import lazy
from django.db import models

ACCOMODATION_TYPE = (
		('1', 'Hotel'),
		('2', 'Resort')
	)
ACCOMODATION_STAR =	(
		('1','2 Star'),
		('2','3 Star'),
		('3','4 Star'),
		('4','5 Star')
	)
MODEOFTRANSPORT = (
    	('1','FLIGHT'),
    	('2','TRAIN'),
    	('3','BUS'),
    	('4','CAR'),
    	('5','GROUP')
	)
FLIGHT = (
		('1','ECONOMY'),
	    ('2','BUSINESS CLASS')
	)
TRAIN = (
		('1','AC'),
	 	('2','NON AC')
	)
BUS = (
		('1','SLEEPER'),
		('2','SEMI-SLEEPER')
	)
CAR = (
		('1','INDIGO'),
		('2','INNOVA'),
		('3','TEMPO')
	)
GROUP = (
		 ('1','MINI BUS'),
		 ('2','BUS')
	)

class accomodationTypeCreation(models.Model):
	accomodationType = models.CharField(verbose_name = 'Accomodation Type', max_length = 50)

	def __str__(self):
		return self.accomodationType

class accomodationStarCreation(models.Model):
	accomodationStar = models.CharField(verbose_name = 'Accomodation in Star Hotel', max_length = 50)

	def __str__(self):
		return self.accomodationStar

class accomodationType(models.Model):
	accomodationType = models.ForeignKey(accomodationTypeCreation, related_name = 'accomodationType_marketing', verbose_name = "Accomodation Type", null=True, blank=True)
	accomodationStar = models.ForeignKey(accomodationStarCreation,verbose_name = "Accomodation in Star hotel", related_name = 'accomodation_Star')

	def __str__(self):
		return unicode(self.accomodationStar)

class modeOfTransportCreation(models.Model):
	mode = models.CharField(verbose_name = "Mode of Transport", max_length = 255)

	def __str__(self):
		return self.mode

class transportTypeCreation(models.Model):
	modeOfTransport = models.ForeignKey(modeOfTransportCreation, verbose_name = "Mode of transport", related_name = "modeOfTransport")
	transportType = models.CharField(verbose_name = "Transport Facility", max_length = 255)

	def __str__(self):
		return self.transportType

class modeOfTransport(models.Model):
	modeOfTransport = models.ForeignKey(modeOfTransportCreation, verbose_name = "Mode of Transport", related_name = "modeOftrasnportCreation_modeOfTransport")
	transportType = models.ForeignKey(transportTypeCreation,verbose_name = "Transport Facility", related_name = "transportType_modeOfTransport")

	def __str__(self):
		return unicode(self.transportType)

class Marketing(models.Model):
	packageName = models.CharField(verbose_name = 'Package Name',max_length=50)
	contactAddress = models.TextField(verbose_name = 'Contact Address',max_length=200)
	contactMobile = models.CharField(verbose_name = 'Mobile',max_length=50)
	contactMail = models.EmailField(verbose_name = 'Email',max_length = 50)
	dateDeparture = models.DateField(verbose_name = 'Date of Departure')
	dateArrival = models.DateField(verbose_name = 'Date of Arrival')
	duration = models.IntegerField(verbose_name = 'Duration')
	totalPersons = models.IntegerField(verbose_name = 'Total number of persons')
	adultPersons = models.IntegerField(verbose_name = 'No. of adults')
	childPersons = models.IntegerField(verbose_name = 'No. of Children')
	infantPersons = models.IntegerField(verbose_name = 'No. of infants')
	breakfast = models.BooleanField(verbose_name = 'Breakfast included')
	lunch = models.BooleanField(verbose_name = 'Lunch included')
	dinner = models.BooleanField(verbose_name = 'Dinner included')
	notes = models.TextField(verbose_name = "Notes, if any")
	accomodation = models.ManyToManyField(accomodationType, verbose_name = 'Accomodation Type')
	modeOfTransport = models.ManyToManyField(modeOfTransport, verbose_name = 'Mode of Transport')

	def __str__(self):
		return unicode(self.id)

# class accomodationStar(models.Model):
# 	marketing_id = models.ForeignKey(Marketing, related_name = 'Marketing_accomodationtype',null=True, blank=True, default = '0')
# 	accomodationType = models.ForeignKey(accomodationType, related_name = 'accomodationStar_accomodationType', verbose_name = "Accomodation Type", null=True, blank=True, default = '0')
# 	accomodationStar = models.ForeignKey(accomodationStarCreation,verbose_name = "Accomodation in Star hotel", related_name = 'accomodation_Star')


# 	def __str__(self):
# 		return self.accomodationStar

# class modeOfTransport(models.Model):
# 	mode = models.CharField(verbose_name = "Mode of Transport", max_length = 255, choices = MODEOFTRANSPORT, default = '0')
# 	modeOfTransport = models.ManyToManyField(Marketing,through='transportType')

# 	def __str__(self):
# 		return self.modeOfTransport

# class transportType(models.Model):
# 	marketing_id = models.ForeignKey(Marketing, null = True, blank = False, related_name = 'Marketing_transportType')
# 	modeOfTransport = models.ForeignKey(modeOfTransport, related_name = 'modeOfTransport_transportType', default = '0')
# 	transportType = models.CharField(verbose_name = 'Transport Type', max_length = 25, choices = FLIGHT,default = '0')
