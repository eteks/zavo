# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tourpackage(models.Model):
	packageName = models.CharField(verbose_name = 'Package Name', max_length = 50)
	adultCost = models.DecimalField(verbose_name = 'Package Cost (Adult)', max_digits = 10, decimal_places = 2)
	childrenCost = models.DecimalField(verbose_name = 'Package Cost (Children)', max_digits = 10, decimal_places = 2)
	infantCost = models.DecimalField(verbose_name = 'Package Cost (Infant)', max_digits = 10, decimal_places = 2)
	packageDescription = models.TextField(verbose_name = 'Package Description', max_length = 1000)
	packagePhotos = models.ImageField(verbose_name = 'Photos to Upload',upload_to = 'images/',max_length = 255)
	location = models.CharField(verbose_name = 'Location', max_length = 50)
	noOfDays = models.IntegerField(verbose_name = 'No. of days')
	noOfNights = models.IntegerField(verbose_name = 'No. of nights')

	def __str__(self):
		return self.packageName