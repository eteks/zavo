# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Marketing(models.Model):
	ACCOMODATION_TYPE = (
		('Hotel', 'Hotel'),
		('Resort', 'Resort')
	)
	ACCOMODATION_STAR =	(
		('2 Star','2'),
		('3 Star','3'),
		('4 Star','4'),
		('5 Star','5')
	)
	MODEOFTRANSPORT = (
    	('FLIGHT',(
    		('ECONOMY','ECONOMY'),
    		('BUSINESS CLASS','BUSINESS CLASS')
    		)
    	),
    	('TRAIN',(
    		('AC','AC'),
    		('NON AC','NON AC')
    		)
    	),
    	('BUS',(
    		('SLEEPER','SLEEPER'),
    		('SEMI-SLEEPER','SEMI-SLEEPER')
    		)
    	),
    	('CAR',(
    		('INDIGO','INDIGO'),
    		('INNOVA','INNOVA'),
    		('TEMPO','TEMPO')
    		)
    	),
    	('GROUP',(
    		('MINI BUS','MINI BUS'),
    		('BUS','BUS')
    		)
    	)
	)
	
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
	accomodationType  = models.CharField(verbose_name = 'Accomodation type', choices = ACCOMODATION_TYPE,max_length = 50)
	accomodationStar = models.CharField(verbose_name = 'Accomodation in Star Hotel', choices = ACCOMODATION_STAR,max_length = 50)
	modeOfTransport = models.CharField(verbose_name = 'Mode of Transport', choices = MODEOFTRANSPORT,max_length = 50)
	breakfast = models.BooleanField(verbose_name = 'Breakfast included')
	lunch = models.BooleanField(verbose_name = 'Lunch included')
	dinner = models.BooleanField(verbose_name = 'Dinner included')
	notes = models.TextField(verbose_name = "Notes, if any")


	def __str__(self):
		return self.packageName


