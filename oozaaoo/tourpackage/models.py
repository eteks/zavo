# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from forms import TourFileForm
from django.db import models
from master.models import AbstractDefault
from master.action import *

# Create your models here.

class Tourpackage(AbstractDefault):
	package_name = models.CharField(verbose_name = 'Package Name', max_length = 50)
	package_description = models.TextField(verbose_name = 'Package Description', max_length = 1000)
	package_location = models.CharField(verbose_name = 'Location', max_length = 50)
	package_photos = models.ImageField(verbose_name = 'Photos to Upload',upload_to = update_image,max_length = 255, default = '')	
	package_document = models.FileField(verbose_name = 'Package Document',upload_to = update_file, default = '')	
	no_of_days = models.IntegerField(verbose_name = 'No. of days')
	no_of_nights = models.IntegerField(verbose_name = 'No. of nights')
	adult_cost = models.DecimalField(verbose_name = 'Package Cost (Adult)', max_digits = 10, decimal_places = 2)
	children_cost = models.DecimalField(verbose_name = 'Package Cost (Children)', max_digits = 10, decimal_places = 2)
	infant_cost = models.DecimalField(verbose_name = 'Package Cost (Infant)', max_digits = 10, decimal_places = 2)

	def __str__(self):
		return self.package_name

	def gal_image(self):
		files = str(self.package_photos).split(',')
		count=len(files)
		filer=''
		if count > 1:
			for x in files:
				filer = filer + '<img src="'+settings.SITE_URL+'%s" width="100px"/>' % str(x) + '&nbsp;'
			return filer
		else:
			return 'None'	
	gal_image.allow_tags = True
	gal_image.short_description = 'Image'