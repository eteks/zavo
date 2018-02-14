from __future__ import unicode_literals

from django.db import models

# Create your models here.

MEAL_PLAN = (
		('Breakfast', 'BREAKFAST'),
		('Lunch', 'LUNCH'),
		('Dinner','DINNER')
	)
MEAL_PLAN_TYPE = (
		('ep', 'EP'),
		('cp', 'CP'),
		('map','MAP'),
		('ap','AP')
	)
PAYMENT_MODE = (
	('online','ONLINE'),
	('cheque/dd','CHEQUE/DD'),
	('cash','CASH')
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