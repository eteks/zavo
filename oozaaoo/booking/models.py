# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tourpackage.models import Tourpackage
from customer.models import Customer
from master.models import *

# Create your models here.
class Booking(AbstractDefault):
	customer = models.ForeignKey(Customer, verbose_name = 'Customer ID')
	booking_id = models.CharField(verbose_name='Auto generated booking Id',max_length=500, null = True)
	package = models.ForeignKey(Tourpackage,verbose_name = 'Package Name',max_length=50,related_name = 'package', null = True)	
	departure_date = models.DateField(verbose_name = 'Date of Departure')
	arrival_date = models.DateField(verbose_name = 'Date of Arrival')
	no_of_days = models.IntegerField(verbose_name = 'No. of days')
	no_of_nights = models.IntegerField(verbose_name = 'No. of nights')
	no_of_adult = models.IntegerField(verbose_name = 'No. of adults')
	no_of_children = models.IntegerField(verbose_name = 'No. of Children')
	no_of_infant = models.IntegerField(verbose_name = 'No. of Infant')
	total_person = models.IntegerField(verbose_name = 'Total Person')
	package_cost = models.DecimalField(verbose_name = 'Package Cost (Adult)', max_digits = 10, decimal_places = 2,default = 0 ) #Automatic generation
	discount = models.DecimalField(verbose_name = 'Discount (if any)', max_digits = 10, decimal_places = 2,default = 0) #Automatic generation
	total_cost = models.DecimalField(verbose_name = 'Total Cost', max_digits = 10, decimal_places = 2,default = 0) #Automatic generation
	paid_amount = models.DecimalField(verbose_name = 'Paid Amount', max_digits = 10, decimal_places = 2,default = 0) #Automatic generation
	accomodation = models.ManyToManyField(AccomodationStar, verbose_name = 'Accomodation Type and Star',default = 0)
	mode_of_transport = models.ManyToManyField(TransportType, verbose_name = 'Mode of Transport and Type',default = 0)
	mealplan = models.CharField(verbose_name = 'Meal Plan', max_length = 100,choices=MEAL_PLAN,default = 0) #Multiple select in checkboxes
	mealPlan_type = models.CharField(verbose_name = 'Meal Plan Type', max_length = 100,choices=MEAL_PLAN_TYPE,default = 0) #Multiple select in checkboxes
	remarks = models.TextField(verbose_name = "Notes, if any")
	booking_confirmation_status = models.BooleanField(verbose_name ='Booking Team Confirmation status', default = False)
	coordination_confirmation_status = models.BooleanField(verbose_name ='Co-ordination Team Confirmation status', default = False)
	finance_confirmation_status = models.BooleanField(verbose_name ='Finance Team Confirmation status', default = False)

	def __str__(self):
		return self.customer.customer_name

class Coordination(Booking):
    class Meta:
        proxy = True

class Finance(Coordination):
    class Meta:
        proxy = True