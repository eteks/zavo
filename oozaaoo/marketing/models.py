# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.functional import lazy
from django.db import models
from customer.models import Customer
from master.models import *
from booking.models import Booking
import datetime

# ACCOMODATION_TYPE = (
# 		('1', 'Hotel'),
# 		('2', 'Resort')
# 	)
# ACCOMODATION_STAR =	(
# 		('1','2 Star'),
# 		('2','3 Star'),
# 		('3','4 Star'),
# 		('4','5 Star')
# 	)
# MODEOFTRANSPORT = (
#     	('1','FLIGHT'),
#     	('2','TRAIN'),
#     	('3','BUS'),
#     	('4','CAR'),
#     	('5','GROUP')
# 	)
# FLIGHT = (
# 		('1','ECONOMY'),
# 	    ('2','BUSINESS CLASS')
# 	)
# TRAIN = (
# 		('1','AC'),
# 	 	('2','NON AC')
# 	)
# BUS = (
# 		('1','SLEEPER'),
# 		('2','SEMI-SLEEPER')
# 	)
# CAR = (
# 		('1','INDIGO'),
# 		('2','INNOVA'),
# 		('3','TEMPO')
# 	)
# GROUP = (
# 		 ('1','MINI BUS'),
# 		 ('2','BUS')
# 	)

class Marketing(AbstractDefault):
	customer = models.ForeignKey(Customer, verbose_name = 'Customer ID')
	places_to_visit = models.CharField(verbose_name = 'Places to Visit',max_length=50)
	departure_date = models.DateField(verbose_name = 'Date of Departure')
	arrival_date = models.DateField(verbose_name = 'Date of Arrival')
	no_of_days = models.IntegerField(verbose_name = 'No. of days')
	no_of_nights = models.IntegerField(verbose_name = 'No. of nights')
	no_of_adult = models.IntegerField(verbose_name = 'No. of adults')
	no_of_children = models.IntegerField(verbose_name = 'No. of Children')
	no_of_infant = models.IntegerField(verbose_name = 'No. of Infant')
	total_person = models.IntegerField(verbose_name = 'Total Person')	
	accomodation = models.ManyToManyField(AccomodationStar, verbose_name = 'Accomodation Type')
	mode_of_transport = models.ManyToManyField(TransportType, verbose_name = 'Mode of Transport')
	mealplan = models.CharField(verbose_name = 'Meal Plan', max_length = 100,choices=MEAL_PLAN) #Multiple select in checkboxes
	mealPlan_type = models.CharField(verbose_name = 'Meal Plan Type', max_length = 100,choices=MEAL_PLAN_TYPE) #Multiple select in checkboxes
	remarks = models.TextField(verbose_name = "Notes, if any")
	marketing_confirmation_status = models.BooleanField(verbose_name ='Martketing Team Confirmation status', default = False)

	def __str__(self):
		return unicode(self.id)

	def save(self, *args, **kwargs):
		if(self.marketing_confirmation_status):
			b = Booking.objects.filter(created_date__startswith = datetime.date.today()).count()
			if(self.created_date.month >= 10):
				month = str(self.created_date.month)
			else:
				month = '0' + str(self.created_date.month)
			if(self.created_date.day >= 10):
				day = str(self.created_date.day)
			else:
				day = '0' + str(self.created_date.day)
			book = Booking(customer = self.customer, remarks = self.remarks, departure_date = self.departure_date, arrival_date = self.arrival_date, no_of_days = self.no_of_days, 
				no_of_nights = self.no_of_nights, no_of_adult = self.no_of_adult, no_of_infant = self.no_of_infant, no_of_children = self.no_of_children, total_person = self.total_person,
				booking_id = 'BOOKID' + '_' + unicode(day +  month + str(self.created_date.year)) + '_' + str(b+1))
			# myMovieGenre = Movie_Info_genre.objects.create(genre='horror')
			# accomodation = AccomodationStar.objects.create(accomodation_star = )
			book.save()

		super(Marketing, self).save(*args, **kwargs)
