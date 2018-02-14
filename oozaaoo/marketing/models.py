# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.functional import lazy
from django.db import models
from customer.models import Customer
from master.models import accomodationType,modeOfTransport

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

class Marketing(models.Model):
	customer_id = models.ForeignKey(Customer, verbose_name = 'Customer ID')
	placesWishList = models.CharField(verbose_name = 'Places to Visit',max_length=50)
	dateDeparture = models.DateField(verbose_name = 'Date of Departure')
	dateArrival = models.DateField(verbose_name = 'Date of Arrival')
	duration = models.IntegerField(verbose_name = 'Duration')
	totalPersons = models.IntegerField(verbose_name = 'Total number of persons')
	adultPersons = models.IntegerField(verbose_name = 'No. of adults')
	childPersons = models.IntegerField(verbose_name = 'No. of Children')
	infantPersons = models.IntegerField(verbose_name = 'No. of infants')
	mealPlan = models.CharField(verbose_name = 'Meal Plan', max_length = 50)
	mealPlanType = models.CharField(verbose_name = 'Meal Plan Type', max_length = 50)
	notes = models.TextField(verbose_name = "Notes, if any")
	accomodation = models.ManyToManyField(accomodationType, verbose_name = 'Accomodation Type')
	modeOfTransport = models.ManyToManyField(modeOfTransport, verbose_name = 'Mode of Transport')
	confirmation_status = models.BooleanField(verbose_name = 'Customer contacted', default = False)

	def __str__(self):
		return unicode(self.id)
