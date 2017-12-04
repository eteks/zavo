# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from marketing.models import Marketing

# Create your models here.
class Booking(models.Model):
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
	MEALPLAN = (
		('EP','EP'),
		('CP','CP'),
		('MAP','MAP'),
		('AP','AP')
	)
	PAYMENTMODE = (
		('CASH','CASH'),
		('CHEQUE/DD','CHEQUE/DD'),
		('NET BANKING','NET BANKING')
	)
	package_Name = models.ForeignKey(Marketing,verbose_name = 'Package Name',max_length=50,related_name = 'package')
	contactAddress = models.TextField(verbose_name = 'Contact Address',max_length=200)
	contactMobile = models.CharField(verbose_name = 'Mobile',max_length=50)
	contactMail = models.EmailField(verbose_name = 'Email')
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
	mealPlan = models.CharField(verbose_name =  'Meal Plan',choices = MEALPLAN, max_length = 50)
	modePayment = models.CharField(verbose_name = 'Mode of Payment',choices = PAYMENTMODE, max_length = 20)
	notes = models.TextField(verbose_name = "Notes, if any")
